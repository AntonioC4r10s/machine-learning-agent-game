from mapa import Mapa


altura = 4
largura = 4
pocos = 2
wumpus = 1
ouros = 1

print(f'Altura = {altura}')
print(f'Largura = {largura}')
print(f'Poços = {pocos}')
print(f'Wumpus = {wumpus}')
print(f'Ouros = {ouros}')
print('\n')

mapa = Mapa(altura, largura, pocos, wumpus, ouros)

print(mapa)