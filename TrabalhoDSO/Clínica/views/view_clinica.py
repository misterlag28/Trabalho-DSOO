import FreeSimpleGUI as sg
from views.view_pagamento import ViewPagamento
from views.view_procedimento import ViewProcedimento
from views.view_relatorio import ViewRelatorio
from views.view_pessoa import ViewPessoa
from views.view_atendimento import ViewAtendimento


class ViewClinica:
    def __init__(self, controlador_pessoa=None, controlador_clinica=None, controlador_atendimento=None, controlador_pagamento=None, controlador_procedimento=None, controlador_relatorio=None):
        self.controlador_pessoa = controlador_pessoa
        self.controlador_clinica = controlador_clinica
        self.controlador_atendimento = controlador_atendimento
        self.controlador_pagamento = controlador_pagamento
        self.controlador_procedimento = controlador_procedimento
        self.controlador_relatorio = controlador_relatorio
        self.window = None

    def exibir_menu(self):
        layout = [
            [sg.Text('SISTEMA DA CLÍNICA', font=("", 16), justification='center')],
            [sg.Button('Pacientes', key='1', size=(30, 1))],
            [sg.Button('Profissionais', key='2', size=(30, 1))],
            [sg.Button('Clínicas', key='3', size=(30, 1))],
            [sg.Button('Tipos de Atendimento', key='4', size=(30, 1))],
            [sg.Button('Atendimentos', key='5', size=(30, 1))],
            #pagamentos
            [sg.Button('Pagamentos', key='6', size=(30, 1))],
            #procedimentos
            [sg.Button('Procedimentos', key='7', size=(30, 1))],
            [sg.Button('Relatórios', key='8', size=(30, 1))],
            [sg.Button('Limpar Dados da Persistência', key='9', size=(30, 1))],
            [sg.Button('Sair', key='0', size=(30, 1), button_color='red')]
        ]
        self.window = sg.Window('Sistema da Clínica', layout, element_justification='c')

    def obter_opcao(self):
        event, values = self.window.read()
        self.window.close()
        if event == sg.WINDOW_CLOSED:
            return "0"
        return event

    def validar_opcao(self, opcao):
        if opcao == "1":
            ViewPessoa(self.controlador_pessoa).abrir_menu_paciente()

        elif opcao == "2":
            ViewPessoa(self.controlador_pessoa).abrir_menu_profissional()

        elif opcao == "3":
            if self.controlador_clinica:
                self.abrir_menu_clinica()
            else:
                sg.popup_error("Menu de clínicas não disponível.")

        elif opcao == "4":
            sg.popup("Tipos de atendimento disponíveis:\nConsulta\nExame\nProcedimento", title="Tipos de Atendimento")

        elif opcao == "5":
            ViewAtendimento(self.controlador_atendimento, self.controlador_clinica, self.controlador_pessoa).abrir_menu()

        elif opcao == "6":
            # chamada da tela de pagamento vai aqui
            ViewPagamento(self.controlador_pagamento).abrir_menu(self.controlador_atendimento)

        elif opcao == "7":
            # chamada da tela de procedimento vai aqui
            ViewProcedimento(self.controlador_procedimento).abrir_menu(self.controlador_atendimento)

        elif opcao == "8":
            ViewRelatorio(self.controlador_relatorio).abrir_menu(self.controlador_atendimento)

        elif opcao == "9":
            if self.controlador_pessoa:
                self.controlador_pessoa.limpar_dados()
            if self.controlador_clinica:
                self.controlador_clinica.limpar_dados()
            if self.controlador_atendimento:
                self.controlador_atendimento.limpar_dados()
            sg.popup("Dados da persistência foram limpos com sucesso!")

        elif opcao == "0":
            pass

        else:
            sg.popup_error("Opção inválida.")

    def abrir_menu_clinica(self):
        while True:
            layout = [
                [sg.Text('CLÍNICAS', font=("", 16))],
                [sg.Button('Cadastrar', key='1', size=(20, 1))],
                [sg.Button('Listar', key='2', size=(20, 1))],
                [sg.Button('Alterar', key='3', size=(20, 1))],
                [sg.Button('Excluir', key='4', size=(20, 1))],
                [sg.Button('Voltar', key='0', size=(20, 1))]
            ]
            window = sg.Window('Menu de Clínicas', layout, element_justification='c')
            event, values = window.read()
            window.close()
            
            if event in (sg.WINDOW_CLOSED, '0'):
                break
            
            opcao = event
            if opcao == "1":
                layout_cadastro = [
                    [sg.Text('Cadastrar Clínica')],
                    [sg.Text('Nome:', size=(22, 1)), sg.Input(key='nome')],
                    [sg.Text('Cidade:', size=(22, 1)), sg.Input(key='cidade')],
                    [sg.Text('Descrição:', size=(22, 1)), sg.Input(key='descricao')],
                    [sg.Text('Hora abertura (HH):', size=(22, 1)), sg.Input(key='abertura_h')],
                    [sg.Text('Minuto abertura (MM):', size=(22, 1)), sg.Input(key='abertura_m')],
                    [sg.Text('Hora fechamento (HH):', size=(22, 1)), sg.Input(key='fechamento_h')],
                    [sg.Text('Minuto fechamento (MM):', size=(22, 1)), sg.Input(key='fechamento_m')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                win_cad = sg.Window('Cadastro', layout_cadastro)
                ev_cad, val_cad = win_cad.read()
                win_cad.close()
                if ev_cad == 'Salvar':
                    try:
                        nome = val_cad['nome']
                        cidade = val_cad['cidade']
                        descricao = val_cad['descricao']
                        abertura_h = int(val_cad['abertura_h'])
                        abertura_m = int(val_cad['abertura_m'])
                        fechamento_h = int(val_cad['fechamento_h'])
                        fechamento_m = int(val_cad['fechamento_m'])
                        from datetime import time
                        from modelos.clinica import Clinica
                        abertura = time(abertura_h, abertura_m)
                        fechamento = time(fechamento_h, fechamento_m)
                        clinica = Clinica(nome, cidade, descricao, abertura, fechamento)
                        self.controlador_clinica.cadastrar_clinica(clinica)
                        sg.popup("Clínica cadastrada com sucesso!")
                    except ValueError as erro:
                        sg.popup_error(f"Erro ao cadastrar clínica: {erro}\n(Verifique se os horários são números inteiros válidos)")
            
            elif opcao == "2":
                clinicas = self.controlador_clinica.listar_clinicas()
                if not clinicas:
                    sg.popup("Nenhuma clínica cadastrada.")
                else:
                    texto = ""
                    for c in clinicas:
                        texto += c.exibir_dados() + "\n\n"
                    sg.popup_scrolled(texto, title="Lista de Clínicas", size=(50, 15))
            
            elif opcao == "3":
                layout_alt = [
                    [sg.Text('Alterar Clínica')],
                    [sg.Text('Nome da clínica a alterar:', size=(40, 1)), sg.Input(key='nome')],
                    [sg.Text('Novo nome (vazio p/ manter):', size=(40, 1)), sg.Input(key='novo_nome')],
                    [sg.Text('Nova cidade (vazio p/ manter):', size=(40, 1)), sg.Input(key='nova_cidade')],
                    [sg.Text('Nova descrição (vazio p/ manter):', size=(40, 1)), sg.Input(key='nova_desc')],
                    [sg.Text('Nova Hora abertura (HH) (vazio p/ manter):', size=(40, 1)), sg.Input(key='abertura_h')],
                    [sg.Text('Novo Minuto abertura (MM):', size=(40, 1)), sg.Input(key='abertura_m')],
                    [sg.Text('Nova Hora fechamento (HH) (vazio p/ manter):', size=(40, 1)), sg.Input(key='fechamento_h')],
                    [sg.Text('Novo Minuto fechamento (MM):', size=(40, 1)), sg.Input(key='fechamento_m')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                win_alt = sg.Window('Alterar', layout_alt)
                ev_alt, val_alt = win_alt.read()
                win_alt.close()
                if ev_alt == 'Salvar':
                    try:
                        nome = val_alt['nome']
                        novo_nome = val_alt['novo_nome']
                        nova_cidade = val_alt['nova_cidade']
                        nova_desc = val_alt['nova_desc']
                        
                        abertura_h = val_alt['abertura_h']
                        if abertura_h:
                            abertura_m = int(val_alt['abertura_m'])
                            from datetime import time
                            abertura = time(int(abertura_h), abertura_m)
                        else:
                            abertura = None
                            
                        fechamento_h = val_alt['fechamento_h']
                        if fechamento_h:
                            fechamento_m = int(val_alt['fechamento_m'])
                            from datetime import time
                            fechamento = time(int(fechamento_h), fechamento_m)
                        else:
                            fechamento = None
                            
                        success = self.controlador_clinica.alterar_clinica(
                            nome,
                            novo_nome if novo_nome else None,
                            nova_cidade if nova_cidade else None,
                            nova_desc if nova_desc else None,
                            abertura,
                            fechamento
                        )
                        if success:
                            sg.popup("Clínica alterada com sucesso!")
                        else:
                            sg.popup_error("Clínica não encontrada.")
                    except ValueError:
                        sg.popup_error("Horário inválido.")
            
            elif opcao == "4":
                nome = sg.popup_get_text("Nome da clínica:")
                if nome:
                    removed = self.controlador_clinica.excluir_clinica(nome)
                    if removed:
                        sg.popup("Clínica removida com sucesso.")
                    else:
                        sg.popup_error("Clínica não encontrada.")