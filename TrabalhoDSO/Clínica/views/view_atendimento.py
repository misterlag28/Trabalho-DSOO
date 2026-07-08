import FreeSimpleGUI as sg
from datetime import date, time
from modelos.atendimento.atendimento import Atendimento
from modelos.enum.tipo_atendimento import TipoAtendimento


class ViewAtendimento:
    def __init__(self, controlador_atendimento, controlador_clinica, controlador_pessoa):
        self.controlador_atendimento = controlador_atendimento
        self.controlador_clinica = controlador_clinica
        self.controlador_pessoa = controlador_pessoa

    def abrir_menu(self):
        while True:
            layout = [
                [sg.Text('ATENDIMENTOS', font=("", 16))],
                [sg.Button('Cadastrar', key='1', size=(20, 1))],
                [sg.Button('Listar', key='2', size=(20, 1))],
                [sg.Button('Alterar', key='3', size=(20, 1))],
                [sg.Button('Excluir', key='4', size=(20, 1))],
                [sg.Button('Voltar', key='0', size=(20, 1))]
            ]
            window = sg.Window('Atendimentos', layout, element_justification='c')
            event, _ = window.read()
            window.close()

            if event in (sg.WINDOW_CLOSED, '0'):
                break

            opcao = event
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.alterar()
            elif opcao == "4":
                self.excluir()

    def cadastrar(self):
        pacientes = self.controlador_pessoa.listar_pacientes()
        if not pacientes:
            sg.popup("Nenhum paciente cadastrado.")
            return
            
        profissionais = self.controlador_pessoa.listar_profissionais()
        if not profissionais:
            sg.popup("Nenhum profissional cadastrado.")
            return
            
        clinicas = self.controlador_clinica.listar_clinicas()
        if not clinicas:
            sg.popup("Nenhuma clínica cadastrada.")
            return
            
        nomes_pacientes = [f"{i} - {p.nome}" for i, p in enumerate(pacientes)]
        nomes_profs = [f"{i} - {pr.nome} ({pr.especialidade})" for i, pr in enumerate(profissionais)]
        nomes_clinicas = [f"{i} - {c.nome}" for i, c in enumerate(clinicas)]
        tipos_atendimento = [f"{i} - {t.value}" for i, t in enumerate(TipoAtendimento)]
        
        layout_cad = [
            [sg.Text('Paciente:', size=(18, 1)), sg.Combo(nomes_pacientes, key='paciente', readonly=True, size=(40, 1))],
            [sg.Text('Profissional:', size=(18, 1)), sg.Combo(nomes_profs, key='profissional', readonly=True, size=(40, 1))],
            [sg.Text('Clínica:', size=(18, 1)), sg.Combo(nomes_clinicas, key='clinica', readonly=True, size=(40, 1))],
            [sg.Text('Data (DD/MM/YYYY):', size=(18, 1)), sg.Input(key='dia', size=(5,1)), sg.Text('/'), sg.Input(key='mes', size=(5,1)), sg.Text('/'), sg.Input(key='ano', size=(6,1))],
            [sg.Text('Início (HH:MM):', size=(18, 1)), sg.Input(key='hi', size=(5,1)), sg.Text(':'), sg.Input(key='mi', size=(5,1))],
            [sg.Text('Fim (HH:MM):', size=(18, 1)), sg.Input(key='hf', size=(5,1)), sg.Text(':'), sg.Input(key='mf', size=(5,1))],
            [sg.Text('Valor Base:', size=(18, 1)), sg.Input(key='valor')],
            [sg.Text('Tipo:', size=(18, 1)), sg.Combo(tipos_atendimento, key='tipo', readonly=True, size=(40, 1))],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        
        win_cad = sg.Window('Cadastrar Atendimento', layout_cad)
        ev_cad, val_cad = win_cad.read()
        win_cad.close()
        
        if ev_cad == 'Salvar':
            try:
                if not val_cad['paciente'] or not val_cad['profissional'] or not val_cad['clinica'] or not val_cad['tipo']:
                    sg.popup_error("Preencha as seleções (Paciente, Profissional, Clínica, Tipo).")
                    return
                
                pidx = int(val_cad['paciente'].split(' - ')[0])
                paciente = pacientes[pidx]
                if paciente.idade < 18:
                    sg.popup_error("Erro ao cadastrar atendimento: Paciente menor de 18 anos não pode realizar atendimento")
                    return
                
                pridx = int(val_cad['profissional'].split(' - ')[0])
                profissional = profissionais[pridx]
                
                cidx = int(val_cad['clinica'].split(' - ')[0])
                clinica = clinicas[cidx]
                
                ano = int(val_cad['ano'])
                mes = int(val_cad['mes'])
                dia = int(val_cad['dia'])
                data_atendimento = date(ano, mes, dia)
                
                hi = int(val_cad['hi'])
                mi = int(val_cad['mi'])
                hf = int(val_cad['hf'])
                mf = int(val_cad['mf'])
                horario_inicio = time(hi, mi)
                horario_fim = time(hf, mf)
                
                if horario_fim <= horario_inicio:
                    sg.popup_error("Erro ao cadastrar atendimento: Horário fim deve ser maior que horário de início")
                    return
                    
                if clinica.abertura and clinica.fechamento:
                    if horario_inicio < clinica.abertura or horario_fim > clinica.fechamento:
                        sg.popup_error("Erro ao cadastrar atendimento: Horário do atendimento fora do horário de funcionamento da clínica")
                        return
                
                valor = float(val_cad['valor'])
                if valor <= 0:
                    sg.popup_error("Erro: Valor deve ser positivo.")
                    return
                
                tidx = int(val_cad['tipo'].split(' - ')[0])
                tipo = list(TipoAtendimento)[tidx]
                
                atendimento = Atendimento(data_atendimento, horario_inicio, horario_fim, valor, profissional, paciente, clinica, tipo)
                self.controlador_atendimento.cadastrar_atendimento(atendimento)
                sg.popup("Atendimento cadastrado com sucesso.")
                
            except ValueError as e:
                sg.popup_error(f"Erro: Entrada inválida - {e}")
            except Exception as e:
                sg.popup_error(f"Erro ao cadastrar atendimento: {e}")

    def listar(self):
        atendimentos = self.controlador_atendimento.listar_atendimentos()
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return
        texto = ""
        for i, a in enumerate(atendimentos):
            texto += f"{i} - {a.exibir_dados()}\n\n"
        sg.popup_scrolled(texto, title="Atendimentos", size=(60, 20))

    def alterar(self):
        atendimentos = self.controlador_atendimento.listar_atendimentos()
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return
            
        opcoes = [f"{i} - {a.data} {a.horario_inicio} (Pac: {a.paciente.nome})" for i, a in enumerate(atendimentos)]
        tipos_atendimento = [f"{i} - {t.value}" for i, t in enumerate(TipoAtendimento)]
        
        layout = [
            [sg.Text('Selecione o atendimento:'), sg.Combo(opcoes, key='atendimento', readonly=True, size=(50, 1))],
            [sg.Text('--- Deixe em branco os campos que não deseja alterar ---')],
            [sg.Text('Nova Data (DD/MM/YYYY):', size=(23, 1)), sg.Input(key='dia', size=(5,1)), sg.Text('/'), sg.Input(key='mes', size=(5,1)), sg.Text('/'), sg.Input(key='ano', size=(6,1))],
            [sg.Text('Nova Hora Início (HH:MM):', size=(23, 1)), sg.Input(key='hi', size=(5,1)), sg.Text(':'), sg.Input(key='mi', size=(5,1))],
            [sg.Text('Nova Hora Fim (HH:MM):', size=(23, 1)), sg.Input(key='hf', size=(5,1)), sg.Text(':'), sg.Input(key='mf', size=(5,1))],
            [sg.Text('Novo Valor Base:', size=(23, 1)), sg.Input(key='valor')],
            [sg.Text('Novo Tipo (opcional):', size=(23, 1)), sg.Combo([''] + tipos_atendimento, key='tipo', readonly=True, size=(40, 1))],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        
        win = sg.Window('Alterar Atendimento', layout)
        ev, val = win.read()
        win.close()
        
        if ev == 'Salvar':
            if not val['atendimento']:
                sg.popup_error("Nenhum atendimento selecionado.")
                return
                
            idx = int(val['atendimento'].split(' - ')[0])
            atendimento = self.controlador_atendimento.escolher_atendimento_por_index(idx)
            if not atendimento:
                sg.popup_error("Atendimento inválido.")
                return
                
            try:
                nova_data = None
                if val['ano'] and val['mes'] and val['dia']:
                    nova_data = date(int(val['ano']), int(val['mes']), int(val['dia']))
                    
                novo_horario_inicio = None
                if val['hi'] and val['mi']:
                    novo_horario_inicio = time(int(val['hi']), int(val['mi']))
                    
                novo_horario_fim = None
                if val['hf'] and val['mf']:
                    novo_horario_fim = time(int(val['hf']), int(val['mf']))
                    
                novo_valor = None
                if val['valor']:
                    novo_valor = float(val['valor'])
                    if novo_valor <= 0:
                        sg.popup_error("Erro: Valor deve ser positivo.")
                        return
                        
                novo_tipo = None
                if val['tipo']:
                    tidx = int(val['tipo'].split(' - ')[0])
                    novo_tipo = list(TipoAtendimento)[tidx]
                    
                self.controlador_atendimento.alterar_atendimento(
                    atendimento,
                    data=nova_data,
                    horario_inicio=novo_horario_inicio,
                    horario_fim=novo_horario_fim,
                    valor=novo_valor,
                    tipo=novo_tipo
                )
                sg.popup("Atendimento alterado com sucesso.")
            except ValueError as e:
                sg.popup_error(f"Erro: Entrada inválida - {e}")
            except Exception as e:
                sg.popup_error(f"Erro ao alterar atendimento: {e}")

    def excluir(self):
        atendimentos = self.controlador_atendimento.listar_atendimentos()
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return
            
        opcoes = [f"{i} - {a.data} {a.horario_inicio} (Pac: {a.paciente.nome})" for i, a in enumerate(atendimentos)]
        
        layout = [
            [sg.Text('Selecione o atendimento para excluir:')],
            [sg.Combo(opcoes, key='atendimento', readonly=True, size=(50, 1))],
            [sg.Button('Excluir', button_color='red'), sg.Button('Cancelar')]
        ]
        
        win = sg.Window('Excluir Atendimento', layout)
        ev, val = win.read()
        win.close()
        
        if ev == 'Excluir':
            if not val['atendimento']:
                sg.popup_error("Nenhum atendimento selecionado.")
                return
            idx = int(val['atendimento'].split(' - ')[0])
            atendimento = self.controlador_atendimento.escolher_atendimento_por_index(idx)
            if atendimento:
                self.controlador_atendimento.excluir_atendimento(atendimento)
                sg.popup("Atendimento excluído com sucesso.")