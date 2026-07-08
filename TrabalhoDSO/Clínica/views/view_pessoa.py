import FreeSimpleGUI as sg
from controladores.controlador_pessoa import ControladorPessoa
from modelos.pessoa.paciente import Paciente
from modelos.pessoa.profissional_saude import ProfissionalSaude


class ViewPessoa:
    def __init__(self, controlador_pessoa: ControladorPessoa):
        self.controlador = controlador_pessoa

    def abrir_menu_paciente(self):
        layout = [
            [sg.Text('MENU PACIENTE', font=("", 16))],
            [sg.Button('Cadastrar Paciente', key='1', size=(20, 1))],
            [sg.Button('Listar Pacientes', key='2', size=(20, 1))],
            [sg.Button('Editar Paciente', key='3', size=(20, 1))],
            [sg.Button('Excluir Paciente', key='4', size=(20, 1))],
            [sg.Button('Voltar', key='0', size=(20, 1))]
        ]
        window = sg.Window('Pacientes', layout, element_justification='c')
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, '0'):
            return

        resposta = event
        if resposta == "1":
            layout_cad = [
                [sg.Text('Nome:', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Idade:', size=(10, 1)), sg.Input(key='idade')],
                [sg.Text('CPF:', size=(10, 1)), sg.Input(key='cpf')],
                [sg.Text('Telefone:', size=(10, 1)), sg.Input(key='celular')],
                [sg.Button('Salvar'), sg.Button('Cancelar')]
            ]
            win_cad = sg.Window('Cadastrar Paciente', layout_cad)
            ev_cad, val_cad = win_cad.read()
            win_cad.close()
            if ev_cad == 'Salvar':
                try:
                    nome = val_cad['nome']
                    idade = int(val_cad['idade'])
                    cpf = val_cad['cpf']
                    celular = val_cad['celular']
                    novoPaciente = Paciente(nome=nome, idade=idade, cpf=cpf, celular=celular)
                    self.controlador.cadastrar_paciente(novoPaciente)
                    sg.popup("Paciente cadastrado com sucesso.")
                except ValueError as erro:
                    if "invalid literal for int" in str(erro):
                        sg.popup_error("Erro: Idade deve ser um número inteiro válido.")
                    else:
                        sg.popup_error(f"Erro ao cadastrar paciente: {erro}")
        elif resposta == "2":
            pacientes = self.controlador.listar_pacientes()
            if not pacientes:
                sg.popup("Nenhum paciente cadastrado.")
            else:
                texto = ""
                for i, p in enumerate(pacientes):
                    texto += f"{i}: {p.nome}\n     {p.idade} anos, {p.cpf}, {p.celular}\n\n"
                sg.popup_scrolled(texto, title="Pacientes", size=(40, 15))
        elif resposta == "3":
            layout_edit = [
                [sg.Text('Nome do paciente a editar:', size=(26, 1)), sg.Input(key='nome_antigo')],
                [sg.Text('Novo nome:', size=(26, 1)), sg.Input(key='nome')],
                [sg.Text('Nova idade:', size=(26, 1)), sg.Input(key='idade')],
                [sg.Text('Novo CPF:', size=(26, 1)), sg.Input(key='cpf')],
                [sg.Text('Novo telefone:', size=(26, 1)), sg.Input(key='celular')],
                [sg.Button('Salvar'), sg.Button('Cancelar')]
            ]
            win_edit = sg.Window('Editar Paciente', layout_edit)
            ev_edit, val_edit = win_edit.read()
            win_edit.close()
            if ev_edit == 'Salvar':
                try:
                    nome_antigo = val_edit['nome_antigo']
                    nome = val_edit['nome']
                    idade = int(val_edit['idade'])
                    cpf = val_edit['cpf']
                    celular = val_edit['celular']
                    
                    novoPaciente = Paciente(nome=nome, idade=idade, cpf=cpf, celular=celular)
                    alterado = self.controlador.editar_paciente(nome_antigo, novoPaciente)
                    if alterado:
                        sg.popup("Paciente alterado com sucesso.")
                    else:
                        sg.popup_error("Paciente não encontrado.")
                except ValueError as erro:
                    if "invalid literal for int" in str(erro):
                        sg.popup_error("Erro: Idade deve ser um número inteiro válido.")
                    else:
                        sg.popup_error(f"Erro ao editar paciente: {erro}")

        elif resposta == "4":
            nome = sg.popup_get_text("Digite o nome do paciente para ser excluído:")
            if nome:
                removido = self.controlador.remover_paciente(nome)
                if removido:
                    sg.popup("Paciente removido com sucesso.")
                else:
                    sg.popup_error("Paciente não encontrado.")


    def abrir_menu_profissional(self):
        layout = [
            [sg.Text('MENU PROFISSIONAL', font=("", 16))],
            [sg.Button('Cadastrar Profissional', key='1', size=(25, 1))],
            [sg.Button('Listar Profissionais', key='2', size=(25, 1))],
            [sg.Button('Editar Profissional', key='3', size=(25, 1))],
            [sg.Button('Excluir Profissional', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(25, 1))]
        ]
        window = sg.Window('Profissionais', layout, element_justification='c')
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, '0'):
            return

        resposta = event
        if resposta == "1":
            layout_cad = [
                [sg.Text('Nome:', size=(22, 1)), sg.Input(key='nome')],
                [sg.Text('Telefone:', size=(22, 1)), sg.Input(key='celular')],
                [sg.Text('CPF:', size=(22, 1)), sg.Input(key='cpf')],
                [sg.Text('Especialidade:', size=(22, 1)), sg.Input(key='especialidade')],
                [sg.Text('Registro Profissional:', size=(22, 1)), sg.Input(key='registro')],
                [sg.Button('Salvar'), sg.Button('Cancelar')]
            ]
            win_cad = sg.Window('Cadastrar Profissional', layout_cad)
            ev_cad, val_cad = win_cad.read()
            win_cad.close()
            if ev_cad == 'Salvar':
                try:
                    nome = val_cad['nome']
                    celular = val_cad['celular']
                    cpf = val_cad['cpf']
                    especialidade = val_cad['especialidade']
                    registro = val_cad['registro']
                    
                    novoProfissional = ProfissionalSaude(nome=nome, celular=celular, cpf=cpf, 
                                                          especialidade=especialidade, 
                                                          registro_profissional=registro)
                    self.controlador.cadastrar_profissional(novoProfissional)
                    sg.popup("Profissional cadastrado com sucesso.")
                except ValueError as erro:
                    sg.popup_error(f"Erro ao cadastrar profissional: {erro}")
        elif resposta == "2":
            profissionais = self.controlador.listar_profissionais()
            if not profissionais:
                sg.popup("Nenhum profissional cadastrado.")
            else:
                texto = ""
                for i, pr in enumerate(profissionais):
                    texto += f"{i}: {pr.nome}\n     {pr.especialidade}, {pr.cpf}, {pr.celular}\n\n"
                sg.popup_scrolled(texto, title="Profissionais", size=(40, 15))
        elif resposta == "3":
            layout_edit = [
                [sg.Text('Nome do profissional a editar:', size=(30, 1)), sg.Input(key='nome_antigo')],
                [sg.Text('Novo nome:', size=(30, 1)), sg.Input(key='nome')],
                [sg.Text('Novo telefone:', size=(30, 1)), sg.Input(key='celular')],
                [sg.Text('Novo CPF:', size=(30, 1)), sg.Input(key='cpf')],
                [sg.Text('Nova especialidade:', size=(30, 1)), sg.Input(key='especialidade')],
                [sg.Text('Novo Registro:', size=(30, 1)), sg.Input(key='registro')],
                [sg.Button('Salvar'), sg.Button('Cancelar')]
            ]
            win_edit = sg.Window('Editar Profissional', layout_edit)
            ev_edit, val_edit = win_edit.read()
            win_edit.close()
            if ev_edit == 'Salvar':
                try:
                    nome_antigo = val_edit['nome_antigo']
                    nome = val_edit['nome']
                    celular = val_edit['celular']
                    cpf = val_edit['cpf']
                    especialidade = val_edit['especialidade']
                    registro = val_edit['registro']
                    
                    novoProfissional = ProfissionalSaude(nome=nome, celular=celular, cpf=cpf,
                                                          especialidade=especialidade,
                                                          registro_profissional=registro)
                    alterado = self.controlador.editar_profissional(nome_antigo, novoProfissional)
                    if alterado:
                        sg.popup("Profissional alterado com sucesso.")
                    else:
                        sg.popup_error("Profissional não encontrado.")
                except ValueError as erro:
                    sg.popup_error(f"Erro ao editar profissional: {erro}")
        elif resposta == "4":
            nome = sg.popup_get_text("Digite o nome do profissional para ser excluído:")
            if nome:
                removido = self.controlador.remover_profissional(nome)
                if removido:
                    sg.popup("Profissional removido com sucesso.")
                else:
                    sg.popup_error("Profissional não encontrado.")

