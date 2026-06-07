from modelos.pessoa.profissional_saude import ProfissionalSaude
from modelos.pessoa.paciente import Paciente


class ControladorPessoa:
    def __init__(self, pacientes=None, profissionais=None):
        self._pacientes: list[Paciente] = pacientes if pacientes is not None else []
        self._profissionais: list[ProfissionalSaude] = profissionais if profissionais is not None else []

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
        for p in self._pacientes:
            if p.cpf == paciente.cpf:
                raise ValueError(f"Paciente com CPF {paciente.cpf} já cadastrado")
        
        self._pacientes.append(paciente)
        return True

    def listar_pacientes(self) -> list:
        return self._pacientes

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
        
        for idx, paciente in enumerate(self._pacientes):
            if paciente.nome == nome_mudado:
                self._pacientes[idx] = novo_paciente
                return True
        return False

    def remover_paciente(self, nome: str) -> bool:
        for paciente in self._pacientes:
            if paciente.nome == nome:
                self._pacientes.remove(paciente)
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
        for p in self._profissionais:
            if p.cpf == profissional.cpf:
                raise ValueError(f"Profissional com CPF {profissional.cpf} já cadastrado")
        
        self._profissionais.append(profissional)
        return True

    def listar_profissionais(self) -> list:
        return self._profissionais

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
        
        for idx, profissional in enumerate(self._profissionais):
            if profissional.nome == nome_mudado:
                self._profissionais[idx] = novo_profissional
                return True
        return False

    def remover_profissional(self, nome: str) -> bool:
        for profissional in self._profissionais:
            if profissional.nome == nome:
                self._profissionais.remove(profissional)
                return True
        return False