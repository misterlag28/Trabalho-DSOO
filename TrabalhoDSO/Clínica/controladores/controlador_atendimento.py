from datetime import time
from modelos.atendimento.atendimento import Atendimento


class ControladorAtendimento:
    def __init__(self, atendimentos=None):
        self.atendimentos: list[Atendimento] = atendimentos if atendimentos is not None else []

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
        
        self.atendimentos.append(atendimento)

    def listar_atendimentos(self):
        return self.atendimentos

    def escolher_atendimento_por_index(self, index: int):
        if index < 0 or index >= len(self.atendimentos):
            return None
        return self.atendimentos[index]

    def excluir_atendimento(self, atendimento: Atendimento) -> bool:
        if atendimento in self.atendimentos:
            self.atendimentos.remove(atendimento)
            return True
        return False