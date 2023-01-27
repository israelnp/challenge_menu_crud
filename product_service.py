from pydantic import validate_arguments

from product_repository import ProductRepository


class ProductService:

    def __init__(self, respository: ProductRepository):
        self.respository = respository

    @validate_arguments
    def add(self, code: int, name: str, amount: int, price: float):
        self.respository.add(code, name, amount, price)

    def get(self):
        produtos = []
        for product in self.respository.get():
            produtos.append({
                "code": product.code,
                "name": product.name,
                "amount": product.amount,
                "price": str(product.price)
            })
        return produtos

    @validate_arguments
    def get_per_code(self, code: int):
        product = self.respository.get_per_code(code)
        return {
            "code": product.code,
            "name": product.name,
            "amount": product.amount,
            "price": str(product.price)
        }

    @validate_arguments
    def update(self, code: int, name: str, amount: int, price: float):
        self.respository.update(code, name, amount, price)

    @validate_arguments
    def delete(self, code: int):
        self.respository.delete(code)
