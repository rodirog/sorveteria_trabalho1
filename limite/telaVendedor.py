

class TelaVendedor:
  def __init__(self):
    def pega_dados_vendedor(self):
          print("CADASTRO VENDEDOR")
          nome_cliente = input("Nome do Cliente: ")
          cpf_vendedor = input("Cpf do Vendedor:")
          codigo_vendedor = input("Codigo do Vendedor")

          return {"codigo_vendedor": codigo_vendedor,"nome_cliente": nome_cliente, "cpf_vendedor": cpf_vendedor}