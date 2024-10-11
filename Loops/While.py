preco = 100

dia = 0

while preco > 20:
    preco -=5
    dia+=1
    print(f'No dia {dia} o preco do item é de: R${preco}')


loja = int(input("Digite o valor do seu tênis: R$"))

while loja > 400:
    loja = (loja *0.10) - loja
    print("Como o seu tenis foi acima de 500, voce obteve um descto de 10%!!")
    print(f'O valor final ficou entre: R${loja}')
    break


loja2 = int(input("Digite o valor do tenis que voce vendeu: "))

while loja2 > 400:
    loja2 = (loja2 *10)
    print(f'Sua comissão foi de: R${loja2:.2f}')
    break