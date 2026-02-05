print('Você é um explorador corajoso, que se aventura pela floresta sussurante.')
print('Acredite no seu potencial, e encontre todos os tesouros lendários e segredos perdidos!')
print('Vamos lá! Conquiste a melhor pontuação!\n')

print('Olha só! Existem três caminhos distintos.\n')

while True:
    decisao = int(input('Qual caminho você vai escolher? 1, 2 ou 3? '))

    if decisao not in [1,2,3]:
        print(f'Opção Inválida! Você digitou {decisao}. Escolha 1, 2 ou 3 para continuar.')
        continue

    if decisao == 1:
        print('Você entrou no caminho das sombras. ')
        print('Este caminho é cercado por árvores antigas e sombrias, com raios de lua penetrando entre os galhos.\n')
        print('Parece ser o caminho mais misterioso e perigoso da floresta.')
        print('Nossa! Olha só essa criatura mágica, guardiã do caminho!')
        print('-- Resolva meu enigma! Se quiser passar por mim. Diz a criatura, com cara de poucos amigos...\n')

        print('Atenção! Digite sua reposta em letras minúsculas.\n')
        resp_enigma = str(input('Quem sou eu? Tenho olhos, mas não vejo. Tenho boca, mas não falo. O que sou? '))
        if resp_enigma == 'uma caveira':
            print(' ')
            print('Resposta correta! Parabéns!')
            print('\nVocê acaba de encontrar um baú escondido contendo uma gema preciosa que vale 100 pontos. \n')
            break
        else:
            print(' ')
            print('Resposta incorreta!')
            print('\nInfelizmente você não encontrou os tesouros lendários e segredos perdidos da floresta sussurante.\n')
            print('Tente novamente')
            break

    elif decisao == 2:
        print(' ')
        print('Você entrou no caminho da luz.')
        print('Este caminho é iluminado por raios de sol que filtram entre as copas das árvores. ')
        print('Parece ser o caminho mais seguro e reconfortante da floresta! ')
        print('Nossa! Olha só essa ponte quebrada, sobre o rio turbulento! ')
        print('O que você vai fazer? Vai atravessar ou procurar um desvio seguro?')
        print('Digite "atravessar" para seguir ou "contornar" para encontrar um caminho seguro. \n')

        print('Atenção! Digite sua reposta em letras minúsculas.\n')
        resp_enigma = input('O que você vai fazer? ')
        if resp_enigma == 'atravessar':
            print(' ')
            print('Resposta Correta. Parabéns! \nVocê acaba de encontrar uma fonte mágica que restaura sua saúde e adiciona 50 pontos à sua pontuação. \n')
            break
        else:
            print(' ')
            print('Resposta incorreta!')
            print('\nInfelizmente você não encontrou os tesouros lendários e segredos perdidos da floresta sussurante. \n')
            print('Tente novamente')
            break

    elif decisao == 3:
        print(' ')
        print('Você entrou no caminho das criaturas. ')
        print('Esse caminho é repleto de sons estranhos e pegadas misteriosas no chão. ')
        print('Parece ser o caminho mais imprevisível e enigmático da floresta! ')
        print('Nossa! Olha só, essa criatura mágica adormecida, bloqueando o caminho! ')
        print('O que você vai fazer? Vai tentar contornar a criatura, ou acordá-la? ')
        print('Digite "contornar" para tentar seguir ou "acordar" para derrotá-la e se salvar. \n')

        print('Atenção! Digite sua reposta em letras minúsculas.\n')
        resp_enigma = input('O que você vai fazer agora? ')
        print(' ')
        if resp_enigma == 'contornar':
            print('Resposta correta! Parabéns! Você encontrou a árvore encantada.')
            print('\nEla te concede uma habilidade especial de camuflagem, adicionando 75 pontos a sua pontuação. \n')
            break
        else:
            print(' ')
            print('Resposta incorreta!')
            print('\nInfelizmente você não encontrou os tesouros lendários e segredos perdidos da floresta sussurante. \n')
            print('Tente novamente')
            break















