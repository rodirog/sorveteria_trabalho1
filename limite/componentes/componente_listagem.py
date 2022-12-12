import PySimpleGUI as sg

class ComponenteListagem:
  def __init__(self, rotulo: str, lista):
    sg.ChangeLookAndFeel('DarkTeal4')

    tab_layout = [
        [sg.T(f'lista {rotulo}'.title(),  font=("Helvica", 15))],
        [sg.Listbox(values=lista, size=(40, 20),enable_events=True, key='-LISTBOX-'),],
        [sg.Button('Voltar')]
    ]

    self.__container = sg.Window(f'Sistema de {rotulo.title()}').Layout(tab_layout)

  @property
  def container(self):
    return self.__container