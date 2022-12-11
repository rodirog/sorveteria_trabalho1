from multiprocessing.sharedctypes import Value
from excecoes.numeroInvalidoException import NumeroInvalidoException
from excecoes.tipoProdutoInvalidoException import TipoProdutoInvalidoException
from limite.telaSorvete import TelaSorvete
from entidade.produtoSorvete import ProdutoSorvete
from persistencia.produto_sorvete_dao import ProdutoSorveteDAO



class ControladorSorvete:
    def __init__(self):
        self.__tela_sorvete = TelaSorvete()
        self.__produto_sorvete_dao = ProdutoSorveteDAO()

    def incluir_sorvete(self):
        try:
            dados_sorvete = self.__tela_sorvete.pegar_dados_sorvete()

            numeros_sao_validos = dados_sorvete["codigo_sorvete"] >= 0 \
                                    and dados_sorvete["estoque_sorvete"] > 0 \
                                    and dados_sorvete["valor_sorvete"] >= 0 \

            if not numeros_sao_validos:
                raise NumeroInvalidoException

        except ValueError:
            self.__tela_sorvete.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu")
            self.__tela_sorvete.mostrar_mensagem("algum tipo errado na inserção dos dados!")
        
        except NumeroInvalidoException:
                self.__tela_sorvete.mostrar_mensagem("Cadastro nao efetuado. Voce inseriu \
                                                        algum numero invalido na insercao dos dados!")

        else:
            
            sorvete = ProdutoSorvete(dados_sorvete["codigo_sorvete"],
                            dados_sorvete["estoque_sorvete"],
                            dados_sorvete["descricao_sorvete"],
                            dados_sorvete["valor_sorvete"])
            
            if not self.encontrar_sorvete_pelo_codigo(sorvete.codigo):
                # self.__produtos.append(produto)
                self.__tela_sorvete.mostrar_mensagem("Sorvete incluso com sucesso!") 
                
                self.__produto_sorvete_dao.adicionar(sorvete)
            
            else:
                self.__tela_sorvete.mostrar_mensagem("Cadastro nao efetuado")
                self.__tela_sorvete.mostrar_mensagem("Um produto com esse codigo ja existe.")

    def encontrar_sorvete_pelo_codigo(self, codigo):
        return self.__produto_sorvete_dao.encontrar(codigo)

    def alterar_sorvete(self):
        self.listar_sorvetes()
        
        try:
            codigo_sorvete = self.__tela_sorvete.selecionar_sorvete()
        
        except ValueError:
            self.__tela_sorvete.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            
            sorvete = self.encontrar_sorvete_pelo_codigo(codigo_sorvete)

            if(sorvete is not None):

                dados_sorvete = {"codigo_sorvete": sorvete.codigo,
                                 "estoque_sorvete": sorvete.estoque,
                                 "descricao_sorvete": sorvete.descricao,
                                 "valor_sorvete": sorvete.valor}
                
                try:
                                        

                    novos_dados_sorvete = self.__tela_sorvete.alterar_dados_sorvete(dados_sorvete)
                    #ValueError se refere a essa linha

                    numeros_sao_validos = novos_dados_sorvete["codigo_sorvete"] >= 0 \
                                            and novos_dados_sorvete["estoque_sorvete"] > 0 \
                                            and novos_dados_sorvete["valor_sorvete"] >= 0 \
                    
                    if not numeros_sao_validos:
                        raise NumeroInvalidoException
                
                except ValueError:
                    self.__tela_sorvete.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu")
                    self.__tela_sorvete.mostrar_mensagem("algum tipo errado na insercao de dados.")

                except NumeroInvalidoException:
                        self.__tela_sorvete.mostrar_mensagem("Alteracao nao efetuada. Voce inseriu \
                                                                algum numero invalido na insercao dos dados!")
                
                else:
                    self.__produto_sorvete_dao.remover(codigo_sorvete)
                    
                    sorvete.codigo = novos_dados_sorvete["codigo_sorvete"]
                    sorvete.estoque = novos_dados_sorvete["estoque_sorvete"]
                    sorvete.descricao = novos_dados_sorvete["descricao_sorvete"]
                    sorvete.valor = novos_dados_sorvete["valor_sorvete"]
                
                    
                    self.__produto_sorvete_dao.adicionar(sorvete)
                    self.__tela_sorvete.mostrar_mensagem("Produto alterado com sucesso!")
                    self.listar_sorvetes()
            else:
                self.__tela_sorvete.mostrar_mensagem("ATENCAO: Produto nao existente")

    def excluir_sorvete(self):
        try:
            codigo_sorvete = self.__tela_sorvete.selecionar_sorvete()
        
        except ValueError:
            self.__tela_sorvete.mostrar_mensagem("Voce nao inseriu um numero! Tente novamente.")
        
        else:
            sorvete_encontrado = self.encontrar_sorvete_pelo_codigo(codigo_sorvete)
            if sorvete_encontrado:
                # self.__produtos.remove(produto_encontrado)
                self.__produto_sorvete_dao.remover(codigo_sorvete)
                self.__tela_sorvete.mostrar_mensagem("Produto excluido com sucesso")
            else:
                self.__tela_sorvete.mostrar_mensagem("Produto nao encontrado")

    def listar_sorvetes(self):
        dados_sorvetes = []
        sorvetes = self.__produto_sorvete_dao.listar()
        
        for sorvete in sorvetes:
            dados_sorvetes.append({"codigo_sorvete": sorvete.codigo, 
                                  "estoque_sorvete": sorvete.estoque, 
                                  "descricao_sorvete": sorvete.descricao, 
                                  "valor_sorvete": sorvete.valor})

        self.__tela_sorvete.mostrar_sorvetes(dados_sorvetes)

    def gerar_relatorio_de_sorvetes(self):
        sorvetes = []
        lista_relatorio = []
        sorvetes = self.__produto_sorvete_dao.listar()

        ordem_de_vendas = sorted(sorvetes, key=lambda x: x.quantidade_vendida, reverse=True)
        
        for sorvete in ordem_de_vendas:
            
            lista_relatorio.append({"quantidade_vendida_sorvete": sorvete.quantidade_vendida,
                                    "codigo_sorvete": sorvete.codigo,
                                    "estoque_sorvete": sorvete.estoque,
                                    "descricao_sorvete": sorvete.descricao,
                                    "valor_sorvete": sorvete.valor})
            
        self.__tela_sorvete.mostrar_relatorio_de_sorvetes(lista_relatorio)

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_sorvete, 2: self.excluir_sorvete,
                  3: self.listar_sorvetes, 4: self.alterar_sorvete,
                  5: self.gerar_relatorio_de_sorvetes}
                  
        while True:
            try:
                opcao = self.__tela_sorvete.tela_opcoes()
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