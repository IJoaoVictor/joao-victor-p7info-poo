from Database import db

import datetime
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal(db.Model):
    __tablename__ = 'TB_NOTA_FISCAL'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey("TB_CLIENTE.id"), nullable=False)
    data = db.Column(db.String, nullable=False)
    itens = db.relationship("ItemNotaFiscal", backref="NotaFiscal", lazy=True)

    def __init__(self, id, codigo, id_cliente):
        self.id = id
        self.codigo = codigo
        self.id_cliente = id_cliente
        self.data = datetime.datetime.now().strftime("%d-%m-%Y")

    def calcularNotaFiscal(self):
        valor = 0.0
        i = 0
        while i < 3:
            valor = valor + self.itens[i].get_valorItem()
            i += 1
        self.valorNota = valor

    def imprimirNotaFiscal(self):
        p = "-" * 126
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        print(p)
        print("NOTA FISCAL" + " " * 105 + data)

        clientes = Cliente.query.all()
        for cliente in clientes:
            print("Cliente: " + str(cliente.codigo) + " " * 6 + "Nome: " + str(cliente.nome))
            print("CPF/CNPJ: " + str(cliente.cnpjcpf))

        print(p)
        print("ITENS")
        print(p)
        print("{:3s} {:66s} {:12s} {:26s} {:s}".format("Seq", "Descrição", "QTD", "Valor unit", "Preço"))
        print("--- -----------------------------------------------------------       -----       --------------       -----------------------")
        i = 0
        while i < 3:
            print("{:3s} {:68s} {:19s} {:28s} {:s}".format(str(self.itens[i].get_sequencial()),  str(self.itens[i].get_descricao()), str(self.itens[i].get_quantidade()), str(self.itens[i].get_valorUnitario()), str(self.itens[i].get_valorItem())))
            i += 1
        print(p)
        print("Valor Total: ", str(self.valorNota))