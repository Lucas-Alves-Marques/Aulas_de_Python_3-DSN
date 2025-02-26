class Conta_Bancaria:

    taxa_juros = 0
    total_contas = 0

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        Conta_Bancaria.total_contas += 1

    def depositar(self, valor):
        if valor <= 0 :
            print("Deposito invalido")
        else:
            self.saldo += valor
            print(f'Valor depositado com sucesso')

    def sacar(self, valor):
        if valor <= 0 :
            print("Saque invalido")
        elif valor > self.saldo:
            print('Saldo Insuficiente')
        else :
            self.saldo -= valor
            print(f'Valor resgatado com sucesso')

    def verificar_saldo(self):
        print(f'Seu saldo atual é de {self.saldo}')

    def ajustar_taxa_juros(self,taxa):
        Conta_Bancaria.taxa_juros += taxa
        print(f'A nova taxa de Juros é de {Conta_Bancaria.taxa_juros}%')

    @classmethod
    def mostrar_total_contas(cls):
        if Conta_Bancaria.total_contas > 1:
            print(f"Total de contas é de {cls.total_contas} contas")
        else:
            print(f"Total de contas é de {Conta_Bancaria.total_contas} conta")
    
    @staticmethod
    def converter_moeda(valor, conversão):
        return valor*conversão
    
    @staticmethod
    def dias_no_ano():
        return 365
        

# conta1 = Conta_Bancaria('Lucas', 100)
# conta2 = Conta_Bancaria('Lucas', 100)
# conta3 = Conta_Bancaria('Lucas', 100)
# conta4 = Conta_Bancaria('Lucas', 100)

# conta1.contas()
# conta1.depositar(200)
# conta1.sacar(20)
# conta1.verificar_saldo()
# conta1.ajustar_taxa_juros(10)
# conta1.ajustar_taxa_juros(15)
# conta1.mostrar_total_contas()
# resultado = conta1.converter_moeda(5,5.5)
# print(resultado)
print(Conta_Bancaria.dias_no_ano())


