
from multiprocessing.sharedctypes import Value
from excecoes.numeroInvalidoException import NumeroInvalidoException
from excecoes.tipoProdutoInvalidoException import TipoProdutoInvalidoException
from limite.telaProduto import TelaProduto
from entidade.produto import Produto


class ControladorProduto:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #aqui define que a relacao eh bidirecional
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

            tipo_produto_valido = dados_produto["tipo_produto"] == "Sorvete"\
                                        or dados_produto["tipo_produto"] == "Bebida"

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
            produto = Produto(dados_produto["codigo_produto"],
                            dados_produto["estoque_produto"],
                            dados_produto["descricao_produto"],
                            dados_produto["tipo_produto"],
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
                    novos_dados_produto = self.__tela_produto.pegar_dados_produto()
                    #ValueError se refere a essa linha

                    numeros_sao_validos = novos_dados_produto["codigo_produto"] >= 0 \
                                            and novos_dados_produto["estoque_produto"] > 0 \
                                            and novos_dados_produto["valor_produto"] >= 0 \
                    
                    if not numeros_sao_validos:
                        raise NumeroInvalidoException

                    tipo_produto_valido = novos_dados_produto["tipo_produto"] == "Sorvete"\
                                                or novos_dados_produto["tipo_produto"] == "Bebida"

                    if not tipo_produto_valido:
                        raise TipoProdutoInvalidoException
                
                except ValueError:
                    self.__tela_produto.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu")
                    self.__tela_produto.mostrar_mensagem("algum tipo errado na insercao de dados.")

                except NumeroInvalidoException:
                        self.__tela_produto.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                                algum numero invalido na insercao dos dados!")

                except TipoProdutoInvalidoException:
                            self.__tela_produto.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                                um tipo de produto invalido na insercao dos dados!")
                
                else:
            
                    produto.codigo = novos_dados_produto["codigo_produto"]
                    produto.estoque = novos_dados_produto["estoque_produto"]
                    produto.descricao = novos_dados_produto["descricao_produto"]
                    produto.tipo_produto = novos_dados_produto["tipo_produto"]
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
                             "tipo_produto": produto.tipo_produto,
                             "valor_produto": produto.valor}

            self.__tela_produto.mostrar_produto(dados_produto)

    def gerar_relatorio_de_vendas(self):
        self.__tela_produto.mostrar_mensagem("")
        self.__tela_produto.mostrar_mensagem("       RELATORIO DE QUANTIDADE DE VENDAS POR PRODUTO")
        ordem_de_vendas = sorted(self.__produtos, key=lambda x: x.numero_de_vendas, reverse=True)
        for produto in ordem_de_vendas:
            
            dados_produto = {"numero_de_vendas_produto": produto.numero_de_vendas,
                             "codigo_produto": produto.codigo,
                             "estoque_produto": produto.estoque,
                             "descricao_produto": produto.descricao,
                             "tipo_produto": produto.tipo_produto,
                             "valor_produto": produto.valor}
            
            self.__tela_produto.mostrar_relatorio(dados_produto)

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_produto, 2: self.excluir_produto,
                  3: self.listar_produtos, 4: self.alterar_produto,
                  5: self.gerar_relatorio_de_vendas}

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