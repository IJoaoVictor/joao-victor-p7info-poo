class Super:
    
 def Classe(self):
  print("Classe A")
  
class Sub (Super):
 
 def Classe(self):
  print("Classe B")

class Subsub (Sub):
 
 def Classe(self):
  print("Classe C")

chamada = Subsub()
chamada.Classe()
#Embora esteja sendo chamando sempre o mesmo método (Classe), que está presente em todas as classes e nas herdadas, o método se comporta de diferente

