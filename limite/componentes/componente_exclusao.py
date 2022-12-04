import PySimpleGUI as sg


class ComponenteExclusao:
  def __init__(self):
    cliente_remove_layout = [
        [sg.Text('cpf:', size=(7,1)), sg.InputText(key='-cpf-', size=(25,1))],
        [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('cliente remove', cliente_remove_layout, finalize=True)

  @property
  def container(self):
    return self.__container