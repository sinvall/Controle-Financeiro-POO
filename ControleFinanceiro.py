class ControleFinanceiro:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def remover_transacao(self, indice):
        if not isinstance(indice, int) or not (0 <= indice < len(self.transacoes)):
            raise IndexError(
                "Índice fora do intervalo. Por favor, escolha um número da lista.")

        return self.transacoes.pop(indice)

    def calcular_saldo(self):
        saldo = 0
        for t in self.transacoes:
            saldo = t.aplicar(saldo)
        return saldo

    def historico(self):
        return [str(t) for t in self.transacoes]

    # --- MÉTODO MODIFICADO ---
    def simular_poupanca(self, meses, taxa=0, aporte_mensal=0):
        # Simula uma poupança futura, incluindo aportes mensais.

        saldo_simulado = self.calcular_saldo()
        resultados = []

        print(
            f"\n--- Iniciando simulação com Saldo Inicial de R$ {saldo_simulado:.2f} ---")

        for mes in range(1, meses + 1):
            # Adiciona o aporte do mês (se houver)
            if aporte_mensal > 0:
                saldo_simulado += aporte_mensal

            # Aplica o rendimento sobre o novo total
            if taxa > 0:
                saldo_simulado *= (1 + taxa / 100)

            resultados.append((mes, saldo_simulado))

        return resultados
