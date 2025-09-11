from ControleFinanceiro import ControleFinanceiro
from Receita import Receita
from Despesa import Despesa


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
                print("5 - Remover Transação")
                print("6 - Simulador de Investimento")
                print("7 - Sair")
                opcao = input("Escolha uma opção: ").strip()

                if opcao == "1":
                    self.adicionar_transacao(Receita)
                elif opcao == "2":
                    self.adicionar_transacao(Despesa)
                elif opcao == "3":
                    self.mostrar_saldo()
                elif opcao == "4":
                    self.mostrar_historico()
                elif opcao == "5":
                    self.remover_transacao()
                elif opcao == "6":
                    self.simular_investimento()
                elif opcao == "7":
                    confirmar = input(
                        "Tem certeza que deseja sair? (s/n): ").strip().lower()
                    if confirmar == "s":
                        print("Saindo... Até logo!")
                        break
                else:
                    print("Opção inválida! Digite um número entre 1 e 7.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

    def adicionar_transacao(self, classe_transacao):
        try:
            descricao = input("Digite a descrição dessa Transação: ").strip()

            # checa se a descrição está vazia.
            if not descricao:
                raise ValueError("A descrição não pode estar vazia.")

            # checa se a descrição é um número.
            is_numeric = False
            try:
                float(descricao)
                is_numeric = True
            except ValueError:
                is_numeric = False

            if is_numeric:
                raise ValueError(
                    "A descrição não pode ser apenas um valor numérico.")

            valor_str = input("Digite o valor: ").strip().replace(',', '.')
            valor = float(valor_str)

            transacao = classe_transacao(valor, descricao)
            self.sistema.adicionar_transacao(transacao)
            print(f"{classe_transacao.__name__} adicionada com sucesso!")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

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
                for i, t in enumerate(historico):
                    print(f"{i} - {t}")
            else:
                print("Nenhuma transação registrada.")
        except Exception as e:
            print(f"Erro ao mostrar histórico: {e}")

    def remover_transacao(self):
        try:
            self.mostrar_historico()
            historico_atual = self.sistema.historico()
            if not historico_atual:
                return

            indice_str = input(
                "Digite o número da transação que deseja remover: ").strip()
            if not indice_str.isdigit():
                raise ValueError(
                    "Índice inválido. Por favor, digite um número.")

            indice = int(indice_str)
            removida = self.sistema.remover_transacao(indice)
            print(f"Transação removida com sucesso: {removida}")
        except (ValueError, IndexError) as e:
            print(f"Erro ao remover: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def simular_investimento(self):
        try:
            saldo_atual = self.sistema.calcular_saldo()
            if saldo_atual <= 0:
                raise ValueError(
                    "Não há saldo disponível para simulação. "
                    "Adicione uma receita antes de simular o investimento."
                )

            print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

            meses_str = input("Digite o número de meses para simulação: ").strip()
            if not meses_str.isdigit() or int(meses_str) <= 0:
                raise ValueError("O número de meses deve ser um inteiro positivo.")
            meses = int(meses_str)

            taxa_str = input(
                "Digite a taxa de rendimento mensal (%), ou deixe vazio (0%): "
            ).strip().replace(',', '.')
            taxa = float(taxa_str) if taxa_str else 0.0
            if taxa < 0:
                raise ValueError("A taxa de rendimento não pode ser negativa.")

            aporte_str = input(
                "Digite o valor do aporte mensal (deixe vazio se não houver): "
            ).strip().replace(',', '.')
            aporte_mensal = float(aporte_str) if aporte_str else 0.0
            if aporte_mensal < 0:
                raise ValueError("O aporte mensal não pode ser negativo.")

            resultados = self.sistema.simular_investimento(meses, taxa, aporte_mensal)

            print("\n===== RESULTADO DA SIMULAÇÃO DE INVESTIMENTO =====")
            for mes, saldo in resultados:
                print(f"Final do Mês {mes}: R$ {saldo:.2f}")

        except ValueError as ve:
            print(f"Erro na simulação: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
