print('Bem vindo, compras acima de 10 unidades com 10% de desconto e acima 20 unidades com 20% de desconto!')

n1 = eval(input('digite a quantidade de produtos que deseja:'))

n2 = 20
desc10 = 0.1
desc20 = 0.2
m = n2 * n1



if n1 >= 10 < 20:
    valor_final = 10 * n1 * (1 - desc10)

elif n1 > 10 <= 20:
    valor_final = 10 * n1 * (1 - desc20)

else:
    valor_final = 10 * n1

print(f'A quantidade {n1} deste produto custa R${valor_final}')

