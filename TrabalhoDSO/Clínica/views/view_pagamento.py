from datetime import date
from modelos.pagamento.dinheiro import Dinheiro
from modelos.pagamento.pix import Pix
from modelos.pagamento.cartao_credito import CartaoCredito


class ViewPagamento:
    def __init__(self, controlador_pagamento):
        self.controlador = controlador_pagamento

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
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                atendimento = controlador_atendimento.escolher_atendimento_por_index(idx)
                if atendimento is None:
                    print("Atendimento inválido.")
                    continue
                try:
                    ano = int(input("Ano: "))
                    mes = int(input("Mês: "))
                    dia = int(input("Dia: "))
                    data_pagamento = date(ano, mes, dia)
                    valor_pago = float(input("Valor pago: "))
                except ValueError:
                    print("Entrada inválida.")
                    continue
                print("\n1 - Dinheiro")
                print("2 - Pix")
                print("3 - Cartão")
                tipo = input("Opção: ")
                try:
                    if tipo == "1":
                        valor_recebido = float(input("Valor recebido pelo cliente (para calcular troco): "))
                        pagamento = Dinheiro(data_pagamento, atendimento, atendimento.paciente, valor_pago, valor_recebido)
                    elif tipo == "2":
                        cpf = input("CPF do pagante: ")
                        pagamento = Pix(data_pagamento, atendimento, atendimento.paciente, valor_pago, cpf)
                    elif tipo == "3":
                        numero = input("Número do cartão: ")
                        bandeira = input("Bandeira: ")
                        parcelas = int(input("Quantidade de parcelas: "))
                        pagamento = CartaoCredito(data_pagamento, atendimento, atendimento.paciente, valor_pago, numero, bandeira, parcelas)
                    else:
                        print("Opção inválida.")
                        continue
                    self.controlador.registrar_pagamento(pagamento)
                    print("Pagamento registrado com sucesso.")
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
                    idx = int(input("Escolha o atendimento para listar pagamentos: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                atendimento = controlador_atendimento.escolher_atendimento_por_index(idx)
                if atendimento is None:
                    print("Atendimento inválido.")
                    continue
                pagamentos = self.controlador.listar_pagamentos(atendimento)
                if not pagamentos:
                    print("Nenhum pagamento registrado.")
                    continue
                for p in pagamentos:
                    print(f"Tipo: {p.__class__.__name__}")
                    print(f"Data: {p.data}")
                    print(f"Valor pago: R$ {p.valor_pago:.2f}")
                    if hasattr(p, 'troco'):
                        print(f"Troco: R$ {p.troco:.2f}")
                print(f"\nValor restante: R$ {atendimento.calcular_valor_restante():.2f}")
            elif opcao == "3":
                atendimentos = controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                atendimento = controlador_atendimento.escolher_atendimento_por_index(idx)
                if atendimento is None:
                    print("Atendimento inválido.")
                    continue
                pagamentos = self.controlador.listar_pagamentos(atendimento)
                if not pagamentos:
                    print("Nenhum pagamento registrado.")
                    continue
                for i, p in enumerate(pagamentos):
                    print(f"{i} - {p.__class__.__name__} - R$ {p.valor_pago:.2f}")
                try:
                    pidx = int(input("Escolha o pagamento: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                pagamento = self.controlador.escolher_pagamento_por_index(atendimento, pidx)
                if pagamento is None:
                    print("Pagamento inválido.")
                    continue
                try:
                    novo_valor = input("Novo valor (enter para manter): ")
                    if novo_valor:
                        novo_valor = float(novo_valor)
                    else:
                        novo_valor = None
                    self.controlador.alterar_pagamento(pagamento, valor_pago=novo_valor)
                    print("Pagamento alterado com sucesso.")
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
                except ValueError:
                    print("Escolha inválida.")
                    continue
                atendimento = controlador_atendimento.escolher_atendimento_por_index(idx)
                if atendimento is None:
                    print("Atendimento inválido.")
                    continue
                pagamentos = self.controlador.listar_pagamentos(atendimento)
                if not pagamentos:
                    print("Nenhum pagamento registrado.")
                    continue
                for i, p in enumerate(pagamentos):
                    print(f"{i} - {p.__class__.__name__} - R$ {p.valor_pago:.2f}")
                try:
                    pidx = int(input("Escolha o pagamento para excluir: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                pagamento = self.controlador.escolher_pagamento_por_index(atendimento, pidx)
                if pagamento is None:
                    print("Pagamento inválido.")
                    continue
                confirm = input("Confirma exclusão? (s/n): ")
                if confirm.lower() == 's':
                    self.controlador.excluir_pagamento(atendimento, pagamento)
                    print("Pagamento removido com sucesso.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")