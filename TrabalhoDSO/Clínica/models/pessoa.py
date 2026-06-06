from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @abstractmethod
    def tipo_pessoa(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular: str):
        if len(celular) != 11 and len(celular) != 10:
            raise ValueError("Número de celular deve conter 11 dígitos.")
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos.")
        self.__cpf = cpf