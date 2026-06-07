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
        if not (celular.isdigit() and (len(celular) == 10 or len(celular) == 11)):
            raise ValueError("Celular deve conter apenas 10 ou 11 dígitos numéricos")
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if not (cpf.isdigit() and len(cpf) == 11):
            raise ValueError("CPF deve conter apenas 11 dígitos numéricos")
        self.__cpf = cpf
