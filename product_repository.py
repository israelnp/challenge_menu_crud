from pydantic import validate_arguments

from product import Product


class ProductRepository:

    @validate_arguments
    def add(self, code: int, name: str, amount: int, price: float):
        product = Product(code=code, name=name,
                          amount=amount, price=price)
        product.save()

    def get(self):
        return Product.select()

    @validate_arguments
    def get_per_code(self, code: int):
        return Product.get(Product.code == code)

    @validate_arguments
    def update(self, code: int, name: str, amount: int, price: float):
        product = Product.select().where(Product.code == code).get()
        product.name = name
        product.amount = amount
        product.price = price
        product.save()

    @validate_arguments
    def delete(self, code: int):
        product = Product.get(Product.code == code)
        product.delete_instance()
