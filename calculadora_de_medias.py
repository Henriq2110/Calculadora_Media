
# Definindo função str para float
def str_to_float(s):
    return float(s) if s else 0.0

#input do programa
print('Se a nota ainda não foi lançada, não insira nenhum número!')
n1 = input('Nota Bimestre 1: ')
n2 = input('Nota Bimestre 2: ')
n3 = input('Nota Bimestre 3: ')

#condição para saber número de bimestres
numero_bimestres = 0
if n1 != '' and n2 != '' and n3 != '':
    numero_bimestres = 3
    n1 = str_to_float(n1)
    n2 = str_to_float(n2)
    n3 = str_to_float(n3)
elif n1 != '' and n2 != '':
    numero_bimestres = 2
    n1 = str_to_float(n1)
    n2 = str_to_float(n2)
elif n1 != '':
    numero_bimestres = 1
    n1 = str_to_float(n1)
else:
    print('Você ainda não possui nenhuma nota!')

#condição e cálculo da média
media = 0
if numero_bimestres == 1:
    media = n1
elif numero_bimestres == 2:
    media = (n1 + n2*2) / 3
elif numero_bimestres == 3:
    media = (n1 + n2*2 + n3*3) / 6

#output do programa
if numero_bimestres > 0:
    print(f'Sua média é de {media:.2f}')
if media >= 70 and numero_bimestres == 3:
    print('Aprovado!')
elif media <= 70 and numero_bimestres == 3:
    print('Reporvado!')

