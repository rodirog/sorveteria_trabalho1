import PySimpleGUI as sg


class ComponenteCadastroCliente:
  def __init__(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    cliente_add_layout = [
      [sg.Text("Incluir novo cliente")],
      [sg.Text('Nome:', size=(7,1)), sg.InputText(key='it_cadasto_cliente_nome', size=(25,1), do_not_clear=False)],
      [sg.Text('cpf:', size=(7,1)), sg.InputText(key='it_cadasto_cliente_cpf', size=(25,1), do_not_clear=False)],
      [sg.Text('email:', size=(7,1)), sg.InputText(key='it_cadasto_cliente_email', size=(25,1), do_not_clear=False)],
      [sg.Text('telefone:', size=(7,1)), sg.InputText(key='it_cadasto_cliente_telefone', size=(25,1), do_not_clear=False)],

      [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('Sistema de Clientes', cliente_add_layout, finalize=True)
    # self.__container.hide()

  @property
  def container(self):
    return self.__container