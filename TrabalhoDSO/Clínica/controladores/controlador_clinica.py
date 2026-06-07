from modelos.clinica import Clinica
from datetime import time
class ControladorClinica:
    def __init__(self, clinicas=None):
        self.__clinicas: list[Clinica] = clinicas if clinicas is not None else []

    def cadastrar_clinica(self, clinica: Clinica) -> None:
        
        if not clinica.nome or not clinica.nome.strip():
            raise ValueError("Nome da clínica é obrigatório")
        if not clinica.cidade or not clinica.cidade.strip():
            raise ValueError("Cidade é obrigatória")
        
        for c in self.__clinicas:
            if c.nome == clinica.nome:
                raise ValueError(f"Clínica com nome '{clinica.nome}' já cadastrada")
        
        clinica.validar_horarios()
        self.__clinicas.append(clinica)

    def listar_clinicas(self) -> list:
        return self.__clinicas

    def excluir_clinica(self, nome: str) -> bool:
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                self.__clinicas.remove(clinica)
                return True
        return False

    def alterar_clinica(self, nome: str, novo_nome: str = None, nova_cidade: str = None, nova_descricao: str = None, abertura: time = None, fechamento: time = None) -> bool:
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                
                if novo_nome is not None:
                    if not novo_nome.strip():
                        raise ValueError("Nome da clínica não pode estar vazio")
                    clinica.nome = novo_nome
                if nova_cidade is not None:
                    if not nova_cidade.strip():
                        raise ValueError("Cidade não pode estar vazia")
                    clinica.cidade = nova_cidade
                if nova_descricao is not None:
                    clinica.descricao = nova_descricao
                if abertura is not None:
                    clinica.abertura = abertura
                if fechamento is not None:
                    clinica.fechamento = fechamento
                clinica.validar_horarios()
                return True
        return False

    def escolher_clinica_por_index(self, index: int):
        if index < 0 or index >= len(self.__clinicas):
            return None
        return self.__clinicas[index]

    def escolher_clinica_por_nome(self, nome: str):
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                return clinica
        return None
