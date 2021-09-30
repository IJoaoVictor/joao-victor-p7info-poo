import math
class Ponto():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def setX(self, valor):
        self.x = valor

    def getY(self):
        return self.y

    def setY(self, valor):
        self.y = valor

class Reta():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getPontoA(self):
        return self.a

    def setPontoA(self, valor):
        self.a = valor

    def getPontoB(self):
        return self.b

    def setPontoB(self, valor):
        self.b = valor

    def calcularDistancia(self):

        dist = math.sqrt(math.pow((self.getPontoB().getX() - self.getPontoA().getX()), 2) + math.pow((self.getPontoB().getY() - self.getPontoA().getY()), 2))

        print("\nPonto A: (" + str(self.getPontoA().getX()) + "," + str(self.getPontoA().getY()) +")")
        print("Ponto B: (" + str(self.getPontoB().getX()) + "," + str(self.getPontoB().getY()) +")")

        print("\nValor da distância: " + str(dist))

PA = Ponto(int(input("Insira a coordenada X do ponto A: ")), int(input("Insira a coordenada Y do ponto A: ")))
PB = Ponto(int(input("\nInsira a coordenada X do ponto B: ")), int(input("Insira a coordenada Y do ponto B: ")))

reta = Reta(PA, PB)
reta.calcularDistancia()