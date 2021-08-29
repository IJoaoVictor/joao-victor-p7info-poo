import random
i = 0
lista = []

while i < 6:
    num = random.randint(1, 61)
    lista.append(num)
    i += 1

print("Números sorteados: " + str(lista))
