class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"{self.nome} esta latindo")
        
meu_cachorro = Cachorro("Rex", 5)

print(meu_cachorro.nome)

meu_cachorro.latir()
