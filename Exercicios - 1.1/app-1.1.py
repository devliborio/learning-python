res = []
res.append(input('Qual a nota do 1 semestre? '))
res.append(input('Qual a nota do 2 semestre? '))
res.append(input('Qual a nota do 3 semestre? '))
res.append(input('Qual a nota do 4 semestre? '))

soma_notas = 0

for notas in res:
    soma_notas += float(notas)/2

print('A média é: ',soma_notas)