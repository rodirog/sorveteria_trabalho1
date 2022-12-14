from excecoes.clienteNaoExisteException import ClienteNaoExisteException
from excecoes.notaFiscalNaoExisteException import NotaFiscalNaoExisteException
from excecoes.pesoInvalidoException import PesoInvalidoException
from excecoes.posicaoItemInvalidaException import PosicaoItemInvalidaException
from excecoes.produtoNaoExisteException import ProdutoNaoExisteException
from excecoes.quantidadeInvalidaException import QuantidadeInvalidoException
from excecoes.vendedorNaoExisteException import VendedorNaoExisteException
from excecoes.estoqueVazioException import EstoqueVazioException
from limite.telaNotaFiscal import TelaNotaFiscal
from entidade.notaFiscal import NotaFiscal
from persistencia.nota_fiscal_dao import NotaFiscalDAO


class ControladorNotaFiscal:
    def __init__(self, controlador_cliente, controlador_vendedor, controlador_sorvete, controlador_bebida):
        self.__controlador_cliente = controlador_cliente
        self.__controlador_vendedor = controlador_vendedor
        self.__controlador_sorvete = controlador_sorvete
        self.__controlador_bebida = controlador_bebida
        self.__tela_nota_fiscal = TelaNotaFiscal()
        self.__nota_fiscal_dao = NotaFiscalDAO()
        self.__nota_fiscal_atual = None

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

        numero_nota = 1
        
        notas = self.__nota_fiscal_dao.listar()
        if len(notas) > 0:
            ultima_nota = notas[-1]
            numero_nota = ultima_nota.numero + 1
                #ve o numero da ultima nota da lista e adiciona 1
                
        nota_fiscal = NotaFiscal(
            numero_nota, cliente_encontrado, vendedor_encontrado)

        self.__nota_fiscal_atual = nota_fiscal

        self.__mostrar_tela_item_opcoes()
        
        self.gerar_relatorio_da_nota(nota_fiscal)
        self.__nota_fiscal_dao.adicionar(nota_fiscal)
        self.__tela_nota_fiscal.mostrar_mensagem(
            "A nota fiscal foi cadastrada com sucesso!")

    def gerar_relatorio_da_nota(self, nota_fiscal):

        dados_itens = []
        i=0
        for item in nota_fiscal.itens_da_nota:
            dados_itens.append({
                "numero_item": i,
                "codigo_produto": item.produto.codigo,
                "descricao_produto": item.produto.descricao,
                "qtd_item": item.quantidade,
                "valor_item": item.produto.valor,
                "total_item": item.produto.calcular_preco_item(item.quantidade)})
            i = i+1

        dados_nota_fiscal = {
            "numero_nota": nota_fiscal.numero,
            "nome_cliente_nota": nota_fiscal.cliente.nome,
            "nome_vendedor_nota": nota_fiscal.vendedor.nome,
            "valor_total_nota": nota_fiscal.valor_total,
            "data_nota": nota_fiscal.datetime.strftime("%d/%m/%Y %H:%M:%S"),
            "itens_nota": nota_fiscal.itens_da_nota}

        self.__tela_nota_fiscal.mostrar_relatorio_da_nota(dados_nota_fiscal, dados_itens)

    def excluir_nota_fiscal(self):
        numero_nota = int(self.__tela_nota_fiscal.selecionar_nota_fiscal())
        nota_fiscal_encontrada = self.encontrar_nota_fiscal(numero_nota)
        if not nota_fiscal_encontrada:
            raise NotaFiscalNaoExisteException

        self.__nota_fiscal_dao.remover(numero_nota)
        self.__tela_nota_fiscal.mostrar_mensagem(
            "A nota fiscal foi removida com sucesso!")

    def encontrar_nota_fiscal(self, numero_nota):
        return self.__nota_fiscal_dao.encontrar(numero_nota)

    def listar_notas(self):
        dados_notas = []
        notas = self.__nota_fiscal_dao.listar()

        for nota in notas:

            dados_notas.append({"numero_nota": nota.numero, 
                                  "nome_cliente_nota": nota.cliente.nome, 
                                  "nome_vendedor_nota": nota.vendedor.nome, 
                                  "valor_total_nota": nota.valor_total, 
                                  "data_nota": nota.datetime.strftime("%d/%m/%Y %H:%M:%S")})

        self.__tela_nota_fiscal.mostrar_notas(dados_notas)

    def adicionar_item_nota_fiscal(self):
        dados_item_nota = self.__tela_nota_fiscal.pegar_dados_item_nota()
        eh_sorvete = dados_item_nota["rd_sorvete"]
        codigo_produto = int(dados_item_nota["it_codigo_produto_item_nota"])
        if eh_sorvete:
            produto_encontrado = self.encontrar_sorvete(codigo_produto)
        else:
            produto_encontrado = self.encontrar_bebida(codigo_produto)
        if not produto_encontrado:
            raise ProdutoNaoExisteException

        if eh_sorvete:
            quantidade_item = dados_item_nota["it_quantidade_item_nota"]
            if not self.__eh_peso_valido(quantidade_item):
                raise PesoInvalidoException
            quantidade_item = float(quantidade_item)
            
        else:
            quantidade_item = dados_item_nota["it_quantidade_item_nota"]
            if not self.__eh_quantidade_valida(quantidade_item):
                raise QuantidadeInvalidoException
            quantidade_item = int(quantidade_item)
        
        dados_item_nota = {
            "produto_item": produto_encontrado,
            "quantidade_item": quantidade_item,
        }

        self.__nota_fiscal_atual.adicionar_item_nota_fiscal(dados_item_nota)
        if eh_sorvete:
            self.__controlador_sorvete.produto_sorvete_dao.remover(codigo_produto)
            self.__controlador_sorvete.produto_sorvete_dao.adicionar(produto_encontrado)
        else:
            self.__controlador_bebida.produto_bebida_dao.remover(codigo_produto)
            self.__controlador_bebida.produto_bebida_dao.adicionar(produto_encontrado)
        self.__tela_nota_fiscal.mostrar_mensagem(
            "O item foi adicionado com sucesso!")

    def excluir_item_nota_fiscal(self):
        posicao_item = int(self.__tela_nota_fiscal.selecionar_item_nota())
        if not self.__eh_posicao_item_nota_valida(posicao_item):
            raise PosicaoItemInvalidaException

        item_excluido = self.__nota_fiscal_atual.itens_da_nota[posicao_item]
        quantidade_retornada = item_excluido.quantidade
        item_excluido.produto.retornar_ao_estoque(quantidade_retornada)

        self.__nota_fiscal_atual.excluir_item_nota_fiscal(posicao_item)

        if item_excluido.produto.tipo == 1:
            self.__controlador_sorvete.produto_sorvete_dao.remover(item_excluido.produto.codigo)
            self.__controlador_sorvete.produto_sorvete_dao.adicionar(item_excluido.produto)
        else:
            self.__controlador_bebida.produto_bebida_dao.remover(item_excluido.produto.codigo)
            self.__controlador_bebida.produto_bebida_dao.adicionar(item_excluido.produto)
        
        self.__tela_nota_fiscal.mostrar_mensagem(
            "O item da nota fiscal foi removido com sucesso!")

    def listar_itens_nota(self):
        dados_itens = []
        i=0
        for item in self.__nota_fiscal_atual.itens_da_nota:
        
            dados_itens.append({"numero_item": i,
                                "codigo_produto": item.produto.codigo,
                                "descricao_produto": item.produto.descricao,
                                "qtd_item": item.quantidade,
                                })
            i = i+1

        self.__tela_nota_fiscal.mostrar_itens_nota(dados_itens)

    def gerar_nota(self):
        self.__nota_fiscal_atual.gerar_nota()
        self.__nota_fiscal_atual = None

    def encontrar_cliente(self, cpf_cliente):
        return self.__controlador_cliente.encontrar_cliente(cpf_cliente)

    def encontrar_vendedor(self, codigo_vendedor):
        return self.__controlador_vendedor.encontrar_vendedor(codigo_vendedor)

    def encontrar_sorvete(self, codigo_produto):
        return self.__controlador_sorvete.encontrar_sorvete_pelo_codigo(codigo_produto)

    def encontrar_bebida(self, codigo_produto):
        return self.__controlador_bebida.encontrar_bebida_pelo_codigo(codigo_produto)

    def mostrar_tela_opcoes(self):
        if self.__nota_fiscal_atual:
            self.__mostrar_tela_item_opcoes()

        opcoes = {
            1: self.adicionar_nota_fiscal,
            2: self.listar_notas,
            3: self.excluir_nota_fiscal
        }

        while True:
            opcao = self.__tela_nota_fiscal.tela_notas_opcoes()

            try:
                opcoes[opcao]()
            except (ClienteNaoExisteException, VendedorNaoExisteException, NotaFiscalNaoExisteException) as err:
                self.__tela_nota_fiscal.mostrar_mensagem(
                    f"Erro: {err.args[0]}")

    def __mostrar_tela_item_opcoes(self):
        opcoes = {
            1: self.adicionar_item_nota_fiscal,
            2: self.excluir_item_nota_fiscal,
            3: self.listar_itens_nota,
            4: self.gerar_nota
        }

        while self.__nota_fiscal_atual:
            opcao = self.__tela_nota_fiscal.tela_itens_opcoes()

            # if opcao == 0:
            #     break

            try:
                opcoes[opcao]()
            except (ProdutoNaoExisteException, QuantidadeInvalidoException, PesoInvalidoException, PosicaoItemInvalidaException, EstoqueVazioException) as err:
                self.__tela_nota_fiscal.mostrar_mensagem(
                    f"Erro: {err.args[0]}")

    def __eh_quantidade_valida(self, quantidade_item):
        return quantidade_item.isdigit()

    def __eh_peso_valido(self, peso_item):
        dot_amount = peso_item.count(".")
        if dot_amount > 1:
            return False
        elif dot_amount == 1:
            integer, decimal = peso_item.split(".")
            return integer.isdigit() and decimal.isdigit()
        else:
            return peso_item.isdigit()

    def __eh_posicao_item_nota_valida(self, posicao_item):
        quantidade_itens_nota = len(self.__nota_fiscal_atual.itens_da_nota)
        return quantidade_itens_nota > 0 and posicao_item >= 0 and posicao_item < quantidade_itens_nota
