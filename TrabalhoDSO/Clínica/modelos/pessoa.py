from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @abstractmethod
    def tipo_pessoa(self):
        pass

    # GETTERS
    def get_nome(self):
        return self.__nome

    def get_celular(self):
        return self.__celular

    def get_cpf(self):
        return self.__cpf

    # SETTERS
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_celular(self, celular: str):
        self.__celular = celular

    def set_cpf(self, cpf: str):
        self.__cpf = cpf