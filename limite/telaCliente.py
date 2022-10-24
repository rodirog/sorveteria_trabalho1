class TelaCliente:

  def pega_dados_cliente(self):
          print("CADASTRO CLIENTE")
          nome_cliente = input("Nome do Cliente: ")
          email_cliente = input("Email do Cliente:")
          cpf_cliente = input("Cpf do Cliente:")
          telefone_cliente = input("Teleone do Cliente: ")
          return {"nome_cliente": nome_cliente, "telefone_cliente": telefone_cliente, "email_cliente": email_cliente, "cpf_cliente": cpf_cliente}