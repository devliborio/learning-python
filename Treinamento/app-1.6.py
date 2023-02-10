n1 = int(input("Digite um número inteiro: "))  # 20
n2 = int(input("Digite outro número inteiro: "))  # 10
nr = int(input("Digite um número real: "))

if n1 and n2 and nr:
    aAlternative = (n1 * 2) * (n2 / 2)
    bAlternative = (n1 * 3) + nr
    cAlternative = nr**3
    print(
        "A - O resultado do produto do dobro do primeiro com a métade do segundo é: {}".format(
            aAlternative
        )
    )
    print(
        "B - O resultado da soma do triplo do primeiro com o terceiro é: {}".format(
            bAlternative
        )
    )
    print("C - O resultado de nr elevado ao cubo é: {}".format(cAlternative))
