from datetime import datetime


class Transacao:
    def __init__(self, valor, descricao):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(
                "O valor da transação deve ser um número positivo.")

        clean_descricao = descricao.strip()

        if not clean_descricao:
            raise ValueError("A descrição da transação não pode estar vazia.")

        if any(char.isdigit() for char in clean_descricao):
            raise ValueError("A descrição não pode conter números.")

        self.valor = valor
        self.descricao = clean_descricao  # Atribui a descrição já limpa
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        # Método genérico (sobrescrito nas subclasses)
        return f"[{self.data}] {self.descricao} R${self.valor:.2f}"

    def aplicar(self, saldo_atual):
        """Polimórfico: cada subclasse implementa sua própria lógica"""
        raise NotImplementedError(
            "Este método deve ser implementado nas subclasses.")
