# PROGRAMA PRO JOÃO!

perguntaQuilos = int(input('Quantos quilos de peixe você pescou jõao? '))
pesoPeixe = perguntaQuilos


if pesoPeixe > 50:
    pesoExcesso = pesoPeixe - 50 # Sempre quando quiser saber a diferença, sobra, excesso fazer a subtração do limite pela quantidade que você ultrapassou!
    multa = 4 * pesoExcesso
    print("Hoje jõao pescou {}Kg, e teve {}Kg a mais que o estabelecido pelo regulamento e teve uma multa equivalente a R${} reais".format(pesoPeixe, pesoExcesso, multa))
else:
    print("Hoje jõao pescou {}Kg, e está de acordo com as normas do regulamento então ele não paga multa.".format(pesoPeixe))