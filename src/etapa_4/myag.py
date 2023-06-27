from agente import agente, imprimir_individuos, media_de_pontos_da_geracao
import random
from mapa import Mapa
import matplotlib.pyplot as plt
import numpy as np

def fitness_func(solution, mapa:Mapa):

    world = mapa


    actions = ['u', 'd', 'l', 'r']
    # Posição inicial do agente
    start_position = (0, 0)

    # Pontuação inicial
    score = 0
    pegou_ouro = False

    # Executar as ações sequencialmente
    for action in solution:
        # Calcular a próxima posição com base na ação
        if action == 'u':
            next_position = (start_position[0] - 1, start_position[1])
        elif action == 'd':
            next_position = (start_position[0] + 1, start_position[1])
        elif action == 'l':
            next_position = (start_position[0], start_position[1] - 1)
        elif action == 'r':
            next_position = (start_position[0], start_position[1] + 1)

        # Verificar se a próxima posição é válida
        if next_position[0] < 0 or next_position[0] >= world.altura or next_position[1] < 0 or next_position[1] >= world.altura:
            # Movimento inválido, penalizar pontuação
            score -= 10
        
        else:
            # Atualizar posição atual
            start_position = next_position
            # score += 5

            # if start_position[0] == 0 and start_position[1] == 0 and pegou_ouro == True:
            #     score += 1000 

            # Verificar as percepções do agente
            cell = world.matriz[start_position[0]][start_position[1]]
            if cell == 'G':
                # Agente encontrou o ouro, recompensar pontuação
                score += 100
                # world.matriz[start_position[0]][start_position[1]] = 0
                break
                
            elif cell == 'M':
                # Agente encontrou o Wumpus, penalizar pontuação e terminar
                score -= 100
                break
            elif cell == 'P':
                # Agente encontrou um buraco, penalizar pontuação
                score -= 50

    return score

# Definir o espaço de busca (range) para as variáveis
# var_range = np.array([['u', 'd', 'l', 'r']] * 10)  # Sequência de 10 ações


def primeira_geracao(num_invividuos, tam_individuo):
    
    movimentos = ['u', 'd', 'l', 'r']
    geracao = []

    for i in range(0, num_invividuos):
        individuo = agente(i)
        individuo.sequencia = ''.join(random.choice(movimentos) for _ in range(tam_individuo))
        geracao.append(individuo)
    return geracao

def avaliacao(geracao: list[agente], mapa: Mapa):
    pontuacao = []

    for individuo in geracao:
        pontos = fitness_func(individuo.sequencia, mapa)
        individuo.pontos = pontos
    
    ranked = sorted(geracao, key=lambda x: x.pontos, reverse=True)
    
    tam_melhores = len(ranked)/2
    if tam_melhores % 2 == 0:
        pass
    else:
        tam_melhores += 1

    # print(tam_melhores)
    melhores = ranked[:int(tam_melhores)]
    # imprimir_individuos(melhores)

    return melhores

def recombinacao(geracao: list[agente]):

    for i in range(0, len(geracao), 2):
        id_filho1 = str(geracao[i].id) + '_' + str(geracao[i+1].id)
        id_filho2 = str(geracao[i+1].id) + '_' + str(geracao[i].id)
        filho1 = agente(id_filho1)
        filho2 = agente(id_filho2)

        ponto_de_corte = random.randint(0, len(geracao[i].sequencia))

        filho1.sequencia = geracao[i].sequencia[:ponto_de_corte] + geracao[i+1].sequencia[ponto_de_corte:]
        filho2.sequencia = geracao[i+1].sequencia[:ponto_de_corte] + geracao[i].sequencia[ponto_de_corte:]

        geracao.append(filho1)
        geracao.append(filho2)

    # imprimir_individuos(geracao)
    return geracao


def myAG(tam_geracao, tam_sequencia, num_de_geracoes, mapa: Mapa, ploting: bool, text: bool):
    
    melhores_de_cada_geracao = []
    media_de_pontos_por_geracao = []

    lista_de_agentes = primeira_geracao(num_invividuos=tam_geracao, tam_individuo=tam_sequencia)
    lista_de_agentes = avaliacao(lista_de_agentes, mapa)
    media_de_pontos_por_geracao.append(media_de_pontos_da_geracao(lista_de_agentes))

    melhores_de_cada_geracao.append(lista_de_agentes[0])

    i = 0
    while(i < num_de_geracoes):
        lista_de_agentes = recombinacao(lista_de_agentes)
        lista_de_agentes = avaliacao(lista_de_agentes, mapa)
        i += 1

        media_de_pontos_por_geracao.append(media_de_pontos_da_geracao(lista_de_agentes))
        melhores_de_cada_geracao.append(lista_de_agentes[0])

    if text == True:
        print(f'melhor individuo: {lista_de_agentes[0]}')
        imprimir_individuos(melhores_de_cada_geracao)
        print(media_de_pontos_por_geracao)

    if ploting == True:
        # Dados para o primeiro gráfico
        x1 = np.arange(0, len(melhores_de_cada_geracao))
        melhores_de_cada_geracao_float = []

        for individuo in melhores_de_cada_geracao:
            individuo: agente
            melhores_de_cada_geracao_float.append(individuo.pontos)


        y1 = melhores_de_cada_geracao_float

        # Criar a primeira figura e o gráfico de linha
        fig1 = plt.figure()
        plt.plot(x1, y1)
        plt.ylabel('Pontuação')
        plt.xlabel('Geração')
        plt.title('Potuação do melhor indivíduo em cada geração')

        x2 = np.arange(0, len(media_de_pontos_por_geracao))
        y2 = media_de_pontos_por_geracao

        # Criar a primeira figura e o gráfico de linha
        fig2 = plt.figure()
        plt.plot(x2, y2)
        plt.ylabel('Pontuação')
        plt.xlabel('Geração')
        plt.title('Potuação média em cada geração')

        # Exibir as duas figuras
        plt.show()
