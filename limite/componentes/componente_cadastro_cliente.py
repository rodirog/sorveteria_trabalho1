import PySimpleGUI as sg


class ComponenteCadastroCliente:
  def __init__(self):
    cliente_add_layout = [
        [sg.Text('Nome:', size=(7,1)), sg.InputText(key='-cliente-nome-', size=(25,1), do_not_clear=False)],
        [sg.Text('email:', size=(7,1)), sg.InputText(key='-cliente-email-', size=(25,1), do_not_clear=False)],
        [sg.Text('cpf:', size=(7,1)), sg.InputText(key='-cliente-cpf-', size=(25,1), do_not_clear=False)],
        [sg.Text('telefone:', size=(7,1)), sg.InputText(key='-cliente-telefone-', size=(25,1), do_not_clear=False)],

        [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('cliente add', cliente_add_layout, finalize=True)
    self.__container.hide()

  @property
  def container(self):
    return self.__container