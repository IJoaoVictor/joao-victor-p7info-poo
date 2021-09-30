class Veiculo:
    tipo = "Carro" # Variável de classe compartilhada por todas as instâncias
    
    def __init__(self, marca):
        self.marca = marca    # Variável de instância única para cada instância

c1 = Veiculo("Audi") # Único para c1
c2 = Veiculo("BMW")  # Único para c2
c3 = Veiculo("Ford") # Único para c2

print("Tipo do Veículo: " + c1.tipo + " | Marca do Veículo: " + c1.marca)
print("Tipo do Veículo: " + c2.tipo + " | Marca do Veículo: " + c2.marca)
print("Tipo do Veículo: " + c3.tipo + " | Marca do Veículo: " + c3.marca)


