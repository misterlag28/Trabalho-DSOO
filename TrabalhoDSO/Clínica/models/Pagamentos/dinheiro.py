from models.pagamento import Pagamento


class Dinheiro(Pagamento):

    def __init__(
        self,
        data,
        valor_pago: float,
        valor_recebido: float
    ):

        super().__init__(data, valor_pago)

        if valor_recebido < valor_pago:
            raise ValueError(
                "Valor recebido menor que o valor do pagamento."
            )

        self.__valor_recebido = valor_recebido

    # GETTER

    def get_valor_recebido(self):
        return self.__valor_recebido

    # SETTER

    def set_valor_recebido(self, valor_recebido):

        if valor_recebido < self.get_valor_pago():
            raise ValueError(
                "Valor recebido insuficiente."
            )

        self.__valor_recebido = valor_recebido

    def calcular_troco(self):

        return (
            self.__valor_recebido
            - self.get_valor_pago()
        )

    def tipo_pagamento(self):
        return "Dinheiro"
