from models.pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(
        self,
        data,
        valor_pago,
        numero_cartao: str,
        bandeira: str
    ):

        super().__init__(data, valor_pago)

        if numero_cartao.strip() == "":
            raise ValueError("Número do cartão inválido.")

        if bandeira.strip() == "":
            raise ValueError("Bandeira inválida.")

        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    # GETTERS

    def get_numero_cartao(self):
        return self.__numero_cartao

    def get_bandeira(self):
        return self.__bandeira

    # SETTERS

    def set_numero_cartao(self, numero_cartao: str):

        if numero_cartao.strip() == "":
            raise ValueError("Número inválido.")

        self.__numero_cartao = numero_cartao

    def set_bandeira(self, bandeira: str):

        if bandeira.strip() == "":
            raise ValueError("Bandeira inválida.")

        self.__bandeira = bandeira

    def tipo_pagamento(self):
        return "Cartão de Crédito"

    def validar(self):

        super().validar()

        if self.__numero_cartao.strip() == "":
            raise ValueError("Número inválido.")

        if self.__bandeira.strip() == "":
            raise ValueError("Bandeira inválida.")

        return True
