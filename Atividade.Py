x=10

class Exemplo:
    
    Y=20
    
    def __init__(self):
        
        self.z =30
    
    def acessar_variavel(self):
        
        w=40
        
        print(f'Variavel Global X : {x}')
        
        print(f'Variavel Da Classe Y : {Exemplo.Y}')
        
        print(f'Variavel de instancia z: {self.z}')
        
        print(f'Variavel local W: {w}')
        
exemplo = Exemplo()

exemplo.acessar_variavel()

print(f'\n Accesando a varivael global x fora da classe: {x}')
