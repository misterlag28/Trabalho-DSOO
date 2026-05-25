class TipoAtendimento:

    def __init__(self, nome_tipo: str):
        self.__nome_tipo = nome_tipo

    @property
    def nome_tipo(self):
        return self.__nome_tipo

    @nome_tipo.setter
    def nome_tipo(self, nome_tipo: str):
        self.__nome_tipo = nome_tipo