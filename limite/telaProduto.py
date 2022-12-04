import PySimpleGUI as sg


class TelaProduto:

    def __init__(self):
        self.__window = None
        self.init_opcoes()


    # def mostrar_tela_opcoes(self):
    #     print("*" * 20)
    #     print("PRODUTO")
    #     print("*" * 20)
    #     print("1 - Incluir Produto")
    #     print("2 - Excluir Produto")
    #     print("3 - Listar Produto(s)")
    #     print("4 - Alterar Produto")
    #     print("5 - Relatorio de sorvetes")
    #     print("6 - Relatorio de bebidas")
    #     print("0 - Voltar")
    #     opcao = int(input("Escolha a opcao: "))
    #     return opcao

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- PRODUTOS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Produto', "RD1", key='1')],
        [sg.Radio('Excluir Produto', "RD1", key='2')],
        [sg.Radio('Listar Produtos', "RD1", key='3')],
        [sg.Radio('Alterar Produtos', "RD1", key='4')],
        [sg.Radio('Relatório de sorvetes', "RD1", key='5')],
        [sg.Radio('Relatório de bebidas', "RD1", key='6')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de produtos').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pegar_dados_produto(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Incluir novo produto")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(key="it_descricao")],
            [sg.Radio('Sorvete', "RADIO01", default=True), sg.Radio('Bebida', "RADIO01")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Produtos').Layout(layout)

        button, values = self.open()
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        tipo = values[0]
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_produto": codigo, "estoque_produto": estoque, "descricao_produto": descricao, "tipo_produto": tipo, "valor_produto": valor}

    def alterar_dados_produto(self, dados_produto):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Alterar produto")],
            [sg.Text("Codigo", size = (15,1)), sg.InputText(dados_produto["codigo_produto"], key="it_codigo")],
            [sg.Text("Estoque", size = (15,1)), sg.InputText(dados_produto["estoque_produto"], key="it_estoque")],
            [sg.Text("Descricao", size = (15,1)), sg.InputText(dados_produto["descricao_produto"], key="it_descricao")],
            [sg.Radio('Sorvete', "RADIO01", default=True), sg.Radio('Bebida', "RADIO01")],
            [sg.Text("Valor", size = (15,1)), sg.InputText(dados_produto["valor_produto"], key="it_valor")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Produtos').Layout(layout)

        button, values = self.open()
        codigo = int(values['it_codigo'])
        estoque = int(values['it_estoque'])
        descricao = values['it_descricao']
        tipo = values[0]
        valor = float(values['it_valor'])

        self.close()
        return {"codigo_produto": codigo, "estoque_produto": estoque, "descricao_produto": descricao, "tipo_produto": tipo, "valor_produto": valor}

     # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostrar_produto(self, dados_produto):
        string_todos_produtos = ""
        for dado in dados_produto:
            string_todos_produtos = string_todos_produtos + "CODIGO: " + str(dado["codigo_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "ESTOQUE: " + str(dado["estoque_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "DESCRICAO: " + str(dado["descricao_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "TIPO: " + str(dado["tipo_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "VALOR: " + str(dado["valor_produto"]) + '\n\n'

        sg.Popup('-------- LISTA DE PRODUTOS ----------', string_todos_produtos)

     # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def selecionar_produto(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR PRODUTO ----------', font=("Helvica", 25))],
        [sg.Text('Digite o codigo do produto que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Codigo:', size=(15, 1)), sg.InputText(key='it_codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona produto').Layout(layout)

        button, values = self.open()
        codigo = values['it_codigo']
        self.close()
        return int(codigo)

    def mostrar_relatorio_de_sorvetes(self, dados_sorvetes):
        string_todos_sorvetes = ""
        for dado in dados_sorvetes:
            string_todos_sorvetes = string_todos_sorvetes + "QUANTIDADE VENDIDA: " + str(dado["quantidade_vendida_sorvete"]) + "Kg" + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "CODIGO: " + str(dado["codigo_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "ESTOQUE: " + str(dado["estoque_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "DESCRICAO: " + str(dado["descricao_sorvete"]) + '\n'
            string_todos_sorvetes = string_todos_sorvetes + "VALOR: " + str(dado["valor_sorvete"]) + '\n\n'

        sg.Popup('-------- LISTA DE SORVETES ----------', string_todos_sorvetes)

    def mostrar_relatorio_de_bebidas(self, dados_bebidas):
        string_todas_bebidas = ""
        for dado in dados_bebidas:
            string_todas_bebidas = string_todas_bebidas + "QUANTIDADE VENDIDA: " + str(dado["quantidade_vendida_bebida"]) + " unidade(s)" + '\n'
            string_todas_bebidas = string_todas_bebidas + "CODIGO: " + str(dado["codigo_bebida"]) + '\n'
            string_todas_bebidas = string_todas_bebidas + "ESTOQUE: " + str(dado["estoque_bebida"]) + '\n'
            string_todas_bebidas = string_todas_bebidas + "DESCRICAO: " + str(dado["descricao_bebida"]) + '\n'
            string_todas_bebidas = string_todas_bebidas + "VALOR: " + str(dado["valor_bebida"]) + '\n\n'

        sg.Popup('-------- LISTA DE BEBIDAS ----------', string_todas_bebidas)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)


    # def pegar_dados_produto(self):
    #     print()
    #     print("CADASTRO PRODUTO")
    #     codigo_produto = int(input("Codigo do Produto: "))
    #     estoque_produto = int(input("Estoque do Produto: "))
    #     descricao_produto = str(input("Descricao do Produto: "))
    #     tipo_produto = int(input("Tipo do Produto (insira '1' para sorvete ou '2' para bebida): "))
    #     valor_produto = float(input("Valor do Produto: "))

    #     return {"codigo_produto": codigo_produto, "estoque_produto": estoque_produto, "descricao_produto": descricao_produto, "tipo_produto": tipo_produto, "valor_produto": valor_produto}

    # def alterar_dados_produto(self):
    #     print()
    #     print("ALTERAR PRODUTO")
    #     codigo_produto = int(input("Codigo do Produto: "))
    #     estoque_produto = int(input("Estoque do Produto: "))
    #     descricao_produto = str(input("Descricao do Produto: "))
    #     valor_produto = float(input("Valor do Produto: "))

    #     return {"codigo_produto": codigo_produto, "estoque_produto": estoque_produto, "descricao_produto": descricao_produto, "valor_produto": valor_produto}

    # def mostrar_produto(self, dados_produto):
    #     print()
    #     print("PRODUTO")
    #     print(f"Codigo: {dados_produto['codigo_produto']}")
    #     print(f"Estoque: {dados_produto['estoque_produto']}")
    #     print(f"Descricao: {dados_produto['descricao_produto']}")
    #     print(f"Tipo: {dados_produto['tipo_produto']}")
    #     print(f"Valor: {dados_produto['valor_produto']}")
    #     print()

    # def selecionar_produto(self):
    #     print()
    #     codigo = int(input("Insira o codigo do produto que deseja selecionar: "))
    #     return codigo



    # def mostrar_relatorio_de_bebidas(self, dados_bebida):
    #     print()
    #     print("BEBIDA")
    #     print(f"Quantidade total vendida: {dados_bebida['quantidade_vendida_produto']} unidade(s)")
    #     print(f"Codigo: {dados_bebida['codigo_produto']}")
    #     print(f"Estoque: {dados_bebida['estoque_produto']}")
    #     print(f"Descricao: {dados_bebida['descricao_produto']}")
    #     print(f"Valor: {dados_bebida['valor_produto']}")
    #     print()

