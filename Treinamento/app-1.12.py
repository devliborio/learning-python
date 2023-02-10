# Requisição 
quantidadeApple = int(input('Digite quantas maças você quer comprar: ')) 

# Variaveis
apple = 1.30
appleDesconto = 1.00

# Condições
if quantidadeApple < 12:
    print('O total da compra foi de: ', 'R$',apple * quantidadeApple)
elif quantidadeApple >= 12:
    print ('O total da compra foi de: ', 'R$',appleDesconto * quantidadeApple)
