from produto_repositorio import ProdutoRepositorio
from produto_servico import ProdutoServico

repossitorio = ProdutoRepositorio()
servico = ProdutoServico(repossitorio)

while True:
    operacao = -1
    print("--------------------Menu--------------------------")
    print("__________________________________________________\n")
    print("(1) para inserir produto")
    print("(2) para busca por todos os produtos")
    print("(3) para buscar produto pelo ID")
    print("(4) para atualizar produto")
    print("(5) para deletar produto")
    print("(0) sair do programa")
    print("__________________________________________________\n")
    operacao = int(input("Escolha uma da operações acima para continuar:"))
    print("__________________________________________________\n")
    if operacao == 1:
        print("----------------Inserir Produto-------------------")
        print("__________________________________________________\n")
        codigo = input("Qual o código do produto?\t")
        nome = input("Qual o nome do produto?\t")
        quantidade = int(input("Qual a quantidade do produto?\t"))
        valor = float(input("Qual o valor do produto?\t"))
        servico.inserir_produto(codigo, nome, quantidade, valor)
    elif operacao == 2:
        print("----------------Buscar Produtos-------------------")
        print("__________________________________________________\n")
        for produto in servico.buscar_produtos():
            print(produto)
    elif operacao == 3:
        print("----------Buscar Produto por Cédigo-----------")
        print("__________________________________________________\n")
        codigo = input("Qual o código do produto?\t")
        print(servico.buscar_produtos_por_codigo(codigo))
    elif operacao == 4:
        print("----------------Atualizar Produto----------------")
        print("__________________________________________________\n")
        codigo = input("Qual o código do produto?\t")
        nome = input("Qual o nome do produto?\t")
        quantidade = int(input("Qual a quantidade do produto?\t"))
        valor = float(input("Qual o valor do produto?\t"))
        servico.atualizar_produto(codigo, nome, quantidade, valor)
    elif operacao == 5:
        print("----------------Remover Produto----------------")
        print("__________________________________________________\n")
        codigo = input("Qual o código do produto?\t")
        servico.deletar_produto(codigo)
    elif operacao == 0:
        break
