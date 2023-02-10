inicioJogo = int(input('Digite a hora de inicio do jogo: '))
fimJogo = int(input('Digite a hora do fim do jogo: '))

if inicioJogo > fimJogo:
    duracao = 24 - (inicioJogo - fimJogo)
else:
    duracao = fimJogo - inicioJogo

print('O jogo teve uma duração de',duracao, 'horas')