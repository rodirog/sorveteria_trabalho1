

class TelaVendedor:
  def mostrar_tela_opcoes(self):
    print("*" * 20)
    print("VENDEDOR")
    print("*" * 20)
    print("1 - Incluir vendedor")
    print("2 - Excluir vendedor")
    print("3 - Encontrar vendedor")
    print("4 - Listar vendedor")
    print("5 - Alterar Vendedor")
    print("0 - Voltar")
    opcao = int(input("Escolha a opcao: "))
    return opcao 

  def pegar_codigo_vendedor(self):
    codigo_vendedor = input("codigo vendedor:")
    return codigo_vendedor

  def pegar_dados_vendedor(self):
        print("CADASTRO VENDEDOR")
        codigo_vendedor = input("Codigo do Vendedor")
        nome_vendedor = input("Nome do vendedor: ")
        cpf_vendedor = input("Cpf do Vendedor:")
        
        return {"codigo_vendedor": codigo_vendedor,"nome_vendedor": nome_vendedor, "cpf_vendedor": cpf_vendedor}

  def mostrar_vendedor(self, dados_vendedor):
     print("VENDEDOR")
     print(f"codigo: {dados_vendedor['codigo_vendedor']}")
     print(f"Nome: {dados_vendedor['nome_vendedor']}")
    

  def mostrar_mensagem(self, mensagem):
    print(mensagem)     