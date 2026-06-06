from services.Clinica import ClinicaController

class ViewClinica:
    def __init__(self):
        pass

    def exibir_menu(self):
        print("============= Sistema da Clínica ============")
        print("1. Cadastrar Clinica")
        print("2. Cadastrar Procedimento")
        print("3. Fazer Atendimento")
        print("4. Listar Procedimentos de um atendimento")
        print("5. Listar Atendimentos")
        print("6. Sair")

    def obter_opcao(self):
        opcao = input("Escolha uma opção: ")
        return opcao

    def cadastrar_clinica(self):
        nome = input("Digite o nome da clínica: ")
        cidade = input("Digite a cidade da clínica: ")
        descricao = input("Digite a descrição da clínica: ")
        clinica = ClinicaController.criar_clinica(nome, cidade, descricao)
        print(f"Clínica '{clinica.nome}' cadastrada com sucesso!")

    

        

    