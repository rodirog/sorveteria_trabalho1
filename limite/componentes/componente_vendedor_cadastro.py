import PySimpleGUI as sg


class ComponenteVendedorCadastro:
  def __init__(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    vendedor_add_layout = [
        [sg.Text('Nome:', size=(7,1)), sg.InputText(key='it_cadasto_vendedor_nome', size=(25,1), do_not_clear=False)],
        [sg.Text('Cpf:', size=(7,1)), sg.InputText(key='it_cadasto_vendedor_cpf', size=(25,1), do_not_clear=False)],

        [sg.Button('Cancelar'), sg.Submit()]
    ]

    self.__container = sg.Window('Sistema vendedores', vendedor_add_layout, finalize=True)

  @property
  def container(self):
    return self.__container