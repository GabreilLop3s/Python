import time #BIBLIOTECA IMORTADA PARA O TEMPORIZADOR NA LINHA (10)

while True: #Estrutura de repetição, executa oq diz na linha (13)

    distancia = float(input('Olá! seja bem-vindo a companhia de viagens IMPACTA, por favor digite a distancia (EM KM) que vai percorrer até o local de chegada: '))
    print(' QUE ÓTIMA NOTÍCIA! você está prestes e começar uma viagem de {}Km'.format(distancia))
    
    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.45

    print('Analisando percurso...')
    time.sleep(3)
    
    print("Sua viagem de {}km, teve o valor calculado em ${:.2f}. Para mais informações acesse nossa central de atendimento on-line. Tenha uma viagem IMPACTANTE!".format(distancia,preco))

    escolha = input(str('Deseja iniciar uma nova vigem? (S para sim e N para não)')).strip().upper()
    print(escolha)
    if escolha != "S":
        print("Agradecemos a preferência IMPACTA! tenha um otimo dia!")
        break

