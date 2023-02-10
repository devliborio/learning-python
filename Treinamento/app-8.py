combustivel = input("Digite o tipo de combusitvel: ")
litros = float(input("Digite a quantidade de litros: "))

if combustivel.lower() == "a":
    custo = litros * 1.40

    if litros <= 20:
        desconto = custo * 3 / 100 # 3 / 100 = 3%
    else:
        desconto = custo * 4 / 100 # 4 / 100 = 4%


    custo_final = custo - desconto
    print(f'O valor a se pagar será de: R$ {custo_final:.2f}')
else:
     valor = litros * 2.50

     if litros <= 10:
        desconto = valor * 4 / 100
     else:
        desconto = valor * 6 / 100

     custo_final = valor - desconto
     print(f"o valor a se pagar será de: R$ {custo_final:.2f}") 




            

    
