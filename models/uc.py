from ..extensions import db


# cria a tabela
class Uc(db.Model):
    __tablename__ = "ucs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    tipo = db.Column(db.String(50))
    inicio = db.Column(db.Date)
    fim = db.Column(db.Date)

    # mostar o conteudo do objeto
    def __repr__(self):
        return "<Uc(nome={}, tipo={}, inicio={}, fim={})>".format(self.nome, self.tipo, self.inicio, self.fim)