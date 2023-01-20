                                # CONTROLE SALARIO!

dinheiroHora = int(input("Quanto você ganha por hora? ")) # R$ 10 por hora
horasMes = int(input("Quantas horas foram trabalhadas no mês? ")) # 120 horas MÊS

if dinheiroHora and horasMes:
    salarioBruto = dinheiroHora * horasMes
    impostoRenda = salarioBruto * 0.11 # descontando 11% de algum valor!
    INSS = salarioBruto * 0.08 # descontando 8% de algum valor!
    sindicato = salarioBruto * 0.05 # descontando 5% de algum valor!
    salarioLiquido = salarioBruto - impostoRenda - INSS - sindicato
    print("Salário Bruto: R${} reais".format(salarioBruto))
    print("IR(11%): R${}".format(impostoRenda))
    print("INSS(8%): R${}".format(INSS))
    print("Sindicato (5%): R${}".format(sindicato))
    print("O seu Salario liquido é de: R${}".format(salarioLiquido))
