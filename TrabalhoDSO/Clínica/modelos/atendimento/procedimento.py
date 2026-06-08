from modelos.pessoa.profissional_saude import ProfissionalSaude

class Procedimento:

    def __init__(
        self,
        nome,
        descricao,
        custo,
        profissional
    ):

        self.nome = nome
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):

        if not novo_nome.strip():
            raise ValueError(
                "Nome inválido."
            )

        self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):

        if not nova_descricao.strip():
            raise ValueError(
                "Descrição inválida."
            )

        self.__descricao = nova_descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):

        if novo_custo <= 0:
            raise ValueError(
                "O custo deve ser maior que zero."
            )

        self.__custo = novo_custo

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, novo_profissional):

        self.__profissional = novo_profissional

    def validar_procedimento(self):

        if self.custo <= 0:
            raise ValueError(
                "Custo inválido."
            )

        return True

    def exibir_dados(self):

        return (
            f"Nome: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"Custo: R$ {self.custo:.2f}\n"
            f"Profissional: {self.profissional.nome}"
        )
