nome = input('Informe o nome do aluno:');
nota1 = float(input('Informe a nota 1:'));
nota2 = float(input('Informe a nota 2:'));
soma = (nota1 + nota2);
media = soma / 2

print('A média das notas é {:.1f}'.format(media));
if media >= 7.0:
    print(f'Parabéns {nome}, você aprovado!')
elif media >= 5.0:
    print('Você está em recuperação!')

else:
    print('Você foi reprovado!')
