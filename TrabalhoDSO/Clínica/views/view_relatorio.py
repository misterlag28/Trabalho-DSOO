import FreeSimpleGUI as sg


class ViewRelatorio:
    def __init__(self, controlador_relatorio):
        self.controlador = controlador_relatorio

    def abrir_menu(self, controlador_atendimento):
        while True:
            layout = [
                [sg.Text('RELATÓRIOS', font=("", 16))],
                [sg.Button('Clínicas com mais atendimentos', key='1', size=(35, 1))],
                [sg.Button('Atendimento mais caro e mais barato', key='2', size=(35, 1))],
                [sg.Button('Procedimentos mais realizados', key='3', size=(35, 1))],
                [sg.Button('Procedimento mais caro e mais barato', key='4', size=(35, 1))],
                [sg.Button('Voltar', key='0', size=(35, 1))]
            ]
            window = sg.Window('Relatórios', layout, element_justification='c')
            event, _ = window.read()
            window.close()

            if event in (sg.WINDOW_CLOSED, '0'):
                break

            opcao = event
            atendimentos = controlador_atendimento.listar_atendimentos()

            if opcao == "1":
                resultado = self.controlador.relatorio_clinicas(atendimentos)
                if not resultado:
                    sg.popup("Nenhum atendimento cadastrado.")
                else:
                    texto = ""
                    for nome, qtd in resultado.items():
                        texto += f"{nome} - {qtd} atendimento(s)\n"
                    sg.popup_scrolled(texto, title="Clínicas com mais atendimentos", size=(50, 15))

            elif opcao == "2":
                mais_caro, mais_barato = self.controlador.relatorio_atendimentos(atendimentos)
                if mais_caro is None:
                    sg.popup("Nenhum atendimento cadastrado.")
                else:
                    texto = "=== ATENDIMENTO MAIS CARO ===\n"
                    texto += mais_caro.exibir_dados() + "\n\n"
                    texto += "=== ATENDIMENTO MAIS BARATO ===\n"
                    texto += mais_barato.exibir_dados()
                    sg.popup_scrolled(texto, title="Atendimento mais caro e mais barato", size=(60, 20))

            elif opcao == "3":
                contagem = self.controlador.relatorio_procedimentos_realizados(atendimentos)
                if not contagem:
                    sg.popup("Nenhum procedimento registrado.")
                else:
                    maior = max(contagem.values())
                    texto = ""
                    for nome, qtd in contagem.items():
                        if qtd == maior:
                            texto += f"{nome} - {qtd} vez(es)\n"
                    sg.popup_scrolled(texto, title="Procedimentos mais realizados", size=(50, 15))

            elif opcao == "4":
                mais_caro, mais_barato = self.controlador.relatorio_procedimentos_valor(atendimentos)
                if mais_caro is None:
                    sg.popup("Nenhum procedimento registrado.")
                else:
                    texto = "=== PROCEDIMENTO MAIS CARO ===\n"
                    texto += mais_caro.exibir_dados() + "\n\n"
                    texto += "=== PROCEDIMENTO MAIS BARATO ===\n"
                    texto += mais_barato.exibir_dados()
                    sg.popup_scrolled(texto, title="Procedimento mais caro e mais barato", size=(60, 20))
