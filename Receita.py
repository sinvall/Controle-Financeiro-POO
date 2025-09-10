from Transacao import Transacao

class Receita(Transacao):
    def __init__(self, valor, descricao):
        super().__init__(valor, descricao)

    def __str__(self):
        return f"[{self.data}] Receita: {self.descricao} +R${self.valor:.2f}"

    def aplicar(self, saldo_atual):
        return saldo_atual + self.valor
