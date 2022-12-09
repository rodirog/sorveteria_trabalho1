

import PySimpleGUI as sg


class ComponenteClienteEdicao:
  def __init__(self, cliente_dto):
    sg.ChangeLookAndFeel('DarkTeal4')
    cliente_edicao_layout = [
      [sg.Text("Editar cliente")],
      [sg.Text('Nome:', size=(7,1)), sg.InputText(cliente_dto.nome, key='it_edicao_cliente_nome', size=(25,1), do_not_clear=False)],
      [sg.Text('email:', size=(7,1)), sg.InputText(cliente_dto.email, key='it_edicao_cliente_email', size=(25,1), do_not_clear=False)],
      [sg.Text('telefone:', size=(7,1)), sg.InputText(cliente_dto.telefone, key='it_edicao_cliente_telefone', size=(25,1), do_not_clear=False)],

      [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('Sistema de Clientes', cliente_edicao_layout, finalize=True)

  @property
  def container(self):
    return self.__container
