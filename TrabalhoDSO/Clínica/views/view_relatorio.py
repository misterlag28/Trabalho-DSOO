class ViewRelatorio:
    def __init__(self, controlador_relatorio):
        self.controlador = controlador_relatorio

    def abrir_menu(self, controlador_atendimento):
        while True:
            print("\n=== RELATÓRIOS ===")
            print("1 - Clínicas com mais atendimentos")
            print("2 - Atendimento mais caro e mais barato")
            print("3 - Procedimentos mais realizados")
            print("4 - Procedimento mais caro e mais barato")
            print("0 - Voltar")
            opcao = input("Opção: ")
            atendimentos = controlador_atendimento.listar_atendimentos()
            if opcao == "1":
                resultado = self.controlador.relatorio_clinicas(atendimentos)
                if not resultado:
                    print("Nenhum atendimento cadastrado.")
                else:
                    print("\n=== CLÍNICAS COM MAIS ATENDIMENTOS ===")
                    for nome, qtd in resultado.items():
                        print(f"{nome} - {qtd} atendimento(s)")
            elif opcao == "2":
                mais_caro, mais_barato = self.controlador.relatorio_atendimentos(atendimentos)
                if mais_caro is None:
                    print("Nenhum atendimento cadastrado.")
                else:
                    print("\n=== ATENDIMENTO MAIS CARO ===")
                    print(mais_caro.exibir_dados())
                    print("\n=== ATENDIMENTO MAIS BARATO ===")
                    print(mais_barato.exibir_dados())
            elif opcao == "3":
                contagem = self.controlador.relatorio_procedimentos_realizados(atendimentos)
                if not contagem:
                    print("Nenhum procedimento registrado.")
                else:
                    maior = max(contagem.values())
                    print("\n=== PROCEDIMENTOS MAIS REALIZADOS ===")
                    for nome, qtd in contagem.items():
                        if qtd == maior:
                            print(f"{nome} - {qtd} vez(es)")
            elif opcao == "4":
                mais_caro, mais_barato = self.controlador.relatorio_procedimentos_valor(atendimentos)
                if mais_caro is None:
                    print("Nenhum procedimento registrado.")
                else:
                    print("\n=== PROCEDIMENTO MAIS CARO ===")
                    print(mais_caro.exibir_dados())
                    print("\n=== PROCEDIMENTO MAIS BARATO ===")
                    print(mais_barato.exibir_dados())
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")