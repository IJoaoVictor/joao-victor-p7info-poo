string = 0

while True:

    print("Digite 0 para encerrar...")
    frase = input("Digite algo: ")

    palavra = frase.split()
    lista = []

    if palavra == ["0"]:
        break

    for i in palavra:
        lista.append(str(len(i)))

        if len(i) >= string:
            string = len(i)
            maior_palavra = i

    saida = '-'.join(lista)

    print("\n   Entrada   |   Saída  ")
    print("------------------------")
    print(str(frase) + " | " + str(saida) + "\n")

print("\nA maior palavra digitada foi: %s" % maior_palavra)