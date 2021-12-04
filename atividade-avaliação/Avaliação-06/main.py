from Database import db

from produto import Produto
from cliente import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal

def main():

    db.create_all()

    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34", 1)
    db.session.add(cli)
    db.session.commit()

    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    db.session.add(p1)
    db.session.commit()

    it1 = ItemNotaFiscal(1, 1, 10, 1, 1)
    db.session.add(it1)
    db.session.commit()

    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    db.session.add(p2)
    db.session.commit()

    it2 = ItemNotaFiscal(2, 2, 10, 2, 1)
    db.session.add(it2)
    db.session.commit()

    p3 = Produto(3, 300, "Macarao Fortaleza", 4.5)
    db.session.add(p3)
    db.session.commit()

    it3 = ItemNotaFiscal(3, 3, 10, 3, 1)
    db.session.add(it3)
    db.session.commit()

    nf = NotaFiscal(1, 100, 1)
    db.session.add(nf)
    db.session.commit()

    nf.calcularNotaFiscal()

    nf.imprimirNotaFiscal()

if __name__ == '__main__':
    main()