from datetime import date
from modelos.pagamento.dinheiro import Dinheiro
from modelos.pagamento.pix import Pix
from modelos.pagamento.cartao_credito import CartaoCredito

class ControladorPagamento:
    def registrar_pagamento(self, pagamento):
        pagamento.registrar_pagamento()
        pagamento.atendimento.adicionar_pagamento(pagamento)



    def listar_pagamentos(self, atendimento):
        return atendimento.lista_pagamentos

    def escolher_pagamento_por_index(self, atendimento, index: int):
        if not atendimento.lista_pagamentos:
            return None
        if index < 0 or index >= len(atendimento.lista_pagamentos):
            return None
        return atendimento.lista_pagamentos[index]

    def alterar_pagamento(self, pagamento, *, data=None, valor_pago=None):
        if data is not None:
            pagamento.data = data
        if valor_pago is not None:
            pagamento.valor_pago = valor_pago
        pagamento.registrar_pagamento()

    def excluir_pagamento(self, atendimento, pagamento):
        if pagamento in atendimento.lista_pagamentos:
            atendimento.lista_pagamentos.remove(pagamento)
            return True
        return False
