def printDecimal(num):
    return str(num)

def printOctal(num):
    return str(oct(num)[2:])

def printHexadecimal(num):
    return str(hex(num)[2:])

def printBinário(num):
    return str(bin(num)[2:])

def imprimirTabela():
    for count in range(256):
        print("Decimal       Octal       Hexadecimal         Binário    ")
        print("-------      -------     -------------      -----------")
        print("{:14s} {:14s} {:14s} {:s} \n" .format(printDecimal(count), printOctal(count), printHexadecimal(count), printBinário(count)))

imprimirTabela()

