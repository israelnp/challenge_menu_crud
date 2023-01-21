from product_repository import ProductRepository


class ProductService:

    def __init__(self, respository: ProductRepository):
        self.respository = respository

    def add(self, code, name, amount, price):
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

    def get_per_code(self, code):
        product = self.respository.get_per_code(code)
        return {
            "code": product.code,
            "name": product.name,
            "amount": product.amount,
            "price": str(product.price)
        }

    def update(self, code, name, amount, price):
        self.respository.update(code, name, amount, price)

    def delete(self, code):
        self.respository.delete(code)
