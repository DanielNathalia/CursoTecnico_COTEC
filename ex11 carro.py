n1= float(input('digite por quantos dias o carro ficou em seu domínio:'))
n2= float(input('digite quantos quilometros rodado:'))
m1= n1 * 60
print('{} * {} = {}'.format(n1, 60, m1))
m2= n2 * 0.15
print('{} * {} = {}'.format(n2, 0.15, m2))
s= m1 + m2
print('{} + {} = {}'.format(m1, m2, s))
print('você deverá pagar {} pelos dias que ficou'.format(m1))
print('você deverá pagar {} pelos quilometros rodado'.format(m2))
print('total a pagar pelo carro é {}'.format(s))
