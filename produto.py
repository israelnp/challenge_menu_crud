from peewee import Model, SqliteDatabase, TextField, IntegerField, DecimalField

db = SqliteDatabase('produto.db')


class Produto(Model):
    codigo = TextField()
    nome = TextField()
    quantidade = IntegerField()
    valor = DecimalField()

    class Meta:
        database = db


Produto.create_table()
