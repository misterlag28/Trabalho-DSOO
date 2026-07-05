from modelos.atendimento.procedimento import Procedimento
from daos.atendimento_dao import AtendimentoDAO

class ControladorProcedimento:
    def __init__(self):
        self.__atendimento_dao = AtendimentoDAO()

    def registrar_procedimento(self, atendimento, procedimento):
        # Validações de negócio
        if not procedimento.nome or not procedimento.nome.strip():
            raise ValueError("Nome do procedimento é obrigatório")
        if procedimento.custo <= 0:
            raise ValueError("Custo do procedimento deve ser positivo")
        if not procedimento.profissional:
            raise ValueError("Profissional é obrigatório para o procedimento")

        if atendimento.paciente.idade < 18:
            raise ValueError("Paciente menor de 18 anos não pode realizar procedimento")

        if atendimento.clinica.abertura and atendimento.clinica.fechamento:
            if atendimento.horario_inicio < atendimento.clinica.abertura or atendimento.horario_fim > atendimento.clinica.fechamento:
                raise ValueError("Horário do atendimento fora do horário de funcionamento da clínica")
        
        procedimento.validar_procedimento()
        atendimento.adicionar_procedimento(procedimento)
        self.__atendimento_dao.update(atendimento)
        return procedimento

    def listar_procedimentos(self, atendimento):
        return atendimento.lista_procedimentos

    def escolher_procedimento_por_index(self, atendimento, index: int):
        if not atendimento.lista_procedimentos:
            return None
        if index < 0 or index >= len(atendimento.lista_procedimentos):
            return None
        return atendimento.lista_procedimentos[index]

    def alterar_procedimento(self, atendimento, procedimento, *, nome=None, descricao=None, custo=None):
        if nome is not None:
            if not nome.strip():
                raise ValueError("Nome do procedimento não pode estar vazio")
            procedimento.nome = nome
        if descricao is not None:
            procedimento.descricao = descricao
        if custo is not None:
            if custo <= 0:
                raise ValueError("Custo do procedimento deve ser positivo")
            procedimento.custo = custo
        procedimento.validar_procedimento()
        self.__atendimento_dao.update(atendimento)

    def excluir_procedimento(self, atendimento, procedimento):
        if procedimento in atendimento.lista_procedimentos:
            atendimento.lista_procedimentos.remove(procedimento)
            self.__atendimento_dao.update(atendimento)
            return True
        return False
