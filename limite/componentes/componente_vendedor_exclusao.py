import PySimpleGUI as sg


class ComponenteVendedorExclusao:
  def __init__(self):
    vendedor_remove_layout = [
        [sg.Text('cpf:', size=(7,1)), sg.InputText(key='-cpf-', size=(25,1))],
        [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('vendedor remove', vendedor_remove_layout, finalize=True)

  @property
  def container(self):
    return self.__container