from datetime import date, time

from modelos.clinica import Clinica
from modelos.pessoa.paciente import Paciente
from modelos.pessoa.profissional_saude import ProfissionalSaude
from modelos.atendimento.procedimento import Procedimento
from modelos.enum.tipo_atendimento import TipoAtendimento


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
    def lista_procedimentos(self):
        return self.__procedimentos

    @property
    def lista_pagamentos(self):
        return self.__pagamentos

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def calcular_valor_total(self):
        total = self.__valor + sum(p.custo for p in self.__procedimentos)
        return total

    def exibir_dados(self):
        return (
            f"Data: {self.data}\n"
            f"Horário: {self.horario_inicio.strftime('%H:%M')} - {self.horario_fim.strftime('%H:%M')}\n"
            f"Valor base: R$ {self.valor:.2f}\n"
            f"Paciente: {self.__paciente.nome}\n"
            f"Profissional: {self.__profissional.nome}\n"
            f"Clínica: {self.__clinica.nome}"
        )

    @property
    def paciente(self):
        return self.__paciente

    @property
    def profissional(self):
        return self.__profissional

    @property
    def clinica(self):
        return self.__clinica

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