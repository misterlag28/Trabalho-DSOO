from datetime import date
from dinheiro import Dinheiro
from pix import Pix
from cartaoCredito import CartaoCredito

class ControladorPagamento:

    def registrar_pagamento(self, pagamento):

        try:

            pagamento.registrar_pagamento()

            pagamento.atendimento.adicionar_pagamento(
                pagamento
            )

            print(
                "Pagamento registrado com sucesso."
            )

        except ValueError as erro:
            print(f"Erro: {erro}")

    def cadastrar_pagamento(self, atendimento):

        try:

            data_pagamento = date(
                int(input("Ano: ")),
                int(input("Mês: ")),
                int(input("Dia: "))
            )

            valor_pago = float(
                input("Valor pago: ")
            )

            print("\n1 - Dinheiro")
            print("2 - Pix")
            print("3 - Cartão")

            opcao = input("Opção: ")

            if opcao == "1":

                valor_recebido = float(
                    input("Valor recebido: ")
                )

                pagamento = Dinheiro(
                    data_pagamento,
                    atendimento,
                    atendimento.paciente,
                    valor_pago,
                    valor_recebido
                )

            elif opcao == "2":

                cpf_pagante = input(
                    "CPF do pagante: "
                )

                pagamento = Pix(
                    data_pagamento,
                    atendimento,
                    atendimento.paciente,
                    valor_pago,
                    cpf_pagante
                )

            elif opcao == "3":

                numero = input(
                    "Número do cartão: "
                )

                bandeira = input(
                    "Bandeira: "
                )

                pagamento = CartaoCredito(
                    data_pagamento,
                    atendimento,
                    atendimento.paciente,
                    valor_pago,
                    numero,
                    bandeira
                )

            else:

                print("Opção inválida.")
                return

            self.registrar_pagamento(
                pagamento
            )

        except ValueError as erro:
            print(f"Erro: {erro}")

    def listar_pagamentos(self, atendimento):

        if not atendimento.lista_pagamentos:

            print(
                "Nenhum pagamento registrado."
            )

            return

        for pagamento in atendimento.lista_pagamentos:

            print("\n")
            print(
                f"Tipo: {pagamento.__class__.__name__}"
            )

            print(
                f"Data: {pagamento.data}"
            )

            print(
                f"Valor pago: R$ {pagamento.valor_pago:.2f}"
            )

            if isinstance(
                pagamento,
                Dinheiro
            ):

                print(
                    f"Troco: R$ {pagamento.troco:.2f}"
                )

        print(
            f"\nValor restante: "
            f"R$ {atendimento.calcular_valor_restante():.2f}"
        )

    def escolher_pagamento(self, atendimento):

        if not atendimento.lista_pagamentos:

            print(
                "Nenhum pagamento registrado."
            )

            return None

        print(
            "\n=== ESCOLHER PAGAMENTO ==="
        )

        for i, pagamento in enumerate(
            atendimento.lista_pagamentos
        ):

            print(
                f"{i+1} - "
                f"{pagamento.__class__.__name__}"
                f" - "
                f"R$ {pagamento.valor_pago:.2f}"
            )

        try:

            opcao = int(
                input("Escolha: ")
            )

            if (
                opcao < 1
                or
                opcao > len(
                    atendimento.lista_pagamentos
                )
            ):

                print(
                    "Pagamento inválido."
                )

                return None

            return atendimento.lista_pagamentos[
                opcao - 1
            ]

        except ValueError:

            print(
                "Digite um número válido."
            )

            return None

    def alterar_pagamento(self, atendimento):

        pagamento = self.escolher_pagamento(
            atendimento
        )

        if pagamento is None:
            return

        while True:

            print(
                "\n=== ALTERAR PAGAMENTO ==="
            )
            print("1 - Data")
            print("2 - Valor Pago")
            print("0 - Voltar")

            opcao = input("Opção: ")

            try:

                if opcao == "1":

                    pagamento.data = date(
                        int(input("Ano: ")),
                        int(input("Mês: ")),
                        int(input("Dia: "))
                    )

                    pagamento.registrar_pagamento()

                    print(
                        "Data alterada com sucesso."
                    )

                elif opcao == "2":

                    pagamento.valor_pago = float(
                        input("Novo valor: ")
                    )

                    pagamento.registrar_pagamento()

                    print(
                        "Valor alterado com sucesso."
                    )

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")

            except ValueError as erro:
                print(f"Erro: {erro}")

    def excluir_pagamento(self, atendimento):

        pagamento = self.escolher_pagamento(
            atendimento
        )

        if pagamento is None:
            return

        confirmacao = input(
            "Confirma exclusão? (s/n): "
        )

        if confirmacao.lower() == "s":

            atendimento.lista_pagamentos.remove(
                pagamento
            )

            print(
                "Pagamento removido com sucesso."
            )

    def abrir_menu(self, controlador_atendimento):

        while True:

            print("\n=== PAGAMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.cadastrar_pagamento(
                        atendimento
                    )

            elif opcao == "2":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.listar_pagamentos(
                        atendimento
                    )

            elif opcao == "3":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.alterar_pagamento(
                        atendimento
                    )

            elif opcao == "4":

                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento:
                    self.excluir_pagamento(
                        atendimento
                    )

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")