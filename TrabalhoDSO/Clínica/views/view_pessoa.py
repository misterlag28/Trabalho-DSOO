from controladores.controlador_pessoa import ControladorPessoa
from modelos.pessoa.paciente import Paciente
from modelos.pessoa.profissional_saude import ProfissionalSaude


class ViewPessoa:
    def __init__(self, controlador_pessoa: ControladorPessoa):
        self.controlador = controlador_pessoa

    def obter_opcao(self, texto="Escolha uma opção: "):
        opcao = input(texto)
        return opcao

    def abrir_menu_paciente(self):
        print("\n=== MENU PACIENTE ===")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Editar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Voltar")
        resposta = self.obter_opcao()
        if resposta == "1":
            try:
                nome = self.obter_opcao("Digite o nome do paciente para cadastrar: ")
                try:
                    idade = int(self.obter_opcao("Digite a idade do paciente para cadastrar: "))
                except ValueError:
                    print("Erro: Idade deve ser um número inteiro válido.")
                    return
                cpf = self.obter_opcao("Digite o CPF do paciente para cadastrar: ")
                celular = self.obter_opcao("Digite o telefone do paciente para cadastrar: ")
                
                novoPaciente = Paciente(nome=nome, idade=idade, cpf=cpf, celular=celular)
                self.controlador.cadastrar_paciente(novoPaciente)
                print("Paciente cadastrado com sucesso.")
            except ValueError as erro:
                print(f"Erro ao cadastrar paciente: {erro}")
        elif resposta == "2":
            pacientes = self.controlador.listar_pacientes()
            for i in range(len(pacientes)):
                print(f"{i}: {pacientes[i].nome}")
                print(f"     {pacientes[i].idade} anos, {pacientes[i].cpf}, {pacientes[i].celular}")
                print()
        elif resposta == "3":
            try:
                nome_antigo = self.obter_opcao("Digite o nome do paciente para ser editado: ")
                nome = self.obter_opcao("Digite o novo nome do paciente: ")
                try:
                    idade = int(self.obter_opcao("Digite a nova idade do paciente: "))
                except ValueError:
                    print("Erro: Idade deve ser um número inteiro válido.")
                    return
                cpf = self.obter_opcao("Digite o novo CPF do paciente: ")
                celular = self.obter_opcao("Digite o novo telefone do paciente: ")
                
                novoPaciente = Paciente(nome=nome, idade=idade, cpf=cpf, celular=celular)
                alterado = self.controlador.editar_paciente(nome_antigo, novoPaciente)
                if alterado:
                    print("Paciente alterado com sucesso.")
                else:
                    print("Paciente não encontrado.")
            except ValueError as erro:
                print(f"Erro ao editar paciente: {erro}")

        elif resposta == "4":
            print("Excluir Paciente")
            nome = self.obter_opcao("Digite o nome do paciente para ser excluído: ")
            removido = self.controlador.remover_paciente(nome)
            if removido:
                print("Paciente removido com sucesso.")
            else:
                print("Paciente não encontrado.")

        elif resposta == "0":
            print("Voltando ao menu principal.")


    def abrir_menu_profissional(self):
        print("\n=== MENU PROFISSIONAL ===")
        print("1 - Cadastrar Profissional")
        print("2 - Listar Profissionais")
        print("3 - Editar Profissional")
        print("4 - Excluir Profissional")
        print("0 - Voltar")
        resposta = self.obter_opcao()
        if resposta == "1":
            try:
                nome = self.obter_opcao("Digite o nome do profissional para cadastrar: ")
                celular = self.obter_opcao("Digite o telefone do profissional para cadastrar: ")
                cpf = self.obter_opcao("Digite o CPF do profissional para cadastrar: ")
                especialidade = self.obter_opcao("Digite a especialidade do profissional para cadastrar: ")
                registro_profissional = self.obter_opcao("Digite o registro profissional para cadastrar: ")
                
                novoProfissional = ProfissionalSaude(nome=nome, celular=celular, cpf=cpf, 
                                                      especialidade=especialidade, 
                                                      registro_profissional=registro_profissional)
                self.controlador.cadastrar_profissional(novoProfissional)
                print("Profissional cadastrado com sucesso.")
            except ValueError as erro:
                print(f"Erro ao cadastrar profissional: {erro}")
        elif resposta == "2":
            profissionais = self.controlador.listar_profissionais()
            for i in range(len(profissionais)):
                print(f"{i}: {profissionais[i].nome}")
                print(f"     {profissionais[i].especialidade}, {profissionais[i].cpf}, {profissionais[i].celular}")
                print()
        elif resposta == "3":
            try:
                nome_antigo = self.obter_opcao("Digite o nome do profissional para ser editado: ")
                nome = self.obter_opcao("Digite o novo nome do profissional: ")
                celular = self.obter_opcao("Digite o novo telefone do profissional: ")
                cpf = self.obter_opcao("Digite o novo CPF do profissional: ")
                especialidade = self.obter_opcao("Digite a nova especialidade do profissional: ")
                registro_profissional = self.obter_opcao("Digite o novo registro profissional: ")
                
                novoProfissional = ProfissionalSaude(nome=nome, celular=celular, cpf=cpf,
                                                      especialidade=especialidade,
                                                      registro_profissional=registro_profissional)
                alterado = self.controlador.editar_profissional(nome_antigo, novoProfissional)
                if alterado:
                    print("Profissional alterado com sucesso.")
                else:
                    print("Profissional não encontrado.")
            except ValueError as erro:
                print(f"Erro ao editar profissional: {erro}")

        elif resposta == "4":
            print("Excluir Profissional")
            nome = self.obter_opcao("Digite o nome do profissional para ser excluído: ")
            removido = self.controlador.remover_profissional(nome)
            if removido:
                print("Profissional removido com sucesso.")
            else:
                print("Profissional não encontrado.")

        elif resposta == "0":
            print("Voltando ao menu principal.")
    
