from models.clinica import Clinica
import dados

class ClinicaController:
    def __init__(self):
        pass

    def cadastrar_clinica(self, nome: str, cidade: str, descricao: str):
        if nome.strip() == "":
            raise ValueError("Nome da clínica não pode ser vazio.")
        if cidade.strip() == "":
            raise ValueError("Cidade da clínica não pode ser vazia.")
        if descricao.strip() == "":
            raise ValueError("Descrição da clínica não pode ser vazia.")
        
        clinica = Clinica(nome, cidade, descricao)
        if clinica not in dados.clinicas:
            dados.clinicas.append(clinica)
        
        return clinica

    def listar_clinicas(self, clinicas):
        return dados.clinicas