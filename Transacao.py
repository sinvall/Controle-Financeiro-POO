from datetime import datetime

class Transacao:
    def __init__(self, valor, descricao, tipo):
        #Tratamento de Exceção
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O valor da transação deve ser um número positivo.")
        if not descricao.strip():
            raise ValueError("A descrição da transação não pode estar vazia.")
        if tipo not in ["Receita", "Despesa"]:
            raise ValueError("O tipo da transação deve ser 'Receita' ou 'Despesa'.")
        
        self.valor = valor
        self.descricao = descricao
        self.tipo = tipo  # "Receita" ou "Despesa"
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        sinal = "+" if self.tipo == "Receita" else "-"
        return f"[{self.data}] {self.tipo}: {self.descricao} {sinal}R${self.valor:.2f}"
