string = 0

while True:

    print("Digite 0 para encerrar...")
    frase = input("Digite algo: ")

    palavra = frase.split()  #Usando o método split para transformar cada palavra (substring) da frase em uma string separada
    lista = []

    if palavra == ["0"]: #Se a string 0 for digitada, o programa automaticamente para de ser executado
        break

    for i in palavra:
        lista.append(str(len(i))) #O tamanho de cada substring que foi gerada a partir da frase inserida será armazenado em "lista"

        if len(i) >= string:
            string = len(i)
            maior_palavra = i

    saida = '-'.join(lista) #Usando o método join para unir por traços cada string gerada

    print("\n   Entrada   |   Saída  ")
    print("------------------------")
    print(str(frase) + " | " + str(saida) + "\n")

print("\nA maior palavra digitada foi: %s" % maior_palavra) #Devolvendo a maior substring gerada