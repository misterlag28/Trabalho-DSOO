from modelos.clinica import Clinica
from datetime import time

class ControladorClinica:

    def __init__(self):
        self.__clinicas = []

    @property
    def clinicas(self):
        return self.__clinicas

    def cadastrar_clinica(self):

        try:
            nome = input("Nome: ")
            cidade = input("Cidade: ")
            descricao = input("Descrição: ")

            abertura = time(
                int(input("Hora abertura: ")),
                int(input("Minuto abertura: "))
            )

            fechamento = time(
                int(input("Hora fechamento: ")),
                int(input("Minuto fechamento: "))
            )

            clinica = Clinica(
                nome,
                cidade,
                descricao,
                abertura,
                fechamento
            )

            clinica.validar_horarios()

            self.__clinicas.append(clinica)

            print("Clínica cadastrada com sucesso!")

        except ValueError as erro:
            print(f"Erro: {erro}")

    def listar_clinicas(self):

        if not self.__clinicas:
            print("Nenhuma clínica cadastrada.")
            return

        for clinica in self.__clinicas:
            print("\n")
            print(clinica.exibir_dados())

    def excluir_clinica(self):

        nome = input("Nome da clínica: ")

        for clinica in self.__clinicas:

            if clinica.nome == nome:
                self.__clinicas.remove(clinica)
                print("Clínica removida com sucesso.")
                return

        print("Clínica não encontrada.")

    def alterar_clinica(self):

        nome = input("Nome da clínica: ")

        for clinica in self.__clinicas:

            if clinica.nome == nome:

                try:
                    clinica.nome = input("Novo nome: ")
                    clinica.cidade = input("Nova cidade: ")
                    clinica.descricao = input("Nova descrição: ")

                    clinica.validar_horarios()

                    print("Clínica alterada com sucesso!")

                except ValueError as erro:
                    print(f"Erro: {erro}")

                return

        print("Clínica não encontrada.")

    def escolher_clinica(self):

        if len(self.__clinicas) == 0:
            print("Nenhuma clínica cadastrada.")
            return None

        print("\n=== ESCOLHER CLÍNICA ===")

        for i, clinica in enumerate(self.__clinicas):
            print(f"{i + 1} - {clinica.nome}")

        try:
            opcao = int(input("Escolha a clínica: "))

            if opcao < 1 or opcao > len(self.__clinicas):
                print("Opção inválida.")
                return None

            return self.__clinicas[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def abrir_menu(self):

        while True:

            print("\n=== CLÍNICAS ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_clinica()

            elif opcao == "2":
                self.listar_clinicas()

            elif opcao == "3":
                self.alterar_clinica()

            elif opcao == "4":
                self.excluir_clinica()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")
