from views.view_clinica import ViewClinica
from modelos.pessoa.profissional_saude import ProfissionalSaude
from modelos.pessoa.paciente import Paciente
from modelos.clinica import Clinica
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_clinica import ControladorClinica
from controladores.controlador_atendimento import ControladorAtendimento
from controladores.controlador_pagamento import ControladorPagamento
from controladores.controlador_procedimento import ControladorProcedimento
from controladores.controlador_relatorio import ControladorRelatorio
import FreeSimpleGUI as sg

def main():
    sg.set_options(font=("", 14))
    
    controlador_pessoa = ControladorPessoa()
    controlador_clinica = ControladorClinica()
    controlador_atendimento = ControladorAtendimento()
    controlador_pagamento = ControladorPagamento()
    controlador_procedimento = ControladorProcedimento()
    controlador_relatorio = ControladorRelatorio()

    view = ViewClinica(
        controlador_pessoa=controlador_pessoa,
        controlador_clinica=controlador_clinica,
        controlador_atendimento=controlador_atendimento,
        controlador_pagamento=controlador_pagamento,
        controlador_procedimento=controlador_procedimento,
        controlador_relatorio=controlador_relatorio
    )

    while True:
        view.exibir_menu()
        opcao = view.obter_opcao()
        view.validar_opcao(opcao)
        if opcao == "0":
            break


if __name__ == "__main__":
    main()


