import PySimpleGUI as sg

from limite.componentes.componente_cadastro_cliente import ComponenteCadastroCliente
from limite.componentes.componente_edicao import ComponenteEdicao
from limite.componentes.componente_exclusao import ComponenteExclusao
from limite.componentes.item_lista import ItemLista
from limite.componentes.componente_opcoes import ComponenteOpcoes

class TelaCliente:
  def __init__(self, dados_clientes):
    self.__dados_clientes = dados_clientes
    self.__tela_opcoes = self.criar_tela_opcoes()
    self.__tela_dados = self.criar_tela_dados()
    self.__cpf_cliente_selecionado = None

  def mostrar_tela_opcoes(self, dados_clientes):
    self.__dados_clientes = dados_clientes
    self.__tela_opcoes['-LISTBOX-'].update(values=dados_clientes)
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

  def criar_tela_opcoes(self):
    return ComponenteOpcoes('clientes', self.__dados_clientes).container

  def criar_tela_dados(self):
    return ComponenteCadastroCliente().container

  def mostrar_clientes(self, dados_clientes):
    print("LISTA CLIENTES")
    for dados_cliente in dados_clientes:
      self.__mostrar_cliente(dados_cliente)

  def __mostrar_cliente(self, dados_cliente):
    nome_cliente = dados_cliente["nome_cliente"]
    cpf_cliente = dados_cliente["cpf_cliente"]
    email_cliente = dados_cliente["email_cliente"]
    telefone_cliente = dados_cliente["telefone_cliente"]
    print("/ CLIENTE")
    print(f"| Nome: {nome_cliente}")
    print(f"| Cpf: {cpf_cliente}")
    print(f"| Email: {email_cliente}")
    print(f"| Fone: {telefone_cliente}")
    print("\__________________")

  def mostrar_mensagem(self, mensagem):
    print(mensagem)

  def pegar_dados_cliente(self):
    self.__tela_dados.un_hide()
    cliente = None
    while True:
      event, values = self.__tela_dados.read()
      if event == 'Submit':
        # nome = values['-cliente-nome-']
        # cpf = values['-cliente-cpf-']
        # item = ItemLista(nome, cpf)
        # clientes.append(item)
        # window_main['-LISTBOX-'].update(values=clientes)

        nome_cliente = values['-cliente-nome-']
        telefone_cliente = values['-cliente-telefone-']
        email_cliente = values['-cliente-email-']
        cpf_cliente = int(values['-cliente-cpf-'])

        cliente = {"nome_cliente": nome_cliente, "telefone_cliente": telefone_cliente, "email_cliente": email_cliente, "cpf_cliente": cpf_cliente}

        break
      elif event == 'Cancel':
        break

    self.__tela_dados.hide()

    return cliente

  def selecionar_cliente(self):
    return self.__cpf_cliente_selecionado
