print('*' * 30)
print('> > > CALCULO DE EXCESSO')
print('*' * 30)
peso = float(input('Quantos kg de peixe? '))
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print(f'{peso}Kg de peixe teve excesso de {excesso}Kg e a multa foi de {multa}R$')
elif peso == 50:
    print('Peso igual a 50 quilos, SEM MULTA!')
else:
    print('Peso abaixo de 50 quilos, SEM MULTA!')