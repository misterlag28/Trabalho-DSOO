class ControladorRelatorio:

    def abrir_menu(self, controlador_atendimento):

        while True:

            print("\n=== RELATÓRIOS ===")
            print("1 - Clínicas com mais atendimentos")
            print("2 - Atendimento mais caro e mais barato")
            print("3 - Procedimentos mais realizados")
            print("4 - Procedimento mais caro e mais barato")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.relatorio_clinicas(
                    controlador_atendimento
                )

            elif opcao == "2":
                self.relatorio_atendimentos(
                    controlador_atendimento
                )

            elif opcao == "3":
                self.relatorio_procedimentos_realizados(
                    controlador_atendimento
                )

            elif opcao == "4":
                self.relatorio_procedimentos_valor(
                    controlador_atendimento
                )

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

    def relatorio_clinicas(self, controlador_atendimento):

        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        contagem = {}

        for atendimento in atendimentos:

            nome = atendimento.clinica.nome

            if nome in contagem:
                contagem[nome] += 1
            else:
                contagem[nome] = 1

        maior = max(contagem.values())

        print("\n=== CLÍNICAS COM MAIS ATENDIMENTOS ===")

        for nome, quantidade in contagem.items():

            if quantidade == maior:

                print(
                    f"{nome} - "
                    f"{quantidade} atendimento(s)"
                )

    def relatorio_atendimentos(self, controlador_atendimento):

        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        mais_caro = atendimentos[0]
        mais_barato = atendimentos[0]

        for atendimento in atendimentos:

            if (
                atendimento.calcular_valor_total()
                >
                mais_caro.calcular_valor_total()
            ):
                mais_caro = atendimento

            if (
                atendimento.calcular_valor_total()
                <
                mais_barato.calcular_valor_total()
            ):
                mais_barato = atendimento

        print("\n=== ATENDIMENTO MAIS CARO ===")
        print(mais_caro.exibir_dados())

        print("\n=== ATENDIMENTO MAIS BARATO ===")
        print(mais_barato.exibir_dados())

    def relatorio_procedimentos_realizados(
        self,
        controlador_atendimento
    ):

        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        contagem = {}

        for atendimento in atendimentos:

            for procedimento in atendimento.lista_procedimentos:

                nome = procedimento.nome

                if nome in contagem:
                    contagem[nome] += 1
                else:
                    contagem[nome] = 1

        if not contagem:
            print("Nenhum procedimento registrado.")
            return

        maior = max(contagem.values())

        print(
            "\n=== PROCEDIMENTOS MAIS REALIZADOS ==="
        )

        for nome, quantidade in contagem.items():

            if quantidade == maior:

                print(
                    f"{nome} - "
                    f"{quantidade} vez(es)"
                )

    def relatorio_procedimentos_valor(
        self,
        controlador_atendimento
    ):

        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        procedimentos = []

        for atendimento in atendimentos:

            for procedimento in atendimento.lista_procedimentos:

                procedimentos.append(
                    procedimento
                )

        if not procedimentos:
            print("Nenhum procedimento registrado.")
            return

        mais_caro = procedimentos[0]
        mais_barato = procedimentos[0]

        for procedimento in procedimentos:

            if procedimento.custo > mais_caro.custo:
                mais_caro = procedimento

            if procedimento.custo < mais_barato.custo:
                mais_barato = procedimento

        print("\n=== PROCEDIMENTO MAIS CARO ===")
        print(mais_caro.exibir_dados())

        print("\n=== PROCEDIMENTO MAIS BARATO ===")
        print(mais_barato.exibir_dados())