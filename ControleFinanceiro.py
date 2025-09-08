class ControleFinanceiro:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        if not transacao:
            raise ValueError("Transação inválida.")
        self.transacoes.append(transacao)

    def calcular_saldo(self):
        try:
            saldo = 0
            for t in self.transacoes:
                if t.tipo == "Receita":
                    saldo += t.valor
                else:
                    saldo -= t.valor
            return saldo
        except Exception as e:
            print(f"Erro ao calcular saldo: {e}")
            return 0

    def historico(self):
        try:
            return [str(t) for t in self.transacoes]
        except Exception as e:
            print(f"Erro ao gerar histórico: {e}")
            return []
