from Pessoa import Pessoa


class Paciente(Pessoa):

    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        idade: int
    ):
        super().__init__(nome, celular, cpf)

        self.__idade = idade

        # RELAÇÕES
        self.atendimentos = []
        self.pagamentos = []

    def tipo_pessoa(self):
        return "Paciente"

    # GETTERS
    def get_idade(self):
        return self.__idade

    # SETTERS
    def set_idade(self, idade: int):
        self.__idade = idade