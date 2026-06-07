from modelos.pessoa.pessoa import Pessoa


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

        self.atendimentos = []
        self.pagamentos = []

    def tipo_pessoa(self):
        return "Paciente"

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if not isinstance(idade, int) or idade < 0 or idade > 150:
            raise ValueError("Idade inválida. Deve ser um número inteiro entre 0 e 150.")
        self.__idade = idade