class Funcionario:

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
    
    def exibirDados(self):
        return f'Funcionario {self.name} ganha {self.wage}'

class Gerente(Funcionario):
    
    def __init__(self, name, wage, bonus):
        super().__init__(name, wage)
        self.bonus = bonus
    
    def exibirDados(self):
        info = super().exibirDados()
        print(f'{info} e tem um bonus de {self.bonus}')
        
class Programador(Funcionario):
    
    def __init__(self, name, wage, language):
        super().__init__(name, wage)
        self.language = language
        
    def exibirDados(self):
        info = super().exibirDados()
        print(f'{info} é trabalha com a linguagem {self.language}')
        
Roberto = Gerente('Roberto', 3000, 500)
Rodrigo = Programador('Rodrigo', 2300, 'React JS')

Roberto.exibirDados()
Rodrigo.exibirDados()

