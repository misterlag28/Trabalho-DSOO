from abc import ABC, abstractmethod

class Pagamento(ABC):

    def __init__(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago
    ):

        self.data = data_pagamento
        self.atendimento = atendimento
        self.paciente = paciente
        self.valor_pago = valor_pago

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, novo_atendimento):
        self.__atendimento = novo_atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor):

        if novo_valor <= 0:
            raise ValueError(
                "O valor pago deve ser maior que zero."
            )

        self.__valor_pago = novo_valor

    def validar_data_pagamento(self):

        if self.data > self.atendimento.data:
            raise ValueError(
                "O pagamento não pode ser realizado após a data do atendimento."
            )

        return True

    @abstractmethod
    def validar_pagamento(self):
        pass

    def registrar_pagamento(self):

        self.validar_data_pagamento()
        self.validar_pagamento()

        return True
