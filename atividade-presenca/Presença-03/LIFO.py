pilha = []
num_elementos = int(input("Quantos elementos deseja inserir na pilha?: "))

for i in range(num_elementos):
    elemento = input("Insira um elemento na pilha: ")
    pilha.append(elemento)

print("Pilha de elementos: " + str(pilha))
pilha.pop()
print("Pilha de elementos LIFO: " + str(pilha))
