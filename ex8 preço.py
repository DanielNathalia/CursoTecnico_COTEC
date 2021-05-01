n1= float(input('digite o preço do produto:'))
n2= 5
m= n2 * n1
print('{} * {} = {}'.format(n2, n1, m))
d= m / 100
print('{} / {} = {}'.format(m,100, d))
sub= n1 - d 
print('{} - {} = {}'.format(n1,d, sub))
print('O produto custa {}. com 5% de desconto custa {}'.format(n1,sub))