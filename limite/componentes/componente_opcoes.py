import PySimpleGUI as sg

class ComponenteOpcoes:
  def __init__(self, rotulo: str):
    sg.ChangeLookAndFeel('DarkTeal4')

    tab_layout = [
        [sg.T(f'lista {rotulo}'.title(),  font=("Helvica", 15))],
        [sg.Radio(f'Incluir {rotulo.title()}', "RD1", key='1')],
        [sg.Radio(f'Excluir {rotulo.title()}', "RD1", key='4')],
        [sg.Radio(f'Listar {rotulo.title()}', "RD1", key='2')],
        [sg.Radio(f'Alterar {rotulo.title()}', "RD1", key='3')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Cancel('Voltar'), sg.Button('Confirmar')]
    ]
    self.__container = sg.Window(f'Sistema de {rotulo.title()}').Layout(tab_layout)

  @property
  def container(self):
    return self.__container