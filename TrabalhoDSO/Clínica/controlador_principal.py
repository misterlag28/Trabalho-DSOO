from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorTipoAtendimento import ControladorTipoAtendimento
from controladorAtendimento import ControladorAtendimento
from controladorPagamento import ControladorPagamento
from controladorProcedimento import ControladorProcedimento
from controladorRelatorio import ControladorRelatorio

class ControladorPrincipal:

    def __init__(self):

        self.__controladorPaciente = ControladorPaciente()
        self.__controladorProfissional = ControladorProfissional()
        self.__controladorClinica = ControladorClinica()
        self.__controladorTipoAtendimento = ControladorTipoAtendimento()
        self.__controladorAtendimento = ControladorAtendimento()
        self.__controladorPagamento = ControladorPagamento()
        self.__controladorProcedimento = ControladorProcedimento()
        self.__controladorRelatorio = ControladorRelatorio()

    def iniciar(self):

        while True:

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

            opcao = input("Escolha uma opção: ")

            if opcao == "1":

                self.__controladorPaciente.abrir_menu()

            elif opcao == "2":

                self.__controladorProfissional.abrir_menu()

            elif opcao == "3":

                self.__controladorClinica.abrir_menu()

            elif opcao == "4":

                self.__controladorTipoAtendimento.abrir_menu()

            elif opcao == "5":

                self.__controladorAtendimento.abrir_menu(
                    self.__controladorClinica,
                    self.__controladorPaciente,
                    self.__controladorProfissional,
                    self.__controladorTipoAtendimento
                )

            elif opcao == "6":

                self.__controladorPagamento.abrir_menu(
                    self.__controladorAtendimento
                )

            elif opcao == "7":

                self.__controladorProcedimento.abrir_menu(
                    self.__controladorAtendimento
                )

            elif opcao == "8":

                self.__controladorRelatorio.abrir_menu(
                    self.__controladorAtendimento
                )

            elif opcao == "0":

                print("Sistema encerrado.")
                break

            else:

                print("Opção inválida.")