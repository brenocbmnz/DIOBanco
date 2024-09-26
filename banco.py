class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque_diario = 3
        self.saque_diario = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito. Insira um valor positivo.")

    def sacar(self, valor):
        if self.saque_diario >= self.limite_saque_diario:
            print("Limite de saques diários atingido.")
        elif valor > 500:
            print("Não é possível sacar valores acima de R$ 500,00 por vez.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saque_diario += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimento in self.extrato:
                print(movimento)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}")

    def resetar_limite_saques(self):
        self.saque_diario = 0

# Função para mostrar o menu
def mostrar_menu():
    print("\nEscolha uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")

# Inicializa a conta bancária
banco = Banco()

# Loop principal para interações do usuário
while True:
    mostrar_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        banco.depositar(valor_deposito)

    elif opcao == '2':
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        banco.sacar(valor_saque)

    elif opcao == '3':
        banco.mostrar_extrato()

    elif opcao == '4':
        print("Saindo do sistema. Obrigado por usar o banco.")
        break

    else:
        print("Opção inválida. Tente novamente.")
