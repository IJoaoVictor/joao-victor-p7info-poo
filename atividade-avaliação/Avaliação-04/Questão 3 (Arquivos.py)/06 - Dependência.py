# Há uma relação de dependência com as classes abaixo
class Carro:
    
    def __init__(self,marca):
        self.marca = marca

    def ligandoCarro(self):
        print("O carro da marca " + str(self.marca) + " foi ligado")
    
    def desligandoCarro(self):
        print("O carro da marca " + str(self.marca) + " foi desligado")

class Pessoa:
    
    def ligarCarro(self, acao):
        acao.ligandoCarro()
    
    def desligarCarro(self, acao):
        acao.desligandoCarro()

veiculo = Carro("Audi")
pessoa = Pessoa()

pessoa.ligarCarro(veiculo) 
#O método ligarCarro da classe Pessoa depende do método ligandoCarro da classe Carro para funcionar 

pessoa.desligarCarro(veiculo) 
#Assim como no exemplo anterior, o método desligarCarro da classe Pessoa depende do método desligandoCarro da classe Carro para funcionar
