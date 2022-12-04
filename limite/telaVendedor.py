import PySimpleGUI as sg
from limite.componentes.componente_opcoes import ComponenteOpcoes
from limite.componentes.componente_cadastro_vendedor import ComponenteCadastroVendedor

class TelaVendedor:
  def __init__(self, dados_vendedores):
    self.__dados_vendedores = dados_vendedores
    self.__tela_opcoes = self.criar_tela_opcoes()
    self.__tela_dados = self.criar_tela_dados()
    self.__cpf_vendedor_selecionado = None

  def mostrar_tela_opcoes(self, dados_vendedores):
    self.__dados_vendedor = dados_vendedores
    self.__tela_opcoes['-LISTBOX-'].update(values=dados_vendedores)
    self.__tela_opcoes.un_hide()
    opcao = None
    while True:
      event, values = self.__tela_opcoes.read()
      if event == sg.WIN_CLOSED:
        print('window break')
        break
      elif event == 'adicionar':
        opcao = 1
        #self.pegar_dados_cliente()
        break
      elif event == 'editar':
        opcao = 3
        break
      elif event == 'remover':
        opcao = 4
        break
      elif event == 'Exit':
        opcao = 0
        break
    print(opcao)
    self.__tela_opcoes.hide()
    return opcao
    # print("*" * 20)
    # print("VENDEDOR")
    # print("*" * 20)
    # print("1 - Incluir vendedor")
    # print("2 - Listar vendedor")
    # print("3 - Alterar Vendedor")
    # print("4 - Excluir vendedor")
    # print("0 - Voltar")
    # opcao = int(input("Escolha a opcao: "))
    # return opcao

  def criar_tela_opcoes(self):
    return ComponenteOpcoes('vendedores', self.__dados_vendedores).container

  def criar_tela_dados(self):
    return ComponenteCadastroVendedor().container

  def mostrar_vendedores(self, dados_vendedores):
    print("LISTA VENDEDORES")
    for dados_vendedor in dados_vendedores:
      self.__mostrar_vendedor(dados_vendedor)

  def __mostrar_vendedor(self, dados_vendedor):
    codigo_vendedor = dados_vendedor["codigo_vendedor"]
    nome_vendedor = dados_vendedor["nome_vendedor"]
    cpf_vendedor = dados_vendedor["cpf_vendedor"]
    print("/ VENDEDOR")
    print(f"| Codigo: {codigo_vendedor}")
    print(f"| Nome: {nome_vendedor}")
    print(f"| Cpf: {cpf_vendedor}")
    print("\__________________")

  def mostrar_mensagem(self, mensagem):
    print(mensagem)

  def pegar_dados_vendedor(self):
    self.__tela_dados.un_hide()
    vendedor = None
    while True:
      event, values = self.__tela_dados.read()
      if event == 'Submit':
        # print("CADASTRO VENDEDOR")
        # nome_vendedor = input("Nome do vendedor: ")
        # cpf_vendedor = input("Cpf do Vendedor:")
        nome_vendedor = values['-vendedor-nome-']
        cpf_vendedor = values['-vendedor-cpf-']

        try:
          cpf_vendedor = int(cpf_vendedor)
        except ValueError:
          self.mostrar_mensagem('O cpf informado é invalido.')
          continue

        print(nome_vendedor, cpf_vendedor)

        return {"nome_vendedor": nome_vendedor, "cpf_vendedor": cpf_vendedor}

    
        break
      elif event == 'Cancel':
        break

    self.__tela_dados.hide()

    return vendedor

  def selecionar_vendedor(self):
    codigo_vendedor = input(
        "Insira o codigo do vendedor que deseja selecionar: ")
    return codigo_vendedor
