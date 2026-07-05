from modelos.clinica import Clinica
from datetime import time
from daos.clinica_dao import ClinicaDAO

class ControladorClinica:
    def __init__(self):
        self.__clinica_dao = ClinicaDAO()

    def limpar_dados(self):
        self.__clinica_dao.clear()

    def cadastrar_clinica(self, clinica: Clinica) -> None:
        
        if not clinica.nome or not clinica.nome.strip():
            raise ValueError("Nome da clínica é obrigatório")
        if not clinica.cidade or not clinica.cidade.strip():
            raise ValueError("Cidade é obrigatória")
        
        if self.__clinica_dao.get(clinica.nome) is not None:
            raise ValueError(f"Clínica com nome '{clinica.nome}' já cadastrada")
        
        clinica.validar_horarios()
        self.__clinica_dao.add(clinica)

    def listar_clinicas(self) -> list:
        return self.__clinica_dao.get_all()

    def excluir_clinica(self, nome: str) -> bool:
        clinica = self.__clinica_dao.get(nome)
        if clinica is not None:
            self.__clinica_dao.remove(nome)
            return True
        return False

    def alterar_clinica(self, nome: str, novo_nome: str = None, nova_cidade: str = None, nova_descricao: str = None, abertura: time = None, fechamento: time = None) -> bool:
        clinica = self.__clinica_dao.get(nome)
        if clinica is not None:
            if novo_nome is not None:
                if not novo_nome.strip():
                    raise ValueError("Nome da clínica não pode estar vazio")
                if novo_nome != nome and self.__clinica_dao.get(novo_nome) is not None:
                    raise ValueError(f"Clínica com nome '{novo_nome}' já cadastrada")
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
            
            if novo_nome is not None and novo_nome != nome:
                self.__clinica_dao.remove(nome)
            
            self.__clinica_dao.add(clinica)
            return True
            
        return False

    def escolher_clinica_por_index(self, index: int):
        clinicas = self.listar_clinicas()
        if index < 0 or index >= len(clinicas):
            return None
        return clinicas[index]

    def escolher_clinica_por_nome(self, nome: str):
        return self.__clinica_dao.get(nome)
