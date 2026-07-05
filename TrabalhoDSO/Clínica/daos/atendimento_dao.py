from daos.dao import DAO
from modelos.atendimento.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento) and isinstance(atendimento.id, str):
            super().add(atendimento.id, atendimento)

    def update(self, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento) and isinstance(atendimento.id, str):
            super().update(atendimento.id, atendimento)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
