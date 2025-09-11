class ControleFinanceiro:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        if not transacao:
            raise ValueError("Transação inválida.")
        self.transacoes.append(transacao)

    def remover_transacao(self, indice):
        if indice < 0 or indice >= len(self.transacoes):
            raise IndexError("Índice inválido.")
        return self.transacoes.pop(indice)

    def calcular_saldo(self):
        saldo = 0
        for t in self.transacoes:
            saldo = t.aplicar(saldo)
        return saldo

    def historico(self):
        return [str(t) for t in self.transacoes]

    def simular_investimento(self, meses, taxa=0, aporte_mensal=0):
        saldo_atual = self.calcular_saldo()
        resultados = []
        for mes in range(1, meses + 1):
            saldo_atual += aporte_mensal
            if taxa > 0:
                saldo_atual *= (1 + taxa / 100)
            resultados.append((mes, saldo_atual))
        return resultados
