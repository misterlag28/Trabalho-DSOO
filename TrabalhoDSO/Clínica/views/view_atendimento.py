from datetime import date, time
from modelos.atendimento.atendimento import Atendimento
from modelos.enum.tipo_atendimento import TipoAtendimento


class ViewAtendimento:
    def __init__(self, controlador_atendimento, controlador_clinica, controlador_pessoa):
        self.controlador_atendimento = controlador_atendimento
        self.controlador_clinica = controlador_clinica
        self.controlador_pessoa = controlador_pessoa

    def abrir_menu(self):
        while True:
            print("\n=== ATENDIMENTOS ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Excluir")
            print("0 - Voltar")
            opcao = input("Opção: ")
            if opcao == "1":
                pacientes = self.controlador_pessoa.listar_pacientes()
                if not pacientes:
                    print("Nenhum paciente cadastrado.")
                    continue
                for i, p in enumerate(pacientes):
                    print(f"{i} - {p.nome}")
                try:
                    pidx = int(input("Escolha o paciente: "))
                    if pidx < 0 or pidx >= len(pacientes):
                        print("Índice inválido.")
                        continue
                    paciente = pacientes[pidx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                profissionais = self.controlador_pessoa.listar_profissionais()
                if not profissionais:
                    print("Nenhum profissional cadastrado.")
                    continue
                for i, pr in enumerate(profissionais):
                    print(f"{i} - {pr.nome} ({pr.especialidade})")
                try:
                    pridx = int(input("Escolha o profissional: "))
                    if pridx < 0 or pridx >= len(profissionais):
                        print("Índice inválido.")
                        continue
                    profissional = profissionais[pridx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                clinicas = self.controlador_clinica.listar_clinicas()
                if not clinicas:
                    print("Nenhuma clínica cadastrada.")
                    continue
                for i, c in enumerate(clinicas):
                    print(f"{i} - {c.nome}")
                try:
                    cidx = int(input("Escolha a clínica: "))
                    if cidx < 0 or cidx >= len(clinicas):
                        print("Índice inválido.")
                        continue
                    clinica = clinicas[cidx]
                except ValueError:
                    print("Escolha inválida.")
                    continue
                try:
                    ano = int(input("Ano (YYYY): "))
                    mes = int(input("Mês (MM): "))
                    dia = int(input("Dia (DD): "))
                    data_atendimento = date(ano, mes, dia)
                    
                    hi = int(input("Hora início (HH): "))
                    mi = int(input("Minuto início (MM): "))
                    hf = int(input("Hora fim (HH): "))
                    mf = int(input("Minuto fim (MM): "))
                    horario_inicio = time(hi, mi)
                    horario_fim = time(hf, mf)
                    
                    valor = float(input("Valor base do atendimento: "))
                    if valor <= 0:
                        print("Erro: Valor deve ser positivo.")
                        continue
                except ValueError as e:
                    print(f"Erro: Entrada inválida - {e}")
                    continue
                print("Tipo de atendimento:")
                for i, t in enumerate(TipoAtendimento):
                    print(f"{i} - {t.value}")
                try:
                    tidx = int(input("Escolha o tipo: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                tipos = list(TipoAtendimento)
                if tidx < 0 or tidx >= len(tipos):
                    print("Tipo inválido.")
                    continue
                tipo = tipos[tidx]
                try:
                    atendimento = Atendimento(data_atendimento, horario_inicio, horario_fim, valor, profissional, paciente, clinica, tipo)
                    self.controlador_atendimento.cadastrar_atendimento(atendimento)
                    print("Atendimento cadastrado com sucesso.")
                except ValueError as erro:
                    print(f"Erro ao cadastrar atendimento: {erro}")
            elif opcao == "2":
                atendimentos = self.controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
            elif opcao == "3":
                atendimentos = self.controlador_atendimento.listar_atendimentos()
                if not atendimentos:
                    print("Nenhum atendimento cadastrado.")
                    continue
                for i, a in enumerate(atendimentos):
                    print(f"{i} - {a.exibir_dados()}")
                try:
                    idx = int(input("Escolha o atendimento para excluir: "))
                except ValueError:
                    print("Escolha inválida.")
                    continue
                atendimento = self.controlador_atendimento.escolher_atendimento_por_index(idx)
                if atendimento is None:
                    print("Atendimento inválido.")
                    continue
                confirm = input("Confirma exclusão? (s/n): ")
                if confirm.lower() == 's':
                    self.controlador_atendimento.excluir_atendimento(atendimento)
                    print("Atendimento excluído com sucesso.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")