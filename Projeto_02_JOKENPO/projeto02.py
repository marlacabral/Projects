#O programa tem que:
# Permitir que eu decida quantas rodadas iremos fazer;
# Ler a minha escolha (Pedra, papel ou tesoura);
# Decidir de forma aleatória a decisão do computador;
# Mostrar quantas rodadas cada jogador ganhou;
# Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
# Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.



from random import randint #importei biblioteca para sorteio de numero aleatório
from time import sleep #importei biblioteca para espaço de tempo 

print('Bem vindo ao JOKENPÔ! Eu te desafio a me ganhar...quem perder, lava a louça por uma semana :)')
sleep(1)
votacao = " "
itens = ('Pedra', 'Papel', 'Tesoura')
contador_de_jogadas = 0
a = 0
b = 0

while True:
    jogadas = int(input('Insira o número de rodadas desejadas: '))

    for c in range(jogadas):
        contador_de_jogadas = contador_de_jogadas +1
        eu = randint(0, 2)
        print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
        voce = int(input('Qual é a sua jogada? '))
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!!')
        sleep(1)
        print('-=' * 11)
        print('Eu joguei {}'.format(itens[eu]))
        print('Você jogou {}'.format(itens[voce]))
        print('-=' * 11)
        sleep(1)

        if eu == 0:
            if voce == 0:
                print('Ahh! Empatamos :(')
            
            elif voce == 1:
                print('Você venceu :)')
                b += 1
               
            elif voce == 2:
                print('Uhuull, eu ganhei \o/')
                a += 1
                
            else:
                print('JOGADA INVÁLIDA')

        elif eu == 1:
            if voce == 0:
                print('Uhuull, eu ganhei \o/')
                a += 1 
                   
            elif voce == 1:
                print('Ahh! Empatamos :(')
           
            elif voce == 2:
                print('Você venceu :)')
                b += 1
                
            else:
                print('JOGADA INVÁLIDA')
        elif eu == 2:
            if voce == 0:
                print('Você venceu :)')
                b += 1
                
            elif voce == 1:
                print('Uhuull, eu ganhei \o/')
                a += 1
                
            elif voce == 2:
                print('Ahh! Empatamos :(')
            
        else:
            print('JOGADA INVÁLIDA') 
        
    if c+1 == jogadas:
        print(f'Eu ganhei {a} partidas e você ganhou {b} partidas.')
    if a == b:
        print('Como nós empatamos, não existe campeão, nós dois vamos precisar lavar a louça :(')
    if a > b:
        print('O troféu de campeão é meu!!!! A louça é sua por uma semana *-*')
    if a < b:
        print('O grande campeão é você!!! \o/\o/ . A louça sobrou pra mim :/')
    votacao = str(input("Gostaria jogar novamente? [S/N]: ")).upper().strip()[0]
    if votacao == 'N':
        break
    elif votacao == 'S':
        contador_de_jogadas = 0
