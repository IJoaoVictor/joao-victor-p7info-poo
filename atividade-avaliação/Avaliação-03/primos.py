n = int(input("Digite um número inteiro positivo: "))

def soma_primos(n):

    soma = 0
    contador = 0
    num = 2
    primos = []

    while contador < n:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break

        if primo:
            primos.append(num)
            soma += num
            contador += 1
        num += 1

    print("Os " + str(int(n)) + " primeiros termos: " + str(primos))
    print("A soma dos " + str(int(n)) + " primeiros termos são: " + str(int(soma)))

print(soma_primos(n))
