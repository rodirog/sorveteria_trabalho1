import PySimpleGUI as sg


class ComponenteVendedorEdicao:
  def __init__(self, vendedor_dto):
    sg.ChangeLookAndFeel('DarkTeal4')
    vendedor_edicao_layout = [
      [sg.Text("Editar vendedor")],
      [sg.Text('Nome:', size=(7,1)), sg.InputText(vendedor_dto.nome, key='it_edicao_vendedor_nome', size=(25,1), do_not_clear=False)],

      [sg.Button('Cancel'), sg.Submit()]
    ]

    self.__container = sg.Window('Sistema de vendedores', vendedor_edicao_layout, finalize=True)

  @property
  def container(self):
    return self.__container