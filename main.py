from product_repository import ProductRepository
from product_service import ProductService

repository = ProductRepository()
service = ProductService(repository)

while True:
    operation = -1
    print("--------------------Menu--------------------------")
    print("__________________________________________________\n")
    print("(1) to add product")
    print("(2) to get all products")
    print("(3) to get product per code")
    print("(4) to update product")
    print("(5) to delete product")
    print("(0) The end")
    print("__________________________________________________\n")
    operation = int(input("Choose one of the operations above to continue:\t"))
    print("__________________________________________________\n")
    if operation == 1:
        print("----------------Add Product-------------------")
        print("__________________________________________________\n")
        code = input("What is the product code?\t")
        name = input("What is the product name?\t")
        amount = int(input("What is the amount of the product?\t"))
        price = float(input("What is the price of the product?\t"))
        service.add(code, name, amount, price)
    elif operation == 2:
        print("----------------Get Produtos-------------------")
        print("__________________________________________________\n")
        for product in service.get():
            print(product)
    elif operation == 3:
        print("----------Get Product per Code-----------")
        print("__________________________________________________\n")
        code = input("What is the product code?\t")
        print(service.get_per_code(code))
    elif operation == 4:
        print("----------------Update Product----------------")
        print("__________________________________________________\n")
        code = input("What is the product code?\t")
        name = input("What is the product name?\t")
        amount = int(input("What is the amount of the product?\t"))
        price = float(input("What is the price of the product?\t"))
        service.update(code, name, amount, price)
    elif operation == 5:
        print("----------------Delete Product----------------")
        print("__________________________________________________\n")
        code = input("What is the product code?\t")
        service.delete(code)
    elif operation == 0:
        break
