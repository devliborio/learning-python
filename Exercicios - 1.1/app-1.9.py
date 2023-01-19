# Requisição
turno = str(input("Digite qual o seu turno: "))

# Condições
if turno == "Matutino":
    print('Bom dia!')
elif turno == "Vespertino":
    print('Bom tarde!')
elif turno == 'Noturno':
    print('Boa noite!')
else:
    print('Valor digitado invalido!')