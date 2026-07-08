import FreeSimpleGUI as sg
from modelos.atendimento.procedimento import Procedimento


class ViewProcedimento:
    def __init__(self, controlador_procedimento):
        self.controlador = controlador_procedimento

    def abrir_menu(self, controlador_atendimento):
        while True:
            layout = [
                [sg.Text('PROCEDIMENTOS', font=("", 16))],
                [sg.Button('Registrar', key='1', size=(20, 1))],
                [sg.Button('Listar', key='2', size=(20, 1))],
                [sg.Button('Alterar', key='3', size=(20, 1))],
                [sg.Button('Excluir', key='4', size=(20, 1))],
                [sg.Button('Voltar', key='0', size=(20, 1))]
            ]
            window = sg.Window('Procedimentos', layout, element_justification='c')
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
            return None

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
            return None

        idx = int(val['atendimento'].split(' - ')[0])
        return controlador_atendimento.escolher_atendimento_por_index(idx)

    def registrar(self, controlador_atendimento):
        atendimento = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        layout = [
            [sg.Text('Registrar Procedimento')],
            [sg.Text('Nome:', size=(15, 1)), sg.Input(key='nome')],
            [sg.Text('Descrição:', size=(15, 1)), sg.Input(key='descricao')],
            [sg.Text('Custo:', size=(15, 1)), sg.Input(key='custo')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Registrar Procedimento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Salvar':
            return

        try:
            nome = val['nome']
            descricao = val['descricao']
            custo = float(val['custo'])
            if custo <= 0:
                sg.popup_error("Erro: Custo deve ser positivo.")
                return

            procedimento = Procedimento(nome, descricao, custo, atendimento.profissional)
            self.controlador.registrar_procedimento(atendimento, procedimento)
            sg.popup("Procedimento registrado com sucesso.")
        except ValueError as erro:
            sg.popup_error(f"Erro: {erro}")

    def listar(self, controlador_atendimento):
        atendimento = self._escolher_atendimento(controlador_atendimento, 'Selecione o atendimento para listar procedimentos:')
        if atendimento is None:
            return

        procedimentos = self.controlador.listar_procedimentos(atendimento)
        if not procedimentos:
            sg.popup("Nenhum procedimento registrado.")
            return

        texto = ""
        for p in procedimentos:
            texto += p.exibir_dados() + "\n\n"
        sg.popup_scrolled(texto, title="Procedimentos", size=(60, 20))

    def alterar(self, controlador_atendimento):
        atendimento = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        procedimentos = self.controlador.listar_procedimentos(atendimento)
        if not procedimentos:
            sg.popup("Nenhum procedimento registrado.")
            return

        opcoes = [f"{i} - {p.nome} - R$ {p.custo:.2f}" for i, p in enumerate(procedimentos)]

        layout = [
            [sg.Text('Selecione o procedimento:'), sg.Combo(opcoes, key='procedimento', readonly=True, size=(40, 1))],
            [sg.Text('--- Deixe em branco os campos que não deseja alterar ---')],
            [sg.Text('Novo nome:', size=(15, 1)), sg.Input(key='novo_nome')],
            [sg.Text('Nova descrição:', size=(15, 1)), sg.Input(key='nova_desc')],
            [sg.Text('Novo custo:', size=(15, 1)), sg.Input(key='novo_custo')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Alterar Procedimento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Salvar' or not val['procedimento']:
            return

        pidx = int(val['procedimento'].split(' - ')[0])
        procedimento = self.controlador.escolher_procedimento_por_index(atendimento, pidx)
        if procedimento is None:
            sg.popup_error("Procedimento inválido.")
            return

        try:
            novo_nome = val['novo_nome']
            nova_desc = val['nova_desc']
            novo_custo = val['novo_custo']
            novo_custo = float(novo_custo) if novo_custo else None

            self.controlador.alterar_procedimento(
                atendimento,
                procedimento,
                nome=novo_nome if novo_nome else None,
                descricao=nova_desc if nova_desc else None,
                custo=novo_custo
            )
            sg.popup("Procedimento alterado com sucesso.")
        except ValueError as erro:
            sg.popup_error(f"Erro: {erro}")

    def excluir(self, controlador_atendimento):
        atendimento = self._escolher_atendimento(controlador_atendimento)
        if atendimento is None:
            return

        procedimentos = self.controlador.listar_procedimentos(atendimento)
        if not procedimentos:
            sg.popup("Nenhum procedimento registrado.")
            return

        opcoes = [f"{i} - {p.nome} - R$ {p.custo:.2f}" for i, p in enumerate(procedimentos)]

        layout = [
            [sg.Text('Selecione o procedimento para excluir:')],
            [sg.Combo(opcoes, key='procedimento', readonly=True, size=(40, 1))],
            [sg.Button('Excluir', button_color='red'), sg.Button('Cancelar')]
        ]
        win = sg.Window('Excluir Procedimento', layout)
        ev, val = win.read()
        win.close()

        if ev != 'Excluir' or not val['procedimento']:
            return

        pidx = int(val['procedimento'].split(' - ')[0])
        procedimento = self.controlador.escolher_procedimento_por_index(atendimento, pidx)
        if procedimento is None:
            sg.popup_error("Procedimento inválido.")
            return

        self.controlador.excluir_procedimento(atendimento, procedimento)
        sg.popup("Procedimento removido com sucesso.")
