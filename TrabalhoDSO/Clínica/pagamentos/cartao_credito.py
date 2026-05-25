from Pagamento import Pagamento
from datetime import date


class CartaoCredito(Pagamento):

    def __init__(
        self,
        data: date,
        valor_pago: float,
        numero_cartao: str,
        bandeira: str
    ):
        super().__init__(data, valor_pago)

        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    def tipo_pagamento(self):
        return "Cartão de Crédito"

    # GETTERS
    def get_numero_cartao(self):
        return self.__numero_cartao

    def get_bandeira(self):
        return self.__bandeira

    # SETTERS
    def set_numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao

    def set_bandeira(self, bandeira: str):
        self.__bandeira = bandeira