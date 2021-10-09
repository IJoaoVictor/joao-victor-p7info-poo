"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
                
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor

    def imprimirNotaFiscal(self):
        p = "-" * 126
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        print(p)
        print("NOTA FISCAL" + " " * 105 + data)
        print("Cliente: " + str(self._cliente._codigo) + " " * 6 + "Nome: " + str(self._cliente._nome))
        print("CPF/CNPJ: " + str(self._cliente._cnpjcpf))
        print(p)
        print("ITENS")
        print(p)
        print("{:3s} {:66s} {:12s} {:26s} {:s}".format("Seq", "Descrição", "QTD", "Valor unit", "Preço"))
        print("--- -----------------------------------------------------------       -----       --------------       -----------------------")
        i = 0
        while i < 3:
            print("{:3s} {:68s} {:19s} {:28s} {:s}".format(str(self._itens[i].get_sequencial()),  str(self._itens[i].get_descricao()), str(self._itens[i].get_quantidade()), str(self._itens[i].get_valorUnitario()), str(self._itens[i].get_valorItem())))
            i += 1 
        print(p)
        print("Valor Total: ", str(self.valorNota))
    

