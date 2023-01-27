from peewee import DecimalField, IntegerField, Model, SqliteDatabase, TextField

db = SqliteDatabase('product.db')


class Product(Model):
    code = TextField()
    name = TextField()
    amount = IntegerField()
    price = DecimalField()

    class Meta:
        database = db


Product.create_table()
