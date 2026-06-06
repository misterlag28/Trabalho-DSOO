from datetime import date, time

from .clinica import Clinica
from .Pessoas.paciente import Paciente
from .Pessoas.profissional_saude import ProfissionalSaude
from .procedimento import Procedimento
from enums.tipo_atendimento import TipoAtendimento


class Atendimento:

    def __init__(
        self,
        data: date,
        horario_inicio: time,
        horario_fim: time,
        valor: float,
        profissional: ProfissionalSaude,
        paciente: Paciente,
        clinica: Clinica,
        tipo: TipoAtendimento
    ):
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor

        self.__profissional = profissional
        self.__paciente = paciente
        self.__clinica = clinica
        self.__tipo = tipo

        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__data = data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time):
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        self.__horario_fim = horario_fim

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    def calcular_valor_restante(self):
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.__valor - total_pago