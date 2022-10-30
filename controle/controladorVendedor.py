from excecoes.vendedorJahExisteException import VendedorJahExisteException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from limite.telaVendedor import TelaVendedor
from entidade.vendedor import Vendedor


class ControladorVendedor:
    def __init__(self, controlador_principal):
        #self.__controlador_principal = controlador_principal
        self.__tela_vendedor = TelaVendedor()
        self.__vendedores = []

    def adicionar_vendedor(self):
        dados_vendedor = self.__tela_vendedor.pegar_dados_vendedor()
        codigo_vendedor = dados_vendedor["codigo_vendedor"]
        if self.__encontrar_vendedor(codigo_vendedor):
            raise VendedorJahExisteException

        vendedor = Vendedor(dados_vendedor["nome_vendedor"],
                            dados_vendedor["codigo_vendedor"])

        self.__vendedores.append(vendedor)
        self.__tela_vendedor.mostrar_mensagem(
            "O Vendedor foi cadastrado com sucesso!")

    def excluir_vendedor(self):
        codigo_vendedor = self.__tela_vendedor.pegar_codigo_vendedor()
        vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
        if not vendedor_encontrado:
            raise VendedorJahExisteException

        self.__vendedores.remove(vendedor_encontrado)
        self.__tela_vendedor.mostrar_mensagem(
            "O vendedor foi removido com sucesso!")

    def encontrar_vendedor(self, codigo_vendedor: int):
        for vendedor in self.__vendedores:
            if vendedor.codigo_vendedor == codigo_vendedor:
                return vendedor

    def alterar_vendedor(self):
        codigo_vendedor = self.__tela_vendedor.pegar_codigo_vendedor()
        vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
        if not vendedor_encontrado:
            raise VendedorNaoExisteException

        dados_vendedor = self.__tela_vendedor.pegar_dados_vendedor()
        nome_vendedor = dados_vendedor["nome_vendedor"]
        cpf_vendedor = dados_vendedor["cpf_vendedor"]
        codigo_vendedor = dados_vendedor["codigo_vendedor"]

        vendedor_encontrado.nome = nome_vendedor
        vendedor_encontrado.cpf = cpf_vendedor
        codigo_vendedor.codigo_vendedor = codigo_vendedor

        self.__tela_vendedor.mostrar_mensagem(
            "O vendedor foi alterado com sucesso!")

    def listar_vendedor(self):
        print("listar_vendedor")
        dados_vendedor = []
        for vendedor in self.__vendedor:
            dados_vendedor = {
                "codigo_vendedor": vendedor.telefone,
                "nome_vendedor": vendedor.nome
            }
            dados_vendedor.append(dados_vendedor)

        self.__tela_vendedor.mostrar_vendedor(dados_vendedor)

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_vendedor,
            2: self.excluir_vendedor,
            3: self.encontrar_vendedor,
            4: self.listar_vendedor,
            5: self.alterar_vendedor
        }

        while True:
            opcao = self.__tela_vendedor.mostrar_tela_opcoes()

            if opcao == 0:
                break

            try:
                opcoes[opcao]()
            except VendedorJahExisteException:
                self.__tela_vendedor.mostrar_mensagem("O vendedor já existe!")
            except VendedorNaoExisteException:
                self.__tela_vendedor.mostrar_mensagem("O vendedor não existe!")
