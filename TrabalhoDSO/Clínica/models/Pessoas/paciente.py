from ..pessoa import Pessoa


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

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self.__idade = idade