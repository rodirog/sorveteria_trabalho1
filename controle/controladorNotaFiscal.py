from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.notaFiscalNaoExisteException import NotaFiscalNaoExisteException
from excecoes.pesoInvalidoException import PesoInvalidoException
from excecoes.produtoNaoExisteException import ProdutoNaoExisteException
from excecoes.quantidadeInvalidaException import QuantidadeInvalidoException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from limite.telaNotaFiscal import TelaNotaFiscal
from entidade.notaFiscal import NotaFiscal


class ControladorNotaFiscal:
    def __init__(self, controlador_principal, controlador_cliente, controlador_vendedor, controlador_produto):
        #self.__controlador_principal = controlador_principal
        self.__controlador_cliente = controlador_cliente
        self.__controlador_vendedor = controlador_vendedor
        self.__controlador_produto = controlador_produto
        self.__tela_nota_fiscal = TelaNotaFiscal()
        self.__notas_fiscais = []
        self.__nota_fiscal_atual = None
        self.__numero = 1

    def adicionar_nota_fiscal(self):
        dados_nota = self.__tela_nota_fiscal.pegar_dados_nota()

        cpf_cliente = int(dados_nota["cpf_cliente"])
        cliente_encontrado = self.encontrar_cliente(cpf_cliente)
        if not cliente_encontrado:
            raise ClienteNaoExisteException

        codigo_vendedor = int(dados_nota["codigo_vendedor"])
        vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
        if not vendedor_encontrado:
            raise VendedorNaoExisteException

        numero_nota = self.__numero

        self.__numero += 1

        nota_fiscal = NotaFiscal(
            numero_nota, cliente_encontrado, vendedor_encontrado)

        self.__notas_fiscais.append(nota_fiscal)
        self.__nota_fiscal_atual = nota_fiscal
        self.__tela_nota_fiscal.mostrar_mensagem(
            "A nota fiscal foi cadastrada com sucesso!")

    def excluir_nota_fiscal(self):
        numero_nota = int(self.__tela_vendedor.selecionar_nota_fiscal())
        nota_fiscal_encontrada = self.encontrar_nota_fiscal(numero_nota)
        if not nota_fiscal_encontrada:
            raise NotaFiscalNaoExisteException

        self.__notas_fiscais.remove(nota_fiscal_encontrada)
        self.__tela_nota_fiscal.mostrar_mensagem(
            "A nota fiscal foi removida com sucesso!")

    def encontrar_nota_fiscal(self, numero_nota):
        for nota_fiscal in self.__notas_fiscais:
            if nota_fiscal.numero == numero_nota:
                return nota_fiscal

    def listar_nota_fiscal(self):
        dados_notas_fiscais = []
        for nota_fiscal in self.__notas_fiscais:
            dados_nota_fiscal = {
                "numero_nota": nota_fiscal.numero,
                "cliente_nota": nota_fiscal.cliente,
                "vendedor_nota": nota_fiscal.vendedor,
                "valor_total_nota": nota_fiscal.valor_total,
                "data_nota": nota_fiscal.data
            }
            dados_notas_fiscais.append(dados_nota_fiscal)

        self.__tela_nota_fiscal.mostrar_notas(dados_notas_fiscais)

    def adicionar_item_nota_fiscal(self):
        dados_item_nota = self.__tela_nota_fiscal.pegar_dados_item_nota()

        codigo_produto = dados_item_nota["codigo_produto_item_nota"]
        produto_encontrado = self.encontrar_produto(codigo_produto)
        if not produto_encontrado:
            raise ProdutoNaoExisteException

        quantidade_item = dados_item_nota["quantidade_item_nota"]
        if not self.eh_quantidade_valida(quantidade_item):
            raise QuantidadeInvalidoException
        quantidade_item = int(quantidade_item)

        peso_item = dados_item_nota["peso_item_nota"]
        if not self.eh_peso_valido(peso_item):
            raise PesoInvalidoException
        peso_item = float(peso_item)

        dados_item_nota = {
            "produto_item": produto_encontrado,
            "quantidade_item": quantidade_item,
            "peso_item": peso_item
        }

        self.__nota_fiscal_atual.adicionar_item_nota_fiscal(dados_item_nota)
        self.__tela_nota_fiscal.mostrar_mensagem(
            "O item foi adicionado com sucesso!")

    def excluir_item_nota_fiscal(self):
        codigo_vendedor = int(self.__tela_vendedor.selecionar_vendedor())
        vendedor_encontrado = self.encontrar_vendedor(codigo_vendedor)
        if not vendedor_encontrado:
            raise VendedorNaoExisteException

        self.__vendedores.remove(vendedor_encontrado)
        self.__tela_vendedor.mostrar_mensagem(
            "O vendedor foi removido com sucesso!")

    def encontrar_cliente(self, cpf_cliente):
        return self.__controlador_cliente.encontrar_cliente(cpf_cliente)

    def encontrar_vendedor(self, codigo_vendedor):
        return self.__controlador_vendedor.encontrar_vendedor(codigo_vendedor)

    def encontrar_produto(self, codigo_produto):
        return self.__controlador_produto.encontrar_produto_pelo_codigo(codigo_produto)

    def mostrar_tela_opcoes(self):
        opcoes = {
            1: self.adicionar_item_nota_fiscal,
            2: self.excluir_item_nota_fiscal,
            2: self.excluir_item_nota_fiscal,
            3: self.encontrar_nota_fiscal
        }

        while True:
            opcao = self.__tela_vendedor.mostrar_tela_opcoes()

            if opcao == 0:
                break

            try:
                opcoes[opcao]()
            except (VendedorJahExisteException, VendedorNaoExisteException, NomeInvalidoException, CpfInvalidoException) as err:
                self.__tela_vendedor.mostrar_mensagem(f"Erro: {err.args[0]}")

    def eh_quantidade_valida(self, quantidade_item):
        return quantidade_item.isdigit()

    def eh_peso_valido(self, peso_item):
        return peso_item.isdigit()
