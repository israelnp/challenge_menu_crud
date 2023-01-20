from produto import Produto


class ProdutoRepositorio:

    def inserir_produto(self, codigo, nome, quantidade, valor):
        produto = Produto(codigo=codigo, nome=nome,
                          quantidade=quantidade, valor=valor)
        produto.save()

    def buscar_produtos(self):
        return Produto.select()

    def buscar_produtos_por_codigo(self, codigo):
        return Produto.get(Produto.codigo == codigo)

    def atualizar_produto(self, codigo, nome, quantidade, valor):
        produto = Produto.select().where(Produto.codigo == codigo).get()
        produto.nome = nome
        produto.quantidade = quantidade
        produto.valor = valor
        produto.save()

    def deletar_produto(self, codigo):
        produto = Produto.get(Produto.codigo == codigo)
        produto.delete_instance()
