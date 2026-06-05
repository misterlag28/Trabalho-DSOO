from Pagamento import Pagamento

class Pix(Pagamento):

    def __init__(
        self,
        data,
        valor_pago,
        cpf_pagador: str
    ):

        super().__init__(data, valor_pago)

        if len(cpf_pagador) != 11:
            raise ValueError("CPF inválido.")

        self.__cpf_pagador = cpf_pagador

    # GETTER

    def get_cpf_pagador(self):
        return self.__cpf_pagador

    # SETTER

    def set_cpf_pagador(self, cpf_pagador: str):

        if len(cpf_pagador) != 11:
            raise ValueError("CPF inválido.")

        self.__cpf_pagador = cpf_pagador

    def tipo_pagamento(self):
        return "PIX"

    def validar(self):

        super().validar()

        if len(self.__cpf_pagador) != 11:
            raise ValueError("CPF inválido.")

        return True
