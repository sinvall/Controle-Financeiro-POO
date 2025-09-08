from Transacao import Transacao
from ControleFinanceiro import ControleFinanceiro

class Menu:
    def __init__(self):
        self.sistema = ControleFinanceiro()

    def exibir_menu(self):
        while True:
            try:
                print("\n===== MENU FINANCEIRO =====")
                print("1 - Adicionar Receita")
                print("2 - Adicionar Despesa")
                print("3 - Mostrar Saldo")
                print("4 - Mostrar Histórico")
                print("5 - Sair")
                opcao = input("Escolha uma opção: ").strip()

                if opcao == "1":
                    self.adicionar_transacao("Receita")
                elif opcao == "2":
                    self.adicionar_transacao("Despesa")
                elif opcao == "3":
                    self.mostrar_saldo()
                elif opcao == "4":
                    self.mostrar_historico()
                elif opcao == "5":
                    confirmar = input("Tem certeza que deseja sair? (s/n): ").strip().lower()
                    if confirmar == "s":
                        print("Saindo... Até logo!")
                        break
                else:
                    print("Opção inválida! Digite um número entre 1 e 5.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

    def adicionar_transacao(self, tipo):
        try:
            if tipo == "Receita":
                descricao = input("Digite a descrição da receita (ex: Salário, Venda): ").strip()
            else:
                descricao = input("Digite a descrição da despesa (ex: Aluguel, Supermercado): ").strip()

            valor = float(input(f"Digite o valor da {tipo.lower()}: ").strip())
            transacao = Transacao(valor, descricao, tipo)
            self.sistema.adicionar_transacao(transacao)
            print(f"{tipo} adicionada com sucesso!")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def mostrar_saldo(self):
        try:
            saldo = self.sistema.calcular_saldo()
            print(f"Saldo Atual: R$ {saldo:.2f}")
        except Exception as e:
            print(f"Erro ao mostrar saldo: {e}")

    def mostrar_historico(self):
        try:
            historico = self.sistema.historico()
            if historico:
                print("\n===== HISTÓRICO DE TRANSAÇÕES =====")
                for t in historico:
                    print(t)
            else:
                print("Nenhuma transação registrada.")
        except Exception as e:
            print(f"Erro ao mostrar histórico: {e}")