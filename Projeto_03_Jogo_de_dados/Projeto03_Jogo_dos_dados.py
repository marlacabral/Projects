# # Projeto 03 – Jogo de Dados

# # Utilizando  os  conceitos  aprendidos  até dicionários,  crie  um  programa  onde  4 jogadores joguem um dado e tenham resultados aleatórios.
# # O programa tem que:•Perguntar quantas rodadas você quer fazer; 
# # •Guardar os resultados dos dados em um dicionário. 
# # •Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
# # •Mostrar  no  final  qual  jogador  ganhou  mais  rodadas  e  foi  o  grande campeão.
# from random import randint
# partidas = dict()
# jogadores = dict()
# quantPartidas = int(input('Quantas partidas quer realizar? '))
# for contadorPartidas in range(quantPartidas):
#     lista = list()
#     print('-=' *20)
#     print(f'Partida{contadorPartidas+1}')
#     partidas['partida'+ str(contadorPartidas+1)]=list()
#     for partida in range(4):
#         lista.append(randint(1,6))
#         print(f'Jogador{partida+1} sua jogada resultou em {lista[partida]}.')
#     partidas['partida'+ str(contadorPartidas+1)]=lista
# for jog in range(1,5):
#     jogadores['jogador'+str(jog)] = list()
# for key in partidas.keys():
#     temp = list(partidas[key])
#     temp.sort(reverse=True)
#     for ordenando in range(4):
#         if (temp.index(partidas[key][ordenando])+1) in jogadores['jogador' + str(ordenando+1)]:
#             jogadores['jogador' + str(ordenando+1)].append(temp.index(partidas[key][ordenando])+2)
#         else:
#             jogadores['jogador' + str(ordenando+1)].append(temp.index(partidas[key][ordenando])+1)
# vitorias = list()
# for key in jogadores.keys():
#     vitorias.append(jogadores[key].count(1))

# for percorrer in range(quantPartidas):
#     print('-=' *20)
#     print(f'Na partida {percorrer+1}')
#     for key in jogadores.keys():
#         print(f'O {key} ficou na posição {jogadores[key][percorrer]}')
# print('-=' *20)
# print(f'O jogador{vitorias.index(max(vitorias))+1} é o grande campeão.')

import os
import sys
if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
    #Limpando a tela do Interpretador no Windows
    clear = lambda: os.system('cls')
    clear()
else:
    #Limpando a tela do Interpretador no Linux
    clear = lambda: os.system('clear')
    clear()

# Programa principal

from time import sleep #Lib para realizar temporizar tarefas
import random #Lib para realizar sorteio de números aleatórios
from operator import itemgetter # lib para organizar items da list()

vit1 = vit2 = vit3 = vit4 = empates = 0  # Declarando vitórias e empates
resp = None

print('''
    VAMOS JOGAR DADOS ?
    
   _______
 /\ o o o \ ______
<  o >------>   o /|
 \ o/  o   /o____/o|
  \/______/     |oo|
        |   o   |o /
        |_______|/
''')
sleep(2)
while resp != 'N':
    rod = int(input('Número de rodadas: ')) # Declarando o número de rodadas.
    print()
    clear()
    # Cada Jogador terá um valor sorteado através da lib Random
    for c in range(rod):
        jogo = {'Player1': random.randint(1,6),
                'Player2': random.randint(1,6),
                'Player3' : random.randint(1,6),
                'Player4': random.randint(1,6)}
        placar = list()
        # listando cada jogador e suas jogadas respectivamente
        print('Valores sorteados: ')
        for k, v in jogo.items():
            print(f'{k} tirou {v} no dado.')
            sleep(1)

        # Validando o vencedor de cada Rodada
        if (jogo['Player3'] < jogo['Player1'] > jogo['Player2']) and jogo['Player1'] > jogo['Player4'] :
            vit1 +=1
            print()
            print('O Player 1 foi o vencedor dessa rodada !')
        elif (jogo['Player3'] < jogo['Player2'] > jogo['Player1']) and jogo['Player2'] > jogo['Player4'] :
            vit2 +=1
            print()
            print('O Player 2 foi o vencedor dessa rodada !')
        elif (jogo['Player2'] < jogo['Player3'] > jogo['Player1']) and jogo['Player3'] > jogo['Player4'] :
            vit3 +=1
            print()
            print('O Player 3 foi vencedor dessa rodada !')
        elif (jogo['Player3'] < jogo['Player4'] > jogo['Player2']) and jogo['Player4'] > jogo['Player1'] :
            vit4 += 1
            print()
            print('O Player 4 foi o vencedor dessa rodada !')
        else:
            empates = rod - (vit1+vit2+vit3+vit4) # Contador de empates
            print()
            print('Houve um empate nessa rodada.')
        placar = sorted(jogo.items(), key=itemgetter(1), reverse = True) # Para ordenar do maior resultado para o menor

        print()
        print('   ==== Ranking ===')
        for i, v in enumerate(placar): 
            print(f'{i+1}° lugar: {v[0]} com {v[1]}.') 
            sleep(1)
        print()
        print('*' * 40)
        clear()
    while True:
        resp = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Digite apenas S ou N.')
    if resp == 'N':
        break
print('E O GRANDE VENCEDOR FOI ...')
sleep(2)
print('.', end=' ') # Dramatização do resultado rs ^^
sleep(1)
print('.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print()
# Validando o vencedor
if vit3 < vit1 > vit2 and vit1 > vit4:
  print(f'O Player 1 venceu com {vit1} vitórias.')
elif vit3 < vit2 > vit1 and vit2 > vit4:
  print(f'O Player 2 venceu com {vit2} vitórias.')
elif vit2 < vit3 > vit1 and vit3 > vit4:
  print(f'O Player 3 venceu com {vit3} vitórias.')
elif vit3 < vit4 > vit1 and vit4 > vit2:
  print(f'O Player 4 venceu com {vit4} vitórias.')
else:
    print('Houve um empate.')
print()
# Validando o número de vitórias de cada Jogador

# print(f'''
# O Player 1 teve {vit1} vitórias.
# O Player 2 teve {vit2} vitórias.
# O Player 3 teve {vit3} vitórias.
# O Player 4 teve {vit4} vitórias.
# \n
# Tivemos {empates} empates.

# ''')
resp = str(input('Deseja ver o placar final?[S/N]: ')).strip().upper()[0]
if resp not in 'SN':
    print('Digite apenas S ou N.')
if resp == 'S':
    print(f'''
     _____________________
    |    **  PLACAR  **   |
    |_____________________|
    |Player 1 | {vit1} vitórias|
    |Player 2 | {vit2} vitórias|
    |Player 3 | {vit3} vitórias|
    |Player 4 | {vit4} vitórias|
    |_____________________|
    
    Fim de Jogo ^^
    ''')
else:
  print('Fim de Jogo ^^')

