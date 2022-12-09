import PySimpleGUI as sg

class ComponenteVendedorSelecao:
  def __init__(self):
    vendedor_edit_layout = [
        [sg.Text('codigo:', size=(7,1)), sg.InputText(key='it_selecao_vendedor_codigo', size=(25,1))],
        [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('Vendedor edit', vendedor_edit_layout, finalize=True)

  @property
  def container(self):
    return self.__container