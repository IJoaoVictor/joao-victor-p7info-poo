class Pessoa:
    
    def __init__(self, sexo, nome, idade, altura, peso): # Método construtor
        self.sexo = sexo
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def printInfo(self):
        print("Sexo: " + str(self.sexo), "\nNome: " + str(self.nome), "\nIdade: " + str(self.idade),"\nAltura: " + str(self.altura), "\nPeso: " + str(self.peso))
        
ps  = Pessoa("Masculino", "João Victor", "17 anos", "1,69m", "70kg")
ps.printInfo()
