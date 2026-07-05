from modelos.pagamento.pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago,
        numero,
        bandeira,
        parcelas=1
    ):

        super().__init__(
            data_pagamento,
            atendimento,
            paciente,
            valor_pago
        )

        self.numero = numero
        self.bandeira = bandeira
        self.parcelas = parcelas

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

    @property
    def parcelas(self):
        return self.__parcelas

    @parcelas.setter
    def parcelas(self, nova_parcela):
        if nova_parcela <= 0:
            raise ValueError("O número de parcelas deve ser maior que zero.")
        self.__parcelas = nova_parcela
