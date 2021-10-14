# Sistema que armazena a lista de funcionários de uma empresa

# Nas classes abaixo, ocorre um relacionamento de "Agregação"

class Funcionário: # Classe

    def __init__(self, nome, cargo, salario):     # Atributos
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Lista_Funcionario: # Classe

    def __init__(self):
        self.funcionarios = [] # Atributo

    def adicionar_funcionario(self, funcionario):     # Método
        self.funcionarios.append(funcionario)

    def lista_funcionarios(self):                 # Método
        print("Lista de Funcionários")
        for funcionario in self.funcionarios: 
            print(f"Nome: {funcionario.nome} | Cargo: {funcionario.cargo} | Salário: R${funcionario.salario}")

lista = Lista_Funcionario()

funcionario1 = Funcionário("João", "Analista de Sistemas", 3500)
funcionario2 = Funcionário("Maria", "Engenheira de Software", 4500)
funcionario3 = Funcionário("Carlos", "Programador Júnior", 2000)

lista.adicionar_funcionario(funcionario1) # Agregação
lista.adicionar_funcionario(funcionario2) # Agregação
lista.adicionar_funcionario(funcionario3) # Agregação

lista.lista_funcionarios()