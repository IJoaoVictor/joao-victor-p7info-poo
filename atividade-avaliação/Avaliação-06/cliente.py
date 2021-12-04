from Database import db

from tipocliente import TipoCliente


class Cliente(db.Model):
    __tablename__ = 'TB_CLIENTE'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    codigo = db.Column(db.Integer, nullable=False)
    cnpjcpf = db.Column(db.String, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def str(self):
        string = "\nid={4} codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self.tipo, self.cnpjcpf, self.codigo, self.nome, self.id)
        return string

if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 100, '200.100.345-34', 1)
    print(cliente.str())