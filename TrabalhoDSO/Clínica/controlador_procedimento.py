from procedimento import Procedimento

class ControladorProcedimento:

    def registrar_procedimento(self, atendimento, procedimento):

        try:
            procedimento.validar_procedimento()

            atendimento.adicionar_procedimento(
                procedimento
            )

            print(
                "Procedimento registrado com sucesso."
            )

            return procedimento

        except ValueError as erro:
            print(f"Erro: {erro}")
            return None

    def cadastrar_procedimento(self, atendimento):

        try:

            nome = input(
                "Nome do procedimento: "
            )

            descricao = input(
                "Descrição: "
            )

            custo = float(
                input("Custo: ")
            )

            procedimento = Procedimento(
                nome,
                descricao,
                custo,
                atendimento.profissional
            )

            self.registrar_procedimento(
                atendimento,
                procedimento
            )

        except ValueError as erro:
            print(f"Erro: {erro}")

    def listar_procedimentos(self, atendimento):

        if not atendimento.lista_procedimentos:
            print(
                "Nenhum procedimento registrado."
            )
            return

        for procedimento in atendimento.lista_procedimentos:

            print("\n")
            print(
                procedimento.exibir_dados()
            )

    def escolher_procedimento(self, atendimento):

        if not atendimento.lista_procedimentos:

            print(
                "Nenhum procedimento registrado."
            )

            return None

        print(
            "\n=== ESCOLHER PROCEDIMENTO ==="
        )

        for i, procedimento in enumerate(
            atendimento.lista_procedimentos
        ):

            print(
                f"{i + 1} - "
                f"{procedimento.nome} - "
                f"R$ {procedimento.custo:.2f}"
            )

        try:

            opcao = int(
                input("Escolha: ")
            )

            if (
                opcao < 1
                or
                opcao > len(
                    atendimento.lista_procedimentos
                )
            ):

                print(
                    "Procedimento inválido."
                )

                return None

            return atendimento.lista_procedimentos[
                opcao - 1
            ]

        except ValueError:

            print(
                "Digite um número válido."
            )

            return None

    def alterar_procedimento(self, atendimento):

        procedimento = self.escolher_procedimento(
            atendimento
        )

        if procedimento is None:
            return

        while True:

            print(
                "\n=== ALTERAR PROCEDIMENTO ==="
            )
            print("1 - Nome")
            print("2 - Descrição")
            print("3 - Custo")
            print("0 - Voltar")

            opcao = input("Opção: ")

            try:

                if opcao == "1":

                    procedimento.nome = input(
                        "Novo nome: "
                    )

                    print(
                        "Nome alterado com sucesso."
                    )

                elif opcao == "2":

                    procedimento.descricao = input(
                        "Nova descrição: "
                    )

                    print(
                        "Descrição alterada com sucesso."
                    )

                elif opcao == "3":

                    procedimento.custo = float(
                        input("Novo custo: ")
                    )

                    procedimento.validar_procedimento()

                    print(
                        "Custo alterado com sucesso."
                    )

                elif opcao == "0":
                    break

                else:
                    print(
                        "Opção inválida."
                    )

            except ValueError as erro:
                print(f"Erro: {erro}")

    def excluir_procedimento(self, atendimento):

        procedimento = self.escolher_procedimento(
            atendimento
        )

        if procedimento is None:
            return

        confirmacao = input(
            "Confirma exclusão? (s/n): "
        )

        if confirmacao.lower() == "s":

            atendimento.lista_procedimentos.remove(
                procedimento
            )

            print(
                "Procedimento removido com sucesso."
            )

    def abrir_menu(self, controlador_atendimento):

        while True:

            print("\n=== PROCEDIMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.cadastrar_procedimento(
                        atendimento
                    )

            elif opcao == "2":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.listar_procedimentos(
                        atendimento
                    )

            elif opcao == "3":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.alterar_procedimento(
                        atendimento
                    )

            elif opcao == "4":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.excluir_procedimento(
                        atendimento
                    )

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")