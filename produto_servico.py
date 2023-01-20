from produto_repositorio import ProdutoRepositorio


class ProdutoServico:

    def __init__(self, respositorio: ProdutoRepositorio):
        self.repositorio = respositorio

    def inserir_produto(self, codigo, nome, quantidade, valor):
        self.repositorio.inserir_produto(codigo, nome, quantidade, valor)

    def buscar_produtos(self):
        produtos = []
        for produto in self.repositorio.buscar_produtos():
            produtos.append({
                "codigo": produto.codigo,
                "nome": produto.nome,
                "quantidade": produto.quantidade,
                "valor": produto.valor
            })
        return produtos

    def buscar_produtos_por_codigo(self, codigo):
        produto = self.repositorio.buscar_produtos_por_codigo(codigo)
        return {
            "codigo": produto.codigo,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor
        }

    def atualizar_produto(self, codigo, nome, quantidade, valor):
        self.repositorio.atualizar_produto(codigo, nome, quantidade, valor)

    def deletar_produto(self, codigo):
        self.repositorio.deletar_produto(codigo)
