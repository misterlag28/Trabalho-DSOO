from pagamento import Pagamento

class Dinheiro(Pagamento):

    def __init__(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago,
        valor_recebido
    ):

        super().__init__(
            data_pagamento,
            atendimento,
            paciente,
            valor_pago
        )

        self.valor_recebido = valor_recebido

    @property
    def valor_recebido(self):
        return self.__valor_recebido

    @valor_recebido.setter
    def valor_recebido(self, valor):

        if valor <= 0:
            raise ValueError(
                "Valor recebido inválido."
            )

        self.__valor_recebido = valor

    @property
    def troco(self):
        return self.calcular_troco()

    def calcular_troco(self):

        return (
            self.valor_recebido
            - self.valor_pago
        )

    def validar_pagamento(self):

        if self.valor_recebido < self.valor_pago:
            raise ValueError(
                "Valor recebido insuficiente."
            )

        return True
