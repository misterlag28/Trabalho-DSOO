from abc import ABC, abstractmethod
from datetime import date


class Pagamento(ABC):

    def __init__(self, data: date, valor_pago: float):
        self.__data = data
        self.__valor_pago = valor_pago

        # RELAÇÕES
        self.atendimento = None
        self.paciente = None

    @abstractmethod
    def tipo_pagamento(self):
        pass

    # GETTERS
    def get_data(self):
        return self.__data

    def get_valor_pago(self):
        return self.__valor_pago

    # SETTERS
    def set_data(self, data: date):
        self.__data = data

    def set_valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago