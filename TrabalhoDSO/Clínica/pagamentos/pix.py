from Pagamento import Pagamento
from datetime import date


class Pix(Pagamento):

    def __init__(
        self,
        data: date,
        valor_pago: float,
        cpf_pagador: str
    ):
        super().__init__(data, valor_pago)

        self.__cpf_pagador = cpf_pagador

    def tipo_pagamento(self):
        return "Pix"

    # GETTERS
    def get_cpf_pagador(self):
        return self.__cpf_pagador

    # SETTERS
    def set_cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador