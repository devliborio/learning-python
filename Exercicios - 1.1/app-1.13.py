# Importando Objeto Date()
from datetime import date

# Requisição
anoNascimentoUser = int(input('Digite seu ano de nascimento: '))

# Função
def calcularIdade(): # Função para Calcular a Idade
    hoje = date.today() # Retorna a data de hoje.
    idade = hoje.year - anoNascimentoUser # Subtrai o ano atual pelo ano do nascimento do usuario 

    return idade

# Condições
if calcularIdade() >= 18: # Se a idade do usuario for maior ou igual a 18 anos faça:
     print('Você pode voltar!')
elif calcularIdade() < 18: # Se a idade do usuario for menor que 18 anso faça:
     print('Você não pode voltar!') 



