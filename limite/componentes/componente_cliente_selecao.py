import PySimpleGUI as sg

class ComponenteClienteSelecao:
  def __init__(self):
    cliente_edit_layout = [
        [sg.Text('cpf:', size=(7,1)), sg.InputText(key='it_selecao_cliente_cpf', size=(25,1))],
        [sg.Button('Cancelar'), sg.Submit()]
    ]

    self.__container = sg.Window('cliente edit', cliente_edit_layout, finalize=True)

  @property
  def container(self):
    return self.__container