from Pessoa import Pessoa


class ProfissionalSaude(Pessoa):

    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        especialidade: str,
        registro_profissional: str
    ):
        super().__init__(nome, celular, cpf)

        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

        # RELAÇÕES
        self.atendimentos = []
        self.procedimentos = []

    def tipo_pessoa(self):
        return "Profissional de Saúde"

    # GETTERS
    def get_especialidade(self):
        return self.__especialidade

    def get_registro_profissional(self):
        return self.__registro_profissional

    # SETTERS
    def set_especialidade(self, especialidade: str):
        self.__especialidade = especialidade

    def set_registro_profissional(self, registro_profissional: str):
        self.__registro_profissional = registro_profissional