class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self): #Propriedade salario criada
        return self.__salario

    @salario.setter
    def salario(self, novo_salario): 
    #Uma vez restringido o acesso à propriedade salário, é instruído que altere o valor da variável salario usando a função calcula_salario()
        raise ValueError("Impossivel alterar o salário diretamente. Use a função calcula_salario()")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

func = Funcionario('João', 'Programador', 50)
func.salario = 100000 
