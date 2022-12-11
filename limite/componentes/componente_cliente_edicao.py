

import PySimpleGUI as sg


class ComponenteClienteEdicao:
  def __init__(self, cliente_dto):
    sg.ChangeLookAndFeel('DarkTeal4')
    cliente_edicao_layout = [
      [sg.Text("Editar cliente")],
      [sg.Text('Nome:', size=(7,1)), sg.InputText(cliente_dto.nome, key='it_edicao_cliente_nome', size=(25,1), do_not_clear=True)],
      [sg.Text('Cpf:', size=(7,1)), sg.InputText(cliente_dto.cpf, size=(25,1), do_not_clear=True, disabled=True)],
      [sg.Text('Email:', size=(7,1)), sg.InputText(cliente_dto.email, key='it_edicao_cliente_email', size=(25,1), do_not_clear=True)],
      [sg.Text('Telefone:', size=(7,1)), sg.InputText(cliente_dto.telefone, key='it_edicao_cliente_telefone', size=(25,1), do_not_clear=True)],

      [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('Sistema de Clientes', cliente_edicao_layout, finalize=True)

  @property
  def container(self):
    return self.__container
