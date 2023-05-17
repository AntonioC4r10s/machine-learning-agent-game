from mapa import Mapa
from agente1 import Agente


agentes = []
numero_de_ciclos = int(input('Número de ciclos: '))
i = 0

while(i < numero_de_ciclos):

    # altura, largura, num_pocos, num_monstros, num_ouros
    mapa = Mapa(4,4,2,1,1)
    # print(mapa)
    agente = Agente(mapa)

    # print("-------------------------------------------------")

    while(True):
        # print('ciclo', agente.passos)

        # print(mapa)
        # print(agente.percepcoes)
        # print(agente.caminhos)
        # print('Ouro', agente.ouro)
        # print('GO', agente.game_over)

        
        # print('casa: ', agente.casa)

        if agente.casa.count('P'):
            agente.game_over = True        
            agente.caiu = True
            break

        if agente.casa.count('M'):
            agente.game_over = True        
            agente.capturado = True
            break

        agente.acao()
        agente.passos += 1
        # print('\n')

    agentes.append(agente)
    i += 1
    # print(mapa)
    # print(agente)



# Estatísticas:

# números brutos
n_caiu = 0
n_capturado = 0
n_ouro = 0
n_passos = 0


for agente in agentes:
    if agente.caiu == True:
        n_caiu += 1
    
    if agente.capturado == True:
        n_capturado += 1

    if agente.ouro > 0:
        n_ouro += 1

    n_passos = n_passos + agente.passos

print(f'Mortes em Poço: {n_caiu}    {n_caiu*100/numero_de_ciclos:.2f}%')
print(f'Mortes em Monstro: {n_capturado}    {n_capturado*100/numero_de_ciclos:.2f}%')
print(f'Coletas de ouro: {n_ouro}    {n_ouro*100/numero_de_ciclos:.2f}%')
print(f'Passos Totais: {n_passos}    media: {n_passos/numero_de_ciclos:.2f}')