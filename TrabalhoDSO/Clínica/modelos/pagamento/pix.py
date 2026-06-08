from modelos.pagamento.pagamento import Pagamento

class Pix(Pagamento):

    def __init__(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago,
        cpf_pagante
    ):

        super().__init__(
            data_pagamento,
            atendimento,
            paciente,
            valor_pago
        )

        self.cpf_pagante = cpf_pagante

    @property
    def cpf_pagante(self):
        return self.__cpf_pagante

    @cpf_pagante.setter
    def cpf_pagante(self, cpf):

        if not cpf.strip():
            raise ValueError(
                "CPF inválido."
            )

        self.__cpf_pagante = cpf

    def validar_pagamento(self):

        if len(self.cpf_pagante) != 11:
            raise ValueError(
                "CPF do pagante inválido."
            )

        return True
