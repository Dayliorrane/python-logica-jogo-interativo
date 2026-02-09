print('Você é um explorador corajoso, que se aventura pela floresta sussurante.')
print('Acredite no seu potencial, e encontre todos os tesouros lendários e segredos perdidos!')
print('Vamos lá! Conquiste a melhor pontuação!\n')
print('Olha só! Existem três caminhos distintos.\n')

def caminho_sombras():
    print('\nVocê entrou no caminho das sombras.')
    print('Este caminho é cercado por árvores antigas e sombrias, com raios de lua penetrando entre os galhos.')
    print('Parece ser o caminho mais misterioso e perigoso da floresta.')
    print('Nossa! Olha só essa criatura mágica, guardiã do caminho!')
    print('-- Resolva meu enigma! Se quiser passar por mim. Diz a criatura, com cara de poucos amigos...\n')

    print('Atenção! Digite sua resposta em letras minúsculas.\n')
    resposta = input(
        'Quem sou eu? Tenho olhos, mas não vejo. Tenho boca, mas não falo. O que sou? '
    )
    if resposta == 'uma caveira':
        print('\nResposta correta! Parabéns!')
        print('Você encontrou um baú escondido contendo uma gema preciosa que vale 100 pontos.\n')
    else:
        print('\nResposta incorreta!')
        print('Infelizmente você não encontrou os tesouros lendários da floresta sussurante.')
        print('Tente novamente.\n')

decisao = int(input('Qual caminho você vai escolher? 1, 2 ou 3? '))


def caminho_luz():
    print('Você entrou no Caminho da luz.')
    print('Este caminho é iluminado por raios de sol que filtram entre as copas das árvores. ')
    print('Parece ser o caminho mais seguro e reconfortante da floresta! ')
    print('Nossa! Olha só essa ponte quebrada, sobre o rio turbulento! ')
    print('O que você vai fazer? Vai atravessar ou procurar um desvio seguro?')
    print('Digite "atravessar" para seguir ou "contornar" para encontrar um caminho seguro. \n')

    print('Atenção! Digite sua resposta em letras minúsculas.\n')
    resposta = input(
        'O que você vai fazer? '
    )

    if resposta == 'atravessar':
        print('\nResposta correta! Parabéns!')
        print('Você acaba de encontrar uma fonte mágica que restaura sua saúde e adiciona 50 pontos à sua pontuação. \n')
    else:
        print('\nResposta incorreta!')
        print('Infelizmente você não encontrou os tesouros lendários da floresta sussurante.')
        print('Tente novamente.\n')

def caminho_criaturas():
    print('Você entrou no caminho das criaturas. ')
    print('Esse caminho é repleto de sons estranhos e pegadas misteriosas no chão. ')
    print('Parece ser o caminho mais imprevisível e enigmático da floresta! ')
    print('Nossa! Olha só, essa criatura mágica adormecida, bloqueando o caminho! ')
    print('O que você vai fazer? Vai tentar contornar a criatura, ou acordá-la? ')
    print('Digite "contornar" para tentar seguir ou "acordar" para derrotá-la e se salvar. \n')

    print('Atenção! Digite sua resposta em letras minúsculas.\n')
    resposta = input(
        'O que você vai fazer agora? '

    if resposta == 'contornar':
        print('\nResposta correta! Parabéns! Você encontrou a árvore encantada.')
        print('Ela te concede uma habilidade especial de camuflagem, adicionando 75 pontos a sua pontuação. \n')
    else:
        print('\nResposta incorreta!')
        print('Infelizmente você não encontrou os tesouros lendários da floresta sussurante.')
        print('Tente novamente.\n')


if decisao == 1:
    caminho_sombras()
elif decisao == 2:
    caminho_luz()
elif decisao == 3:
    caminho_criaturas()
