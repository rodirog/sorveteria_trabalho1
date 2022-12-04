import PySimpleGUI as sg

class ComponenteOpcoes:
  def __init__(self, rotulo: str, lista):
    sg.theme('default1')

    tab_layout = [
        [sg.T(f'lista {rotulo}')],
        # Option values revised
        [sg.Listbox(values=lista, size=(15, 7),enable_events=True, key='-LISTBOX-'),],
        [sg.Button('Incluir', border_width=5, key='adicionar'),
         sg.Button('Excluir', border_width=5, key='remover'),
         sg.Button('Alterar', border_width=5, key='editar')
         ]
    ]

    main_layout = [
        [sg.TabGroup([[sg.Tab(f'   {rotulo}   ', tab_layout, ),]],
                     )],
        [sg.Button('Exit')],
    ]

    self.__container = sg.Window('Main', main_layout, finalize=True)
    self.__container.hide()

  @property
  def container(self):
    return self.__container