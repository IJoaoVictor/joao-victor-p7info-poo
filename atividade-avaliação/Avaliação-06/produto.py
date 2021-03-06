from Database import db

class Produto(db.Model):
    __tablename__ = 'TB_PRODUTO'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    valorUnitario = db.Column(db.Float, nullable=False)

    def __init__(self, id, codigo, descricao, valorUnitario):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.valorUnitario = valorUnitario

    def getDescricao(self):
        return self.descricao

    def getValorUnitario(self):
        return self.valorUnitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self.valorUnitario, self.descricao, self.codigo, self.id)
        return string

if __name__ == '__main__':
    produto = Produto(id=1, codigo=100, descricao="Arroz Agulha", valorUnitario=5.5)
    print(produto.str())