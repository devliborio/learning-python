request = str(input("Qual operação deseja realizar com os número 5 e 6 ? "))

numero1 = int(5)
numero2 = int(6)

soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2

if request == "divisão":
    print(divisao)
    if divisao >= 0:
        print("Positivo")
    elif divisao < 0:
        print("Negativo")
    if (divisao % 2) == 0:
        print("Par")
    else:
        print("Ìmpar")
    if divisao == round(divisao):
        print(f"{int(divisao)} é um número inteiro!")
    else:
        print(f"{divisao} é um número decimal!")


elif request == "soma":
    print(soma)
    if soma >= 0:
        print("Positivo")
    elif soma < 0:
        print("Negativo")
    if (soma % 2) == 0:
        print("Par")
    else:
        print("Ìmpar")
    if soma == round(soma):
        print(f"{int(soma)} é um número inteiro!")
    else:
        print(f"{soma} é um número decimal!")


elif request == "subtração":
    print(subtracao)
    if subtracao >= 0:
        print("Positivo")
    elif subtracao < 0:
        print("Negativo")
    if (subtracao % 2) == 0:
        print("Par")
    else:
        print("Ìmpar")
    if subtracao == round(subtracao):
        print(f"{int(subtracao)} é um número inteiro!")
    else:
        print(f"{subtracao} é um número decimal!")


elif request == "multiplicação":
    print(multiplicacao)
    if multiplicacao >= 0:
        print("Positivo")
    if (multiplicacao % 2) == 0:
        print("Par")
    else:
        print("Ìmpar")
    if multiplicacao == round(multiplicacao):
        print(f"{int(multiplicacao)} é um número inteiro!")
    else:
        print(f"{multiplicacao} é um número decimal!")
