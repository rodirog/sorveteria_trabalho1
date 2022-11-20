
from multiprocessing.sharedctypes import Value
from excecoes.numeroInvalidoException import NumeroInvalidoException
from excecoes.tipoProdutoInvalidoException import TipoProdutoInvalidoException
from limite.telaProduto import TelaProduto
from entidade.produtoBebida import ProdutoBebida
from entidade.produtoSorvete import ProdutoSorvete


class ControladorProduto:
    def __init__(self):
        self.__tela_produto = TelaProduto()
        self.__produtos = []

    def incluir_produto(self):
        try:
            dados_produto = self.__tela_produto.pegar_dados_produto()
            #ValueError se refere a essa linha

            numeros_sao_validos = dados_produto["codigo_produto"] >= 0 \
                                    and dados_produto["estoque_produto"] > 0 \
                                    and dados_produto["valor_produto"] >= 0 \

            if not numeros_sao_validos:
                raise NumeroInvalidoException

            tipo_produto_valido = dados_produto["tipo_produto"] == 1\
                                        or dados_produto["tipo_produto"] == 2

            if not tipo_produto_valido:
                raise TipoProdutoInvalidoException

        except ValueError:
            self.__tela_produto.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu")
            self.__tela_produto.mostrar_mensagem("algum tipo errado na inserção dos dados!")
        
        except NumeroInvalidoException:
                self.__tela_produto.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu \
                                                        algum numero invalido na insercao dos dados!")
        
        except TipoProdutoInvalidoException:
                self.__tela_produto.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu \
                                                    um tipo de produto invalido na insercao dos dados!")

        else:
            if dados_produto["tipo_produto"] == 1:
                produto = ProdutoSorvete(dados_produto["codigo_produto"],
                                dados_produto["estoque_produto"],
                                dados_produto["descricao_produto"],
                                dados_produto["valor_produto"])
            else:
                produto = ProdutoBebida(dados_produto["codigo_produto"],
                                dados_produto["estoque_produto"],
                                dados_produto["descricao_produto"],
                                dados_produto["valor_produto"])
            
            if not self.encontrar_produto_pelo_codigo(produto.codigo):
                self.__produtos.append(produto)
                self.__tela_produto.mostrar_mensagem("Produto incluso com sucesso!") 
            
            else:
                self.__tela_produto.mostrar_mensagem("Cadastro nao efetuado")
                self.__tela_produto.mostrar_mensagem("Um produto com esse codigo ja existe.")

    def encontrar_produto_pelo_codigo(self, codigo):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto

    def alterar_produto(self):
        self.listar_produtos()
        
        try:
            codigo_produto = self.__tela_produto.selecionar_produto()
        
        except ValueError:
            self.__tela_produto.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            
            produto = self.encontrar_produto_pelo_codigo(codigo_produto)

            if(produto is not None):
                
                try:
                    novos_dados_produto = self.__tela_produto.alterar_dados_produto()
                    #ValueError se refere a essa linha

                    numeros_sao_validos = novos_dados_produto["codigo_produto"] >= 0 \
                                            and novos_dados_produto["estoque_produto"] > 0 \
                                            and novos_dados_produto["valor_produto"] >= 0 \
                    
                    if not numeros_sao_validos:
                        raise NumeroInvalidoException
                
                except ValueError:
                    self.__tela_produto.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu")
                    self.__tela_produto.mostrar_mensagem("algum tipo errado na insercao de dados.")

                except NumeroInvalidoException:
                        self.__tela_produto.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                                algum numero invalido na insercao dos dados!")
                
                else:
            
                    produto.codigo = novos_dados_produto["codigo_produto"]
                    produto.estoque = novos_dados_produto["estoque_produto"]
                    produto.descricao = novos_dados_produto["descricao_produto"]
                    produto.valor = novos_dados_produto["valor_produto"]
                    self.__tela_produto.mostrar_mensagem("Produto alterado com sucesso!")
                    self.listar_produtos()
            else:
                self.__tela_produto.mostrar_mensagem("ATENCAO: Produto nao existente")

    def excluir_produto(self):
        try:
            codigo_produto = self.__tela_produto.selecionar_produto()
        
        except ValueError:
            self.__tela_produto.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            produto_encontrado = self.encontrar_produto_pelo_codigo(codigo_produto)
            if produto_encontrado:
                self.__produtos.remove(produto_encontrado)
                self.__tela_produto.mostrar_mensagem("Produto excluido com sucesso")
            else:
                self.__tela_produto.mostrar_mensagem("Produto nao encontrado")

    def listar_produtos(self):
        for produto in self.__produtos:
            dados_produto = {"codigo_produto": produto.codigo,
                             "estoque_produto": produto.estoque,
                             "descricao_produto": produto.descricao,
                             "tipo_produto": produto.tipo,
                             "valor_produto": produto.valor}

            self.__tela_produto.mostrar_produto(dados_produto)

    def gerar_relatorio_de_sorvetes(self):
        self.__tela_produto.mostrar_mensagem("")
        self.__tela_produto.mostrar_mensagem("       RELATORIO DE PESO VENDIDO POR SORVETE")
        sorvetes = []
        
        for produto in self.__produtos:
            if produto.tipo == 1:
                sorvetes.append(produto)

        ordem_de_vendas = sorted(sorvetes, key=lambda x: x.quantidade_vendida, reverse=True)
        
        for sorvete in ordem_de_vendas:
            
            dados_sorvete = {"quantidade_vendida_produto": sorvete.quantidade_vendida,
                             "codigo_produto": sorvete.codigo,
                             "estoque_produto": sorvete.estoque,
                             "descricao_produto": sorvete.descricao,
                             "valor_produto": sorvete.valor}
            
            self.__tela_produto.mostrar_relatorio_de_sorvetes(dados_sorvete)

    def gerar_relatorio_de_bebidas(self):
        self.__tela_produto.mostrar_mensagem("")
        self.__tela_produto.mostrar_mensagem("       RELATORIO DE QUANTIDADE VENDIDA POR BEBIDA")
        bebidas = []
        
        for produto in self.__produtos:
            if produto.tipo == 2:
                bebidas.append(produto)

        ordem_de_vendas = sorted(bebidas, key=lambda x: x.quantidade_vendida, reverse=True)
        
        for bebida in ordem_de_vendas:
            
            dados_bebida = {"quantidade_vendida_produto": bebida.quantidade_vendida,
                             "codigo_produto": bebida.codigo,
                             "estoque_produto": bebida.estoque,
                             "descricao_produto": bebida.descricao,
                             "valor_produto": bebida.valor}
            
            self.__tela_produto.mostrar_relatorio_de_bebidas(dados_bebida)

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_produto, 2: self.excluir_produto,
                  3: self.listar_produtos, 4: self.alterar_produto,
                  5: self.gerar_relatorio_de_sorvetes,
                  6: self.gerar_relatorio_de_bebidas}

        while True:
            try:
                opcao = self.__tela_produto.mostrar_tela_opcoes()
                if opcao == 0:
                    break
                opcoes[opcao]()
            except ValueError:
                self.__tela_produto.mostrar_mensagem("Voce digitou um tipo invalido.")
            except KeyError:
                self.__tela_produto.mostrar_mensagem("Voce digitou um numero invalido.")