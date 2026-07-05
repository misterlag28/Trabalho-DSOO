from datetime import time
from modelos.atendimento.atendimento import Atendimento
from daos.atendimento_dao import AtendimentoDAO

class ControladorAtendimento:
    def __init__(self):
        self.__atendimento_dao = AtendimentoDAO()

    def limpar_dados(self):
        self.__atendimento_dao.clear()

    def cadastrar_atendimento(self, atendimento: Atendimento) -> None:
        if atendimento.horario_inicio is None or atendimento.horario_fim is None:
            raise ValueError("Horário de início e fim são obrigatórios")
        if atendimento.horario_fim <= atendimento.horario_inicio:
            raise ValueError("Horário fim deve ser maior que horário de início")
        if atendimento.valor <= 0:
            raise ValueError("Valor do atendimento deve ser positivo")
        if atendimento.paciente is None:
            raise ValueError("Paciente é obrigatório")
        if atendimento.profissional is None:
            raise ValueError("Profissional é obrigatório")
        if atendimento.clinica is None:
            raise ValueError("Clínica é obrigatória")
        if atendimento.tipo is None:
            raise ValueError("Tipo de atendimento é obrigatório")

        if atendimento.paciente.idade < 18:
            raise ValueError("Paciente menor de 18 anos não pode realizar atendimento")

        if atendimento.clinica.abertura and atendimento.clinica.fechamento:
            if atendimento.horario_inicio < atendimento.clinica.abertura or atendimento.horario_fim > atendimento.clinica.fechamento:
                raise ValueError("Horário do atendimento fora do horário de funcionamento da clínica")
        
        self.__atendimento_dao.add(atendimento)

    def listar_atendimentos(self):
        return self.__atendimento_dao.get_all()

    def escolher_atendimento_por_index(self, index: int):
        atendimentos = self.listar_atendimentos()
        if index < 0 or index >= len(atendimentos):
            return None
        return atendimentos[index]

    def excluir_atendimento(self, atendimento: Atendimento) -> bool:
        if self.__atendimento_dao.get(atendimento.id):
            self.__atendimento_dao.remove(atendimento.id)
            return True
        return False

    def alterar_atendimento(self, atendimento: Atendimento, **kwargs) -> bool:
        if 'data' in kwargs and kwargs['data'] is not None:
            atendimento.data = kwargs['data']
        if 'horario_inicio' in kwargs and kwargs['horario_inicio'] is not None:
            atendimento.horario_inicio = kwargs['horario_inicio']
        if 'horario_fim' in kwargs and kwargs['horario_fim'] is not None:
            atendimento.horario_fim = kwargs['horario_fim']
        if 'valor' in kwargs and kwargs['valor'] is not None:
            atendimento.valor = kwargs['valor']
        if 'profissional' in kwargs and kwargs['profissional'] is not None:
            atendimento.profissional = kwargs['profissional']
        if 'paciente' in kwargs and kwargs['paciente'] is not None:
            atendimento.paciente = kwargs['paciente']
        if 'clinica' in kwargs and kwargs['clinica'] is not None:
            atendimento.clinica = kwargs['clinica']
        if 'tipo' in kwargs and kwargs['tipo'] is not None:
            atendimento.tipo = kwargs['tipo']

        if atendimento.horario_fim <= atendimento.horario_inicio:
            raise ValueError("Horário fim deve ser maior que horário de início")
        if atendimento.clinica.abertura and atendimento.clinica.fechamento:
            if atendimento.horario_inicio < atendimento.clinica.abertura or atendimento.horario_fim > atendimento.clinica.fechamento:
                raise ValueError("Horário do atendimento fora do horário de funcionamento da clínica")

        self.__atendimento_dao.update(atendimento)
        return True