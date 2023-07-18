from mapa import Mapa


# fitness_1

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

# fitness_2

def fitness_func_2(solution, mapa:Mapa):

    n = len(mapa.matriz)  # Tamanho da matriz
    pontuacao = 0
    pontuacao_movimento = -1  # Pontuação para cada movimento
    pontuacao_pegar_ouro = 100  # Pontuação para pegar o ouro
    pontuacao_voltar_casa = 50  # Pontuação para voltar para a casa (0, 0)
    pontuacao_morte_wumpus = -500  # Pontuação para morrer pelo Wumpus
    pontuacao_morte_buraco = -500  # Pontuação para morrer em um buraco
    
    tamanho_acoes = len(solution)
    posicao_atual = (0, 0)
    pegou_ouro = False
    cumpriu_objetivos = False
    
    # Verificar cada ação na sequência
    for i, acao in enumerate(solution):
        if acao == 'u':
            # Verificar se a ação é ir para cima
            nova_posicao = (posicao_atual[0] - 1, posicao_atual[1])
            if 0 <= nova_posicao[0] < n:
                posicao_atual = nova_posicao
                pontuacao += pontuacao_movimento
            else:
                # Movimento inválido, penalizar
                pontuacao -= 5
        elif acao == 'd':
            # Verificar se a ação é ir para baixo
            nova_posicao = (posicao_atual[0] + 1, posicao_atual[1])
            if 0 <= nova_posicao[0] < n:
                posicao_atual = nova_posicao
                pontuacao += pontuacao_movimento
            else:
                # Movimento inválido, penalizar
                pontuacao -= 5
        elif acao == 'l':
            # Verificar se a ação é ir para a esquerda
            nova_posicao = (posicao_atual[0], posicao_atual[1] - 1)
            if 0 <= nova_posicao[1] < n:
                posicao_atual = nova_posicao
                pontuacao += pontuacao_movimento
            else:
                # Movimento inválido, penalizar
                pontuacao -= 5
        elif acao == 'r':
            # Verificar se a ação é ir para a direita
            nova_posicao = (posicao_atual[0], posicao_atual[1] + 1)
            if 0 <= nova_posicao[1] < n:
                posicao_atual = nova_posicao
                pontuacao += pontuacao_movimento
            else:
                # Movimento inválido, penalizar
                pontuacao -= 5
        elif acao == 'g':
            # Verificar se a ação é pegar o ouro
            if mapa.matriz[posicao_atual[0]][posicao_atual[1]] == 'G':
                pontuacao += pontuacao_pegar_ouro
                mapa.matriz[posicao_atual[0]][posicao_atual[1]] == 0
                pegou_ouro = True
            else:
                # Pegar o ouro fora da posição inicial, penalizar
                pontuacao -= 10
        else:
            # Ação desconhecida, penalizar
            pontuacao -= 2
    
        # Verificar se o agente caiu em um buraco
        if mapa.matriz[posicao_atual[0]][posicao_atual[1]] == 'P':
            pontuacao += pontuacao_morte_buraco
            break
        
        # Verificar se o agente encontrou o Wumpus
        if mapa.matriz[posicao_atual[0]][posicao_atual[1]] == 'W':
            pontuacao += pontuacao_morte_wumpus
            break
        
        if posicao_atual == (0, 0) and pegou_ouro == True:
            if cumpriu_objetivos == False:
                    pontuacao += pontuacao_voltar_casa
                    cumpriu_objetivos = True
            else:
                pass
            

    # Verificar se a sequência é muito curta ou muito longa
    if tamanho_acoes < 10:
        pontuacao -= 10
    elif tamanho_acoes > 20:
        pontuacao -= 5
    
    # Verificar se o agente concluiu os objetivos e voltou para a casa (0, 0)
            
    
    return pontuacao