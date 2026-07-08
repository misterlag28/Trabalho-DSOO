import FreeSimpleGUI as sg
from datetime import date
from modelos.pagamento.dinheiro import Dinheiro
from modelos.pagamento.pix import Pix
from modelos.pagamento.cartao_credito import CartaoCredito


class ViewPagamento:
    def __init__(self, controlador_pagamento):
        self.controlador = controlador_pagamento

    def abrir_menu(self, controlador_atendimento):
        while True:
            layout = [
                [sg.Text('PAGAMENTOS', font=("", 16))],
                [sg.Button('Registrar', key='1', size=(20, 1))],
                [sg.Button('Listar', key='2', size=(20, 1))],
                [sg.Button('Alterar', key='3', size=(20, 1))],
                [sg.Button('Excluir', key='4', size=(20, 1))],
                [sg.Button('Voltar', key='0', size=(20, 1))]
            ]
            window = sg.Window('Pagamentos', layout, element_justification='c')
            event, _ = window.read()
            window.close()

            if event in (sg.WINDOW_CLOSED, '0'):
                break

            opcao = event
            if opcao == "1":
                self.registrar(controlador_atendimento)
            elif opcao == "2":
                self.listar(controlador_atendimento)
            elif opcao == "3":
                self.alterar(controlador_atendimento)
            elif opcao == "4":
                self.excluir(controlador_atendimento)

    def _escolher_atendimento(self, controlador_atendimento, titulo='Selecione o atendimento:'):
        atendimentos = controlador_atendimento.listar_atendimentos()
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return None, None

        opcoes = [f"{i} - {a.exibir_dados()}" for i, a in enumerate(atendimentos)]

        layout = [
            [sg.Text(titulo)],
            [sg.Combo(opcoes, key='atendimento', readonly=True, size=(60, 1))],
            [sg.Button('Selecionar'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Escolher Atendimento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Selecionar' or not val['atendimento']:
            return None, None

        idx = int(val['atendimento'].split(' - ')[0])
        atendimento = controlador_atendimento.escolher_atendimento_por_index(idx)
        return atendimento, idx

    def registrar(self, controlador_atendimento):
        atendimento, _ = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        layout_dados = [
            [sg.Text('Registrar Pagamento')],
            [sg.Text('Data (DD/MM/YYYY):', size=(20, 1)), sg.Input(key='dia', size=(5, 1)), sg.Text('/'), sg.Input(key='mes', size=(5, 1)), sg.Text('/'), sg.Input(key='ano', size=(6, 1))],
            [sg.Text('Valor pago:', size=(20, 1)), sg.Input(key='valor_pago')],
            [sg.Text('Tipo de pagamento:', size=(20, 1)), sg.Combo(['Dinheiro', 'Pix', 'Cartão'], key='tipo', readonly=True, size=(20, 1))],
            [sg.Button('Continuar'), sg.Button('Cancelar')]
        ]
        win_dados = sg.Window('Registrar Pagamento', layout_dados)
        ev_dados, val_dados = win_dados.read()
        win_dados.close()

        if ev_dados != 'Continuar':
            return

        try:
            ano = int(val_dados['ano'])
            mes = int(val_dados['mes'])
            dia = int(val_dados['dia'])
            data_pagamento = date(ano, mes, dia)
            valor_pago = float(val_dados['valor_pago'])
            tipo = val_dados['tipo']

            if tipo == 'Dinheiro':
                layout_tipo = [
                    [sg.Text('Valor recebido pelo cliente (para calcular troco):', size=(40, 1)), sg.Input(key='valor_recebido')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                win_tipo = sg.Window('Pagamento em Dinheiro', layout_tipo)
                ev_tipo, val_tipo = win_tipo.read()
                win_tipo.close()
                if ev_tipo != 'Salvar':
                    return
                valor_recebido = float(val_tipo['valor_recebido'])
                pagamento = Dinheiro(data_pagamento, atendimento, atendimento.paciente, valor_pago, valor_recebido)

            elif tipo == 'Pix':
                layout_tipo = [
                    [sg.Text('CPF do pagante:', size=(20, 1)), sg.Input(key='cpf')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                win_tipo = sg.Window('Pagamento via Pix', layout_tipo)
                ev_tipo, val_tipo = win_tipo.read()
                win_tipo.close()
                if ev_tipo != 'Salvar':
                    return
                cpf = val_tipo['cpf']
                pagamento = Pix(data_pagamento, atendimento, atendimento.paciente, valor_pago, cpf)

            elif tipo == 'Cartão':
                layout_tipo = [
                    [sg.Text('Número do cartão:', size=(22, 1)), sg.Input(key='numero')],
                    [sg.Text('Bandeira:', size=(22, 1)), sg.Input(key='bandeira')],
                    [sg.Text('Quantidade de parcelas:', size=(22, 1)), sg.Input(key='parcelas')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                win_tipo = sg.Window('Pagamento com Cartão', layout_tipo)
                ev_tipo, val_tipo = win_tipo.read()
                win_tipo.close()
                if ev_tipo != 'Salvar':
                    return
                numero = val_tipo['numero']
                bandeira = val_tipo['bandeira']
                parcelas = int(val_tipo['parcelas'])
                pagamento = CartaoCredito(data_pagamento, atendimento, atendimento.paciente, valor_pago, numero, bandeira, parcelas)

            else:
                sg.popup_error("Selecione um tipo de pagamento.")
                return

            restante_antes = atendimento.calcular_valor_restante()
            self.controlador.registrar_pagamento(pagamento)

            mensagem = "Pagamento registrado com sucesso."
            if isinstance(pagamento, Dinheiro):
                if pagamento.troco > 0:
                    mensagem += f"\n\nTroco de R$ {pagamento.troco:.2f}"
                elif pagamento.valor_pago < restante_antes:
                    falta = restante_antes - pagamento.valor_pago
                    mensagem += f"\n\nFalta pagar R$ {falta:.2f}"
            else:
                if pagamento.valor_pago < restante_antes:
                    falta = restante_antes - pagamento.valor_pago
                    mensagem += f"\n\nFalta pagar R$ {falta:.2f}"

            sg.popup(mensagem)

        except ValueError as erro:
            sg.popup_error(f"Erro: {erro}")

    def listar(self, controlador_atendimento):
        atendimento, _ = self._escolher_atendimento(controlador_atendimento, 'Selecione o atendimento para listar pagamentos:')
        if atendimento is None:
            return

        pagamentos = self.controlador.listar_pagamentos(atendimento)
        if not pagamentos:
            sg.popup("Nenhum pagamento registrado.")
            return

        texto = ""
        for p in pagamentos:
            texto += f"Tipo: {p.__class__.__name__}\n"
            texto += f"Data: {p.data}\n"
            texto += f"Valor pago: R$ {p.valor_pago:.2f}\n"
            if hasattr(p, 'troco'):
                texto += f"Troco: R$ {p.troco:.2f}\n"
            texto += "\n"
        texto += f"Valor restante: R$ {atendimento.calcular_valor_restante():.2f}"
        sg.popup_scrolled(texto, title="Pagamentos", size=(60, 20))

    def alterar(self, controlador_atendimento):
        atendimento, _ = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        pagamentos = self.controlador.listar_pagamentos(atendimento)
        if not pagamentos:
            sg.popup("Nenhum pagamento registrado.")
            return

        opcoes = [f"{i} - {p.__class__.__name__} - R$ {p.valor_pago:.2f}" for i, p in enumerate(pagamentos)]

        layout = [
            [sg.Text('Selecione o pagamento:'), sg.Combo(opcoes, key='pagamento', readonly=True, size=(40, 1))],
            [sg.Text('Novo valor (deixe em branco para manter):', size=(35, 1)), sg.Input(key='novo_valor')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Alterar Pagamento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Salvar' or not val['pagamento']:
            return

        pidx = int(val['pagamento'].split(' - ')[0])
        pagamento = self.controlador.escolher_pagamento_por_index(atendimento, pidx)
        if pagamento is None:
            sg.popup_error("Pagamento inválido.")
            return

        try:
            novo_valor = val['novo_valor']
            novo_valor = float(novo_valor) if novo_valor else None
            self.controlador.alterar_pagamento(pagamento, valor_pago=novo_valor)
            sg.popup("Pagamento alterado com sucesso.")
        except ValueError as erro:
            sg.popup_error(f"Erro: {erro}")

    def excluir(self, controlador_atendimento):
        atendimento, _ = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        pagamentos = self.controlador.listar_pagamentos(atendimento)
        if not pagamentos:
            sg.popup("Nenhum pagamento registrado.")
            return

        opcoes = [f"{i} - {p.__class__.__name__} - R$ {p.valor_pago:.2f}" for i, p in enumerate(pagamentos)]

        layout = [
            [sg.Text('Selecione o pagamento para excluir:')],
            [sg.Combo(opcoes, key='pagamento', readonly=True, size=(40, 1))],
            [sg.Button('Excluir', button_color='red'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Excluir Pagamento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Excluir' or not val['pagamento']:
            return

        pidx = int(val['pagamento'].split(' - ')[0])
        pagamento = self.controlador.escolher_pagamento_por_index(atendimento, pidx)
        if pagamento is None:
            sg.popup_error("Pagamento inválido.")
            return

        self.controlador.excluir_pagamento(atendimento, pagamento)
        sg.popup("Pagamento removido com sucesso.")
