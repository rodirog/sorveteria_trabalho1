from limite.telaProduto import TelaProduto
from entidade.produto import Produto


class ControladorProduto:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #aqui define que a relacao eh bidirecional
        self.__tela_produto = TelaProduto()
        self.__produtos = []

    def inclui_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        produto = Produto(dados_produto["codigo_produto"],
                          dados_produto["quantidade_produto"],
                          dados_produto["descricao_produto"])
        if not self.retorna_produto_pelo_codigo(produto.codigo):
            self.__produtos.append(produto)

    def retorna_produto_pelo_codigo(self, codigo):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto

    def altera_produto(self):
        pass

    def exclui_produto(self):
        pass

    def lista_produto(self):
        for produto in self.__produtos:
            dados_produto = {"codigo_produto": produto.codigo,
                             "quantidade_produto": produto.quantidade,
                             "descricao_produto": produto.descricao}

            self.__tela_produto.mostra_produto(dados_produto)

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inclui_produto, 2: self.exclui_produto,
                  3:self.lista_produto, 4: self.altera_produto}

        while True:
            opcao = self.__tela_produto.mostra_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
