# As duas classes possuem uma relação de associação

class Contato:
    def __init__(self, nome):
        self.nome = nome
    
    def ligar(self):
        print("Ligando para " + str(self.nome))
    
    def mensagem(self):
        print("Enviando mensagem para " + str(self.nome))

class Pessoa:
    
    def ligar_contato(self, contato):
        contato.ligar()
    
    def mensagem_contato(self, contato):
        contato.mensagem()
    
pessoa = Pessoa()
contato_raquel = Contato("Raquel")
mensagem_carlos = Contato("Carlos")

pessoa.ligar_contato(contato_raquel)
pessoa.mensagem_contato(mensagem_carlos) 

# O objeto pessoa da classe Pessoa está se associando com a classe Contato

