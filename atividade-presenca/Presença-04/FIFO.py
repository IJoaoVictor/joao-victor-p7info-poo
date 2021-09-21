pilha = []
num_elementos = int(input("Quantos elementos deseja inserir na pilha?: "))

for i in range(num_elementos):
    elemento = input("Insira um elemento na sua pilha: ")
    pilha.append(elemento)

print("Pilha de elementos: " + str(pilha))
del pilha[0]
print("Pilha de elementos FIFO: " + str(pilha))
