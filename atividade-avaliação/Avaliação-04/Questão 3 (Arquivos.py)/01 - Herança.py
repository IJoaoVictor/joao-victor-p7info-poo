class Veiculo:
 def __init__(self, tipo, marca, km):
  self.tipo = tipo
  self.marca = marca
  self.km = km
  
class Carro(Veiculo):
 def __init__(self, tipo, marca, modelo, cor, ano, km, portas):
  Veiculo.__init__(self, tipo, marca, km) #Herdando da Classe Veiculo os seus atributos
  
  self.portas = portas
  self.modelo = modelo
  self.cor = cor
  self.ano = ano
 
 def printCarro(self):
  print("Tipo: " + str(self.tipo), "\nMarca: " + str(self.marca), "\nModelo: " + str(self.modelo),"\nCor: " + str(self.cor), "\nAno: " + str(self.ano), "\nCom", self.km, "km rodados e", self.portas, "portas")

carro = Carro("Carro", "Audi", "Audi Skysphere","Cinza", 2021, "10.000", 2)
carro.printCarro()
