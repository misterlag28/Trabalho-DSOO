from Pagamento import Pagamento
from datetime import date


class Dinheiro(Pagamento):

    def __init__(self, data: date, valor_pago: float):
        super().__init__(data, valor_pago)

    def tipo_pagamento(self):
        return "Dinheiro"