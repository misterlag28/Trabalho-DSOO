class ControladorRelatorio:
    def relatorio_clinicas(self, atendimentos):
        if not atendimentos:
            return {}
        contagem = {}
        for atendimento in atendimentos:
            nome = atendimento.clinica.nome
            contagem[nome] = contagem.get(nome, 0) + 1
        if not contagem:
            return {}
        maior = max(contagem.values())
        resultado = {nome: qtd for nome, qtd in contagem.items() if qtd == maior}
        return resultado

    def relatorio_atendimentos(self, atendimentos):
        if not atendimentos:
            return (None, None)
        mais_caro = atendimentos[0]
        mais_barato = atendimentos[0]
        for atendimento in atendimentos:
            if atendimento.calcular_valor_total() > mais_caro.calcular_valor_total():
                mais_caro = atendimento
            if atendimento.calcular_valor_total() < mais_barato.calcular_valor_total():
                mais_barato = atendimento
        return (mais_caro, mais_barato)

    def relatorio_procedimentos_realizados(self, atendimentos):
        contagem = {}
        for atendimento in atendimentos:
            for procedimento in atendimento.lista_procedimentos:
                nome = procedimento.nome
                contagem[nome] = contagem.get(nome, 0) + 1
        return contagem

    def relatorio_procedimentos_valor(self, atendimentos):
        procedimentos = []
        for atendimento in atendimentos:
            procedimentos.extend(atendimento.lista_procedimentos)
        if not procedimentos:
            return (None, None)
        mais_caro = max(procedimentos, key=lambda p: p.custo)
        mais_barato = min(procedimentos, key=lambda p: p.custo)
        return (mais_caro, mais_barato)