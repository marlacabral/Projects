from time import sleep

print('Bem vindo ao Projeto 04 - VOTAÇÃO')
sleep(1)

candidatos=['Jose', 'Maria', 'Pedro', 'Nulo', 'Branco']
votos = dict()

def autoriza_voto():
    while True:
        anoNasc = int(input('Digite o ano do seu nascimento: '))
        idade = 2021 - anoNasc
        if 16 < idade < 18 or idade > 70:
            print('Devido a sua idade, seu voto é OPCIONAL.')
            return True
        elif idade < 16:
            print('NEGADO: Devido a sua idade, você não pode votar.')
            return False
        else:
            print('Seu voto é OBRIGATÓRIO.')
            return True
sleep(1)

def votacao():
    for c in range(len(candidatos)):
        votos[f'{candidatos[c]}'] = 0
    print('-=' * 20)
    while True:
        if autoriza_voto() == True:
            for c in range(len(candidatos)):
                print(f'{c+1}-{candidatos[c]}')
        voto = int(input('Digite o seu voto: '))
        votos[candidatos[voto-1]] = int(votos[candidatos[voto-1]]) + 1
        print('-=' * 20)    
        if input('Deseja continuar? [S/N]: ').upper()[0] == 'N':
            break
    for c in range(len(candidatos)):
        print(f'Total de votos {candidatos[c]}: {votos[f"{candidatos[c]}"]}')
    vitoria = []
    for c in range(len(candidatos)):
        vitoria.append(votos[f"{candidatos[c]}"])
        vitoriasIndex = vitoria.index(max(vitoria))
    print('-=' * 20)
    print(f'{candidatos[vitoriasIndex]} teve mais votos nessa eleição.')

votacao()
