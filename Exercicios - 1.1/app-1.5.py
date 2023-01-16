celsius = float(input('Qual a temperatura em graus Celsius? '))

if celsius:
    fahrenheit = (celsius * 1.8) + 32
    print('A conversão de {} graus Celsius para Fahrenheit fica: {}'.format(celsius,fahrenheit))