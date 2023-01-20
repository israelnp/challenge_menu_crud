from peewee import Model, SqliteDatabase, TextField

db = SqliteDatabase('produto.db')


class Produto(Model):
    codigo = TextField()
    nome = TextField()
    quantidade = TextField()
    valor = TextField()

    class Meta:
        database = db


Produto.create_table()
