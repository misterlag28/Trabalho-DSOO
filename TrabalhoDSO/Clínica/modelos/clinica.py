from datetime import time

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str, abertura: time = None, fechamento: time = None):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__abertura = abertura
        self.__fechamento = fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def abertura(self):
        return self.__abertura

    @abertura.setter
    def abertura(self, abertura: time):
        self.__abertura = abertura

    @property
    def fechamento(self):
        return self.__fechamento

    @fechamento.setter
    def fechamento(self, fechamento: time):
        self.__fechamento = fechamento

    def validar_horarios(self):
        if self.__abertura is None or self.__fechamento is None:
            raise ValueError("Horários de abertura/fechamento não definidos.")
        if self.__abertura >= self.__fechamento:
            raise ValueError("Horário de abertura deve ser anterior ao de fechamento.")
        return True

    def exibir_dados(self):
        abertura = self.abertura.strftime('%H:%M') if self.abertura else 'N/A'
        fechamento = self.fechamento.strftime('%H:%M') if self.fechamento else 'N/A'
        return (
            f"Nome: {self.nome}\n"
            f"Cidade: {self.cidade}\n"
            f"Descrição: {self.descricao}\n"
            f"Abertura: {abertura}\n"
            f"Fechamento: {fechamento}"
        )