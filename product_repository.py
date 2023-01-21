from product import Product


class ProductRepository:

    def add(self, code, name, amount, price):
        product = Product(code=code, name=name,
                          amount=amount, price=price)
        product.save()

    def get(self):
        return Product.select()

    def get_per_code(self, code):
        return Product.get(Product.code == code)

    def update(self, code, name, amount, price):
        product = Product.select().where(Product.code == code).get()
        product.name = name
        product.amount = amount
        product.price = price
        product.save()

    def delete(self, code):
        product = Product.get(Product.code == code)
        product.delete_instance()
