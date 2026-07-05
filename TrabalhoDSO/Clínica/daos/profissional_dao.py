from daos.dao import DAO
from modelos.pessoa.profissional_saude import ProfissionalSaude

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional: ProfissionalSaude):
        if (profissional is not None) and isinstance(profissional, ProfissionalSaude) and isinstance(profissional.cpf, str):
            super().add(profissional.cpf, profissional)

    def update(self, profissional: ProfissionalSaude):
        if (profissional is not None) and isinstance(profissional, ProfissionalSaude) and isinstance(profissional.cpf, str):
            super().update(profissional.cpf, profissional)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
