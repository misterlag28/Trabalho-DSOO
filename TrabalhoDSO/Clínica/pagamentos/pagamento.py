from abc import ABC, abstractmethod
from datetime import date


class Pagamento(ABC):

    def __init__(self, data: date, valor_pago: float):

        if valor_pago <= 0:
            raise ValueError("Valor pago deve ser maior que zero.")

        self.__data = data
        self.__valor_pago = valor_pago

        self.atendimento = None
        self.paciente = None

    # GETTERS

    def get_data(self):
        return self.__data

    def get_valor_pago(self):
        return self.__valor_pago

    # SETTERS

    def set_data(self, data: date):
        self.__data = data

    def set_valor_pago(self, valor_pago: float):

        if valor_pago <= 0:
            raise ValueError("Valor inválido.")

        self.__valor_pago = valor_pago

    @abstractmethod
    def tipo_pagamento(self):
        pass

    def calcular_valor_restante(self):

        if self.atendimento is None:
            raise ValueError("Pagamento sem atendimento associado.")

        return self.atendimento.get_valor() - self.__valor_pago

    def validar(self):

        if self.__valor_pago <= 0:
            raise ValueError("Valor inválido.")

        return True
