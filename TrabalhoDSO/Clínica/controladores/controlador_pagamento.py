from datetime import date
from modelos.pagamento.dinheiro import Dinheiro
from modelos.pagamento.pix import Pix
from modelos.pagamento.cartao_credito import CartaoCredito
from daos.atendimento_dao import AtendimentoDAO

class ControladorPagamento:
    def __init__(self):
        self.__atendimento_dao = AtendimentoDAO()

    def registrar_pagamento(self, pagamento):
        restante = pagamento.atendimento.calcular_valor_restante()
        
        if isinstance(pagamento, Dinheiro):
            if pagamento.valor_recebido >= restante:
                pagamento.valor_pago = restante
                troco = pagamento.valor_recebido - restante
            else:
                pagamento.valor_pago = pagamento.valor_recebido
                falta = restante - pagamento.valor_pago
        else:
            if pagamento.valor_pago > restante:
                raise ValueError("Não é permitido pagar um valor maior que o restante usando este método de pagamento.")
            elif pagamento.valor_pago < restante:
                falta = restante - pagamento.valor_pago

        pagamento.registrar_pagamento()
        pagamento.atendimento.adicionar_pagamento(pagamento)
        self.__atendimento_dao.update(pagamento.atendimento)

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
        self.__atendimento_dao.update(pagamento.atendimento)

    def excluir_pagamento(self, atendimento, pagamento):
        if pagamento in atendimento.lista_pagamentos:
            atendimento.lista_pagamentos.remove(pagamento)
            self.__atendimento_dao.update(atendimento)
            return True
        return False
