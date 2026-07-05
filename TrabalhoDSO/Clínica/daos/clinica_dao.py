from daos.dao import DAO
from modelos.clinica import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica: Clinica):
        if (clinica is not None) and isinstance(clinica, Clinica) and isinstance(clinica.nome, str):
            super().add(clinica.nome, clinica)

    def update(self, clinica: Clinica):
        if (clinica is not None) and isinstance(clinica, Clinica) and isinstance(clinica.nome, str):
            super().update(clinica.nome, clinica)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
