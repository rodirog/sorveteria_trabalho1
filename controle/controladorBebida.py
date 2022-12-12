from multiprocessing.sharedctypes import Value
from excecoes.numeroInvalidoException import NumeroInvalidoException
from excecoes.tipoProdutoInvalidoException import TipoProdutoInvalidoException
from limite.telaBebida import TelaBebida
from entidade.produtoBebida import ProdutoBebida
from persistencia.produto_bebida_dao import ProdutoBebidaDAO



class ControladorBebida:
    def __init__(self):
        self.__tela_bebida = TelaBebida()
        self.__produto_bebida_dao = ProdutoBebidaDAO()

    def incluir_bebida(self):
        try:
            dados_bebida = self.__tela_bebida.pegar_dados_bebida()
            #ValueError se refere a essa linha

            numeros_sao_validos = dados_bebida["codigo_bebida"] >= 0 \
                                    and dados_bebida["estoque_bebida"] > 0 \
                                    and dados_bebida["valor_bebida"] >= 0 \

            if not numeros_sao_validos:
                raise NumeroInvalidoException

        except ValueError:
            self.__tela_bebida.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu \
                                                    algum tipo errado na inserção dos dados!")
        
        except NumeroInvalidoException:
                self.__tela_bebida.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu \
                                                        algum numero invalido na insercao dos dados!")

        else:
            
            bebida = ProdutoBebida(dados_bebida["codigo_bebida"],
                            dados_bebida["estoque_bebida"],
                            dados_bebida["descricao_bebida"],
                            dados_bebida["valor_bebida"])
            
            if not self.encontrar_bebida_pelo_codigo(bebida.codigo):
                self.__tela_bebida.mostrar_mensagem("Bebida inclusa com sucesso!") 
                
                self.__produto_bebida_dao.adicionar(bebida)
            
            else:
                self.__tela_bebida.mostrar_mensagem("Cadastro nao efetuado. \
                                                        Um produto com esse codigo ja existe.")
                

    def encontrar_bebida_pelo_codigo(self, codigo):
        return self.__produto_bebida_dao.encontrar(codigo)

    def alterar_bebida(self):
        self.listar_bebidas()
        
        try:
            codigo_bebida = self.__tela_bebida.selecionar_bebida()
        
        except ValueError:
            self.__tela_bebida.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            
            bebida = self.encontrar_bebida_pelo_codigo(codigo_bebida)

            if(bebida is not None):

                dados_bebida = {"codigo_bebida": bebida.codigo,
                                 "estoque_bebida": bebida.estoque,
                                 "descricao_bebida": bebida.descricao,
                                 "valor_bebida": bebida.valor}
                
                try:
                                        

                    novos_dados_bebida = self.__tela_bebida.alterar_dados_bebida(dados_bebida)
                    #ValueError se refere a essa linha

                    numeros_sao_validos = novos_dados_bebida["codigo_bebida"] >= 0 \
                                            and novos_dados_bebida["estoque_bebida"] > 0 \
                                            and novos_dados_bebida["valor_bebida"] >= 0 \
                    
                    if not numeros_sao_validos:
                        raise NumeroInvalidoException
                
                except ValueError:
                    self.__tela_bebida.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                            algum tipo errado na insercao de dados.")

                except NumeroInvalidoException:
                        self.__tela_bebida.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                                algum numero invalido na insercao dos dados!")
                
                else:
                    self.__produto_bebida_dao.remover(codigo_bebida)
                    
                    bebida.codigo = novos_dados_bebida["codigo_bebida"]
                    bebida.estoque = novos_dados_bebida["estoque_bebida"]
                    bebida.descricao = novos_dados_bebida["descricao_bebida"]
                    bebida.valor = novos_dados_bebida["valor_bebida"]
                
                    
                    self.__produto_bebida_dao.adicionar(bebida)
                    self.__tela_bebida.mostrar_mensagem("Produto alterado com sucesso!")
                    self.listar_bebidas()
            else:
                self.__tela_bebida.mostrar_mensagem("ATENCAO: Produto nao existente")

    def excluir_bebida(self):
        try:
            codigo_bebida = self.__tela_bebida.selecionar_bebida()
        
        except ValueError:
            self.__tela_bebida.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            bebida_encontrado = self.encontrar_bebida_pelo_codigo(codigo_bebida)
            if bebida_encontrado:
                self.__produto_bebida_dao.remover(codigo_bebida)
                self.__tela_bebida.mostrar_mensagem("Produto excluido com sucesso")
            else:
                self.__tela_bebida.mostrar_mensagem("Produto nao encontrado")

    def listar_bebidas(self):
        dados_bebidas = []
        bebidas = self.__produto_bebida_dao.listar()
        
        for bebida in bebidas:
            dados_bebidas.append({"codigo_bebida": bebida.codigo, 
                                  "estoque_bebida": bebida.estoque, 
                                  "descricao_bebida": bebida.descricao, 
                                  "valor_bebida": bebida.valor})

        self.__tela_bebida.mostrar_bebidas(dados_bebidas)

    def gerar_relatorio_de_bebidas(self):
        bebidas = []
        lista_relatorio = []
        bebidas = self.__produto_bebida_dao.listar()

        ordem_de_vendas = sorted(bebidas, key=lambda x: x.quantidade_vendida, reverse=True)
        
        for bebida in ordem_de_vendas:
            
            lista_relatorio.append({"quantidade_vendida_bebida": bebida.quantidade_vendida,
                                    "codigo_bebida": bebida.codigo,
                                    "estoque_bebida": bebida.estoque,
                                    "descricao_bebida": bebida.descricao,
                                    "valor_bebida": bebida.valor})
            
        self.__tela_bebida.mostrar_relatorio_de_bebidas(lista_relatorio)

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_bebida, 2: self.excluir_bebida,
                  3: self.listar_bebidas, 4: self.alterar_bebida,
                  5: self.gerar_relatorio_de_bebidas}
                  
        while True:
            try:
                opcao = self.__tela_bebida.tela_opcoes()
                if opcao == 0:
                    break
                opcoes[opcao]()
            except ValueError:
                self.__tela_produto.mostrar_mensagem("Voce digitou um tipo invalido.")
            except KeyError:
                self.__tela_produto.mostrar_mensagem("Voce digitou um numero invalido.")
    
    @property
    def produto_sorvete_dao(self):
        return self.__produto_sorvete_dao
    
    @property
    def produto_bebida_dao(self):
        return self.__produto_bebida_dao