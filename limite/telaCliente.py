import PySimpleGUI as sg
from dtos.cliente_dto import ClienteDto
from limite.componentes.componente_cliente_edicao import ComponenteClienteEdicao

from limite.componentes.componente_cadastro_cliente import ComponenteCadastroCliente
from limite.componentes.componente_cliente_selecao import ComponenteClienteSelecao
from limite.componentes.componente_cliente_exclusao import ComponenteClienteExclusao
from limite.componentes.componente_listagem import ComponenteListagem
from limite.componentes.item_lista import ItemLista
from limite.componentes.componente_opcoes import ComponenteOpcoes

class TelaCliente:
  def __init__(self):
    self.__window = self.criar_tela_opcoes()
    # self.__dados_clientes = dados_clientes
    
    # self.__tela_opcoes = self.criar_tela_opcoes()
    # self.__tela_dados = self.criar_tela_dados()
    self.__cpf_cliente_selecionado = None

  def mostrar_tela_opcoes(self):
    # self.__dados_clientes = dados_clientes(values=dados_clientes)
    self.__window = self.criar_tela_opcoes()
    opcao = None
    # while True:
    button, values = self.open()
    #   if event == sg.WIN_CLOSED:
    #     break
    if values['1']:
      opcao = 1
      #self.pegar_dados_cliente()
    elif values['2']:
      opcao = 2
    elif values['3']:
      opcao = 3
    elif values['4']:
      opcao = 4
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def criar_tela_opcoes(self):
    return ComponenteOpcoes('clientes').container

  def criar_tela_dados(self):
    return ComponenteCadastroCliente().container

  def criar_tela_listagem(self, dados_clientes):
    return ComponenteListagem('clientes', dados_clientes).container

  def criar_tela_selecao(self):
    return ComponenteClienteSelecao().container

  def criar_tela_edicao(self, cliente_dto):
    return ComponenteClienteEdicao(cliente_dto).container

  def mostrar_clientes(self, dados_clientes):
    self.__window = self.criar_tela_listagem(dados_clientes)

    button, _ = self.open()
    while True:
      if button in (sg.WIN_CLOSED, 'Voltar'):
        break

    self.close()

  def mostrar_mensagem(self, mensagem):
    sg.popup("", mensagem)

  def pegar_dados_cliente(self):
    self.__window = self.criar_tela_dados()
    while True:
      try:
        cliente = self.pegar_cliente()
        self.close()

        return cliente
      except ValueError:
        self.mostrar_mensagem('Dado invalido!')

  def pegar_cliente(self):
    _, values = self.open()

    nome = values['it_cadasto_cliente_nome']
    cpf = int(values['it_cadasto_cliente_cpf'])
    email = values['it_cadasto_cliente_email']
    telefone = values['it_cadasto_cliente_telefone']

    cliente_dto = ClienteDto(nome, email, telefone, cpf)

    return cliente_dto

  def selecionar_cliente(self):
    self.__window = self.criar_tela_selecao()
    while True:
      try:
        _, values = self.open()
        cpf_cliente = int(values['it_selecao_cliente_cpf'])

        self.close()

        return cpf_cliente
      except ValueError:
        self.mostrar_mensagem('Dado invalido!')

  def alterar_dados_cliente(self, cliente_dto):
    self.__window = self.criar_tela_edicao(cliente_dto)
    while True:
      try:
        cliente = self.alterar_cliente()
        self.close()

        return cliente
      except ValueError:
        self.mostrar_mensagem('Dado invalido!')

  def alterar_cliente(self):
    _, values = self.open()

    nome = values['it_edicao_cliente_nome']
    telefone = values['it_edicao_cliente_telefone']
    email = values['it_edicao_cliente_email']

    cliente_dto = ClienteDto(nome, email, telefone)

    return cliente_dto

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values