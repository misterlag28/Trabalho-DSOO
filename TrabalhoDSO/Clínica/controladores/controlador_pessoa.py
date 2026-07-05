from modelos.pessoa.profissional_saude import ProfissionalSaude
from modelos.pessoa.paciente import Paciente
from daos.paciente_dao import PacienteDAO
from daos.profissional_dao import ProfissionalDAO

class ControladorPessoa:
    def __init__(self):
        self.__paciente_dao = PacienteDAO()
        self.__profissional_dao = ProfissionalDAO()

    def limpar_dados(self):
        self.__paciente_dao.clear()
        self.__profissional_dao.clear()

    # Paciente CRUD
    def cadastrar_paciente(self, paciente: Paciente) -> bool:
        # Validações de negócio
        if not paciente.nome or not paciente.nome.strip():
            raise ValueError("Nome do paciente é obrigatório")
        if paciente.idade < 1 or paciente.idade > 150:
            raise ValueError(f"Idade inválida: deve estar entre 1 e 150")
        if not paciente.cpf or len(paciente.cpf.replace(".", "").replace("-", "")) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        if not paciente.celular or len(paciente.celular.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")) < 10:
            raise ValueError("Telefone deve conter pelo menos 10 dígitos")
        
        # Verificar CPF duplicado
        if self.__paciente_dao.get(paciente.cpf) is not None:
            raise ValueError(f"Paciente com CPF {paciente.cpf} já cadastrado")
        
        self.__paciente_dao.add(paciente)
        return True

    def listar_pacientes(self) -> list:
        return self.__paciente_dao.get_all()

    def editar_paciente(self, nome_mudado: str, novo_paciente: Paciente) -> bool:
        # Validações de negócio
        if not novo_paciente.nome or not novo_paciente.nome.strip():
            raise ValueError("Nome do paciente é obrigatório")
        if novo_paciente.idade < 1 or novo_paciente.idade > 150:
            raise ValueError(f"Idade inválida: deve estar entre 1 e 150")
        if not novo_paciente.cpf or len(novo_paciente.cpf.replace(".", "").replace("-", "")) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        if not novo_paciente.celular or len(novo_paciente.celular.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")) < 10:
            raise ValueError("Telefone deve conter pelo menos 10 dígitos")
        
        for paciente in self.__paciente_dao.get_all():
            if paciente.nome == nome_mudado:
                if paciente.cpf != novo_paciente.cpf:
                    self.__paciente_dao.remove(paciente.cpf)
                self.__paciente_dao.add(novo_paciente)
                return True
        return False

    def remover_paciente(self, nome: str) -> bool:
        for paciente in self.__paciente_dao.get_all():
            if paciente.nome == nome:
                self.__paciente_dao.remove(paciente.cpf)
                return True
        return False

    # Profissional CRUD
    def cadastrar_profissional(self, profissional: ProfissionalSaude) -> bool:
        # Validações de negócio
        if not profissional.nome or not profissional.nome.strip():
            raise ValueError("Nome do profissional é obrigatório")
        if not profissional.cpf or len(profissional.cpf.replace(".", "").replace("-", "")) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        if not profissional.celular or len(profissional.celular.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")) < 10:
            raise ValueError("Telefone deve conter pelo menos 10 dígitos")
        if not profissional.especialidade or not profissional.especialidade.strip():
            raise ValueError("Especialidade é obrigatória")
        if not profissional.registro_profissional or not profissional.registro_profissional.strip():
            raise ValueError("Registro profissional é obrigatório")
        
        # Verificar CPF duplicado
        if self.__profissional_dao.get(profissional.cpf) is not None:
            raise ValueError(f"Profissional com CPF {profissional.cpf} já cadastrado")
        
        self.__profissional_dao.add(profissional)
        return True

    def listar_profissionais(self) -> list:
        return self.__profissional_dao.get_all()

    def editar_profissional(self, nome_mudado: str, novo_profissional: ProfissionalSaude) -> bool:
        # Validações de negócio
        if not novo_profissional.nome or not novo_profissional.nome.strip():
            raise ValueError("Nome do profissional é obrigatório")
        if not novo_profissional.cpf or len(novo_profissional.cpf.replace(".", "").replace("-", "")) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        if not novo_profissional.celular or len(novo_profissional.celular.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")) < 10:
            raise ValueError("Telefone deve conter pelo menos 10 dígitos")
        if not novo_profissional.especialidade or not novo_profissional.especialidade.strip():
            raise ValueError("Especialidade é obrigatória")
        if not novo_profissional.registro_profissional or not novo_profissional.registro_profissional.strip():
            raise ValueError("Registro profissional é obrigatório")
        
        for profissional in self.__profissional_dao.get_all():
            if profissional.nome == nome_mudado:
                if profissional.cpf != novo_profissional.cpf:
                    self.__profissional_dao.remove(profissional.cpf)
                self.__profissional_dao.add(novo_profissional)
                return True
        return False

    def remover_profissional(self, nome: str) -> bool:
        for profissional in self.__profissional_dao.get_all():
            if profissional.nome == nome:
                self.__profissional_dao.remove(profissional.cpf)
                return True
        return False