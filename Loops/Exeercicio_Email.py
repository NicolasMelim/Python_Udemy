
##Enviar email com 3 tentativas se a compra foi efetuada com sucesso.

compra_confirmada = True

dados_compras = "Compra aprovada 18,90 R$"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compras)
        print("Enviado para o seu e-mail!")
    break
else:
    print("Compra negada, sem crédito.")