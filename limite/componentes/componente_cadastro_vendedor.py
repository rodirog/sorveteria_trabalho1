import PySimpleGUI as sg


class ComponenteCadastroVendedor:
  def __init__(self):
    vendedor_add_layout = [
        [sg.Text('Nome:', size=(7,1)), sg.InputText(key='-vendedor-nome-', size=(25,1), do_not_clear=False)],
        [sg.Text('cpf:', size=(7,1)), sg.InputText(key='-vendedor-cpf-', size=(25,1), do_not_clear=False)],

        [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('vendedor add', vendedor_add_layout, finalize=True)
    self.__container.hide()

  @property
  def container(self):
    return self.__container