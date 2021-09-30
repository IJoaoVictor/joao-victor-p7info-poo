# Uma Composição é uma relação entre dois objetos para criar um só, representando um relacionamento do tipo "todo/parte"
class Contato:
    
 def __init__(self, nome):
  self.__nome = nome
  
 def retornaNome(self):
  return self.__nome

class Agenda:
 
 cnt = []
 
 def __init__(self):
  
  while True:
   print("\nDigite 1 para adicionar um contato")
   print("Digite 2 para exibir a lista de contatos")
   op = int(input("\nEscolha uma opção: "))
   
   if op == 1:
    self.adicionar()
    
   elif op == 2:
    self.exibir()
   
   else:
    print("Opção invalida")
 
 def adicionar(self):
  nome = input("Escreva o nome do contato: ")
  self.cnt.append(Contato(nome)) 
  # Á medida que for contradado um funcionário, ele será adicionado na lista de funcionários, a func. Caracterizando desse modo, uma composição
 
 def exibir(self):
     print("\nLista de contatos")
     
     for contato in self.cnt:
         print(contato.retornaNome())  

Agenda()

