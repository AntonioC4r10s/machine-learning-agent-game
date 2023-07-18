from agente import agente, imprimir_individuos, media_de_pontos_da_geracao
import random
from mapa import Mapa
import matplotlib.pyplot as plt
import numpy as np
from fitness import fitness_func, fitness_func_2

def primeira_geracao(num_invividuos, tam_individuo_max):
    
    movimentos = ['u', 'd', 'l', 'r']
    geracao = []

    for i in range(0, num_invividuos):
        individuo = agente(i)
        tam_individuo = random.randint(1, tam_individuo_max)
        individuo.sequencia = ''.join(random.choice(movimentos) for _ in range(tam_individuo))
        geracao.append(individuo)
    return geracao

def avaliacao(geracao: list[agente], mapa: Mapa):
    pontuacao = []

    for individuo in geracao:
        # pontos = fitness_func(individuo.sequencia, mapa)
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


def myAG(tam_geracao, tam_sequencia_MAX, num_de_geracoes, mapa: Mapa, ploting: bool, text: bool):
    
    melhores_de_cada_geracao = []
    media_de_pontos_por_geracao = []

    lista_de_agentes = primeira_geracao(num_invividuos=tam_geracao, tam_individuo_max=tam_sequencia_MAX)
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
