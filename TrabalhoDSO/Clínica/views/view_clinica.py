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

    def exibir_menu(self):
        print("\n=== SISTEMA DA CLÍNICA ===")
        print("1 - Pacientes")
        print("2 - Profissionais")
        print("3 - Clínicas")
        print("4 - Tipos de Atendimento")
        print("5 - Atendimentos")
        print("6 - Pagamentos")
        print("7 - Procedimentos")
        print("8 - Relatórios")
        print("0 - Sair")

    def obter_opcao(self):
        opcao = input("Escolha uma opção: ")
        return opcao

    def validar_opcao(self, opcao):
        if opcao == "1":
            ViewPessoa(self.controlador_pessoa).abrir_menu_paciente()

        elif opcao == "2":
            ViewPessoa(self.controlador_pessoa).abrir_menu_profissional()

        elif opcao == "3":
            if self.controlador_clinica:
                self.abrir_menu_clinica()
            else:
                print("Menu de clínicas não disponível.")

        elif opcao == "4":
            print("Funcionalidade de tipos de atendimento.")

        elif opcao == "5":
            ViewAtendimento(self.controlador_atendimento, self.controlador_clinica, self.controlador_pessoa).abrir_menu()

        elif opcao == "6":
            ViewPagamento(self.controlador_pagamento).abrir_menu(self.controlador_atendimento)

        elif opcao == "7":
            ViewProcedimento(self.controlador_procedimento).abrir_menu(self.controlador_atendimento)

        elif opcao == "8":
            ViewRelatorio(self.controlador_relatorio).abrir_menu(self.controlador_atendimento)

        elif opcao == "0":
            print("Sistema encerrado.")

        else:
            print("Opção inválida.")

    def abrir_menu_clinica(self):
        while True:
            print("\n=== CLÍNICAS ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")
            opcao = input("Opção: ")
            if opcao == "1":
                try:
                    nome = input("Nome: ")
                    cidade = input("Cidade: ")
                    descricao = input("Descrição: ")
                    try:
                        abertura_h = int(input("Hora abertura: "))
                        abertura_m = int(input("Minuto abertura: "))
                        fechamento_h = int(input("Hora fechamento: "))
                        fechamento_m = int(input("Minuto fechamento: "))
                    except ValueError:
                        print("Erro: Horário deve ser número inteiro válido.")
                        continue
                    from datetime import time
                    from modelos.clinica import Clinica
                    abertura = time(abertura_h, abertura_m)
                    fechamento = time(fechamento_h, fechamento_m)
                    clinica = Clinica(nome, cidade, descricao, abertura, fechamento)
                    self.controlador_clinica.cadastrar_clinica(clinica)
                    print("Clínica cadastrada com sucesso!")
                except ValueError as erro:
                    print(f"Erro ao cadastrar clínica: {erro}")
            elif opcao == "2":
                clinicas = self.controlador_clinica.listar_clinicas()
                if not clinicas:
                    print("Nenhuma clínica cadastrada.")
                else:
                    for c in clinicas:
                        print("\n")
                        print(c.exibir_dados())
            elif opcao == "3":
                nome = input("Nome da clínica a alterar: ")
                novo_nome = input("Novo nome (enter para manter): ")
                nova_cidade = input("Nova cidade (enter para manter): ")
                nova_desc = input("Nova descrição (enter para manter): ")
                try:
                    abertura_h = input("Hora abertura (HH) (enter para manter): ")
                    if abertura_h:
                        abertura_m = int(input("Minuto abertura: "))
                        abertura = time(int(abertura_h), abertura_m)
                    else:
                        abertura = None
                    fechamento_h = input("Hora fechamento (HH) (enter para manter): ")
                    if fechamento_h:
                        fechamento_m = int(input("Minuto fechamento: "))
                        fechamento = time(int(fechamento_h), fechamento_m)
                    else:
                        fechamento = None
                except ValueError:
                    print("Horário inválido.")
                    continue
                success = self.controlador_clinica.alterar_clinica(
                    nome,
                    novo_nome if novo_nome else None,
                    nova_cidade if nova_cidade else None,
                    nova_desc if nova_desc else None,
                    abertura,
                    fechamento
                )
                if success:
                    print("Clínica alterada com sucesso!")
                else:
                    print("Clínica não encontrada.")
            elif opcao == "4":
                nome = input("Nome da clínica: ")
                removed = self.controlador_clinica.excluir_clinica(nome)
                if removed:
                    print("Clínica removida com sucesso.")
                else:
                    print("Clínica não encontrada.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")