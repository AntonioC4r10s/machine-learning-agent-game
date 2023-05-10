from mapa import Mapa
from agente1 import Agente

# altura, largura, num_pocos, num_monstros, num_ouros
mapa = Mapa(3,3,2,1,1)
print(mapa)

agente = Agente(mapa)
print(mapa)
print(agente.percepcoes)