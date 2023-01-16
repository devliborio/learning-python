# Aba de perguntas!
resposta = []
resposta.append(input('Você telefonou para a vítima? 1/Sim ou 0/Não: '))
resposta.append(input('Você esteve no local? 1/Sim ou 0/Não:'))
resposta.append(input('Você mora perto da vítima? 1/Sim ou 0/Não:'))
resposta.append(input('Você devia dinheiro para a vítima? 1/Sim ou 0/Não:'))
resposta.append(input('Você já trabalhou com a vítima? 1/Sim ou 0/Não: '))

soma_respostas = 0

for itens in resposta: # soma o número de respostas
    soma_respostas = soma_respostas + int(itens)

# Condições
if soma_respostas < 2:
    print("\nVocê é Inocente!")
elif soma_respostas == 2:
    print("\nVocê é Suspeito!")
elif 3 <= soma_respostas <= 4:
    print("\nVocê é Cúmplice!")
elif soma_respostas == 5:
    print("\nVocê é o Assasino!!")