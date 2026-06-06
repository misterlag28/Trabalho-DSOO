from .Pessoas.profissional_saude import ProfissionalSaude

class Procedimento:

    def __init__(self, descricao: str, custo: float):

        if descricao.strip() == "":
            raise ValueError("Descrição inválida.")

        if custo < 0:
            raise ValueError("O custo não pode ser negativo.")

        self.__descricao = descricao
        self.__custo = custo

        self.profissional = None
        self.atendimentos = []

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if descricao.strip() == "":
            raise ValueError("Descrição inválida.")

        self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if custo < 0:
            raise ValueError("O custo não pode ser negativo.")

        self.__custo = custo


    def validar(self):
        if self.__descricao.strip() == "":
            raise ValueError("Descrição inválida.")

        if self.__custo < 0:
            raise ValueError("Custo inválido.")

        return True
