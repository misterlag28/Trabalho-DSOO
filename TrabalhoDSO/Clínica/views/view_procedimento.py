from modelos.atendimento.procedimento import Procedimento


class ViewProcedimento:
    def __init__(self, controlador_procedimento):
        self.controlador = controlador_procedimento

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
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento: "))
                    if idx < 0 or idx >= len(atendimentos):
                        print("Índice inválido.")
                        continue
                    atendimento = atendimentos[idx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                nome = input("Nome do procedimento: ")
                descricao = input("Descrição: ")
                try:
                    custo = float(input("Custo: "))
                    if custo <= 0:
                        print("Erro: Custo deve ser positivo.")
                        continue
                except ValueError:
                    print("Custo inválido.")
                    continue
                procedimento = Procedimento(nome, descricao, custo, atendimento.profissional)
                try:
                    self.controlador.registrar_procedimento(atendimento, procedimento)
                    print("Procedimento registrado com sucesso.")
                except ValueError as erro:
                    print(f"Erro: {erro}")
            elif opcao == "2":
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento para listar procedimentos: "))
                    if idx < 0 or idx >= len(atendimentos):
                        print("Índice inválido.")
                        continue
                    atendimento = atendimentos[idx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                procedimentos = self.controlador.listar_procedimentos(atendimento)
                if not procedimentos:
                    print("Nenhum procedimento registrado.")
                    continue
                for p in procedimentos:
                    print("\n")
                    print(p.exibir_dados())
            elif opcao == "3":
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento: "))
                    if idx < 0 or idx >= len(atendimentos):
                        print("Índice inválido.")
                        continue
                    atendimento = atendimentos[idx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                procedimentos = self.controlador.listar_procedimentos(atendimento)
                if not procedimentos:
                    print("Nenhum procedimento registrado.")
                    continue
                for i, p in enumerate(procedimentos):
                    print(f"{i} - {p.nome} - R$ {p.custo:.2f}")
                try:
                    pidx = int(input("Escolha o procedimento: "))
                    if pidx < 0 or pidx >= len(procedimentos):
                        print("Índice inválido.")
                        continue
                    procedimento = procedimentos[pidx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                novo_nome = input("Novo nome (enter para manter): ")
                nova_desc = input("Nova descrição (enter para manter): ")
                novo_custo = input("Novo custo (enter para manter): ")
                try:
                    novo_custo = float(novo_custo) if novo_custo else None
                except ValueError:
                    print("Custo inválido.")
                    continue
                try:
                    self.controlador.alterar_procedimento(atendimento, procedimento, nome=novo_nome if novo_nome else None, descricao=nova_desc if nova_desc else None, custo=novo_custo)
                    print("Procedimento alterado com sucesso.")
                except ValueError as erro:
                    print(f"Erro: {erro}")
            elif opcao == "4":
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento: "))
                    if idx < 0 or idx >= len(atendimentos):
                        print("Índice inválido.")
                        continue
                    atendimento = atendimentos[idx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                procedimentos = self.controlador.listar_procedimentos(atendimento)
                if not procedimentos:
                    print("Nenhum procedimento registrado.")
                    continue
                for i, p in enumerate(procedimentos):
                    print(f"{i} - {p.nome} - R$ {p.custo:.2f}")
                try:
                    pidx = int(input("Escolha o procedimento para excluir: "))
                    if pidx < 0 or pidx >= len(procedimentos):
                        print("Índice inválido.")
                        continue
                    procedimento = procedimentos[pidx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                confirm = input("Confirma exclusão? (s/n): ")
                if confirm.lower() == 's':
                    self.controlador.excluir_procedimento(atendimento, procedimento)
                    print("Procedimento removido com sucesso.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")