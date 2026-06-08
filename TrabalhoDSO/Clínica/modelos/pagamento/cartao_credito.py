from modelos.pagamento.pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago,
        numero,
        bandeira
    ):

        super().__init__(
            data_pagamento,
            atendimento,
            paciente,
            valor_pago
        )

        self.numero = numero
        self.bandeira = bandeira

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):

        if not novo_numero.strip():
            raise ValueError(
                "Número do cartão inválido."
            )

        self.__numero = novo_numero

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, nova_bandeira):

        if not nova_bandeira.strip():
            raise ValueError(
                "Bandeira inválida."
            )

        self.__bandeira = nova_bandeira

    def validar_pagamento(self):

        if len(self.numero) < 12:
            raise ValueError(
                "Número do cartão inválido."
            )

        return True
