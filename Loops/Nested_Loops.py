for produto1 in range(1, 6):
    print('Produto' + str(produto1))
    for produto2 in range(1,6):
        print(produto1 , produto2 , "oi")



print("-" * 30)

adicionar = []
for produto1 in range(1, 6):
    print('Produto' + str(produto1))
    for produto2 in range(1, 6):
        if produto1 == produto2:
         print(produto1 , produto2 , "oi")
         adicionar.append(produto2)
         print(adicionar)