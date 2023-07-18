from mapa import Mapa
import numpy as np
import random
from agente import agente, imprimir_individuos, media_de_pontos_da_geracao
from myag import myAG
import keyboard

# Definindo as propriedades do mundo e as imprimindo
altura = 5
largura = 5
pocos = 2
wumpus = 1
ouros = 1

print(f'Altura = {altura}')
print(f'Largura = {largura}')
print(f'Poços = {pocos}')
print(f'Wumpus = {wumpus}')
print(f'Ouros = {ouros}')
print('\n')

# Criando um mundo (mapa) que seja utilizável
while(True):
    mapa = Mapa(altura, largura, pocos, wumpus, ouros)
    if((mapa.info(0, 1) == 'P' or mapa.info(0, 1) == 'M') and (mapa.info(1, 0) == 'P' or mapa.info(1, 0) == 'M')):
        pass
    else:
        break

print(mapa)

myAG(tam_geracao=100, 
     tam_sequencia_MAX=40, 
     num_de_geracoes=50, 
     mapa=mapa,
     ploting=True,
     text=True)


