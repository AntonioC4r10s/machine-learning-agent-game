from mapa import Mapa
import random

class Agente():
    def __init__(self, mapa:Mapa):
        self.x = 0
        self.y = 0
        self.mapa = mapa
        self.mapa.posicao_agente(self.x, self.y)
        self.percepcoes, self.caminhos, self.casa = mapa.info(self.x, self.y)
        self.flecha = 1
        self.medo = 7        # de 1 a 10
        
        self.game_over = False
        self.ouro = 0
        self.capturado = False
        self.caiu = False
        self.passos = 0
        self.matou = False
        self.tiros = 0
        self.memoria = []

    def acao(self):
        percepcoes = self.percepcoes
        
        if percepcoes == []:
            self.caminha()
        
        if percepcoes.count('brilho'):
            self.ouro += 1
            self.percepcoes.remove('brilho')
        
        elif percepcoes.count('brisa'):
            self.caminha()

        elif percepcoes.count('fedor'):
            opcao = random.randint(0, 1)

            if opcao == 0:
                self.caminha()
            else:
                self.atirar()


    def caminha(self):
        proximos = self.caminhos

        conhecidos = []
        for casa in proximos:
            if casa in proximos:
                conhecidos.append(casa)

        # print('conhecidos: ', conhecidos) 
        coragem = random.randint(1, 10)

        if coragem >= self.medo or conhecidos == []:
            proximo = random.randint(0, len(proximos) - 1 )
            proxima_casa = proximos[proximo]
        
        else:
            proximo = random.randint(0, len(conhecidos) - 1 )
            proxima_casa = conhecidos[proximo]

        posicao = [self.x, self.y]
        self.memoria.append(posicao)
        self.mapa.esvazia(self.x, self.y)



        self.x = proxima_casa[0]
        self.y = proxima_casa[1]
        self.percepcoes, self.caminhos, self.casa = self.mapa.info(self.x, self.y)
        self.mapa.posicao_agente(self.x, self.y)

    
    def atirar(self):
        # print('tei!')

        if self.flecha <= 0:
            self.caminha()
        
        else:

            alvos = self.caminhos
            alvo = random.randint(0, len(alvos) - 1 )
            alvo = alvos[alvo]

            self.flecha -= 1
            self.tiros += 1

            # print(self.mapa.matriz[alvo[0]][alvo[1]])
            
            if self.mapa.matriz[alvo[0]][alvo[1]] == ('M'):
                self.mapa.esvazia(alvo[0], alvo[1])
                self.percepcoes.remove('fedor')
                self.matou = True

        
    
    def __str__(self):
        string = 'Agente: \n'
        string += f'Percepcões: {self.percepcoes}\n'
        string += f'Ouro: {self.ouro}\n'
        string += f'Game Over: {self.game_over}\n'
        string += f'Casa: {self.casa}\n'
        string += f'Capturado: {self.capturado}\n'
        string += f'Caiu: {self.caiu}\n'
        string += f'Passos: {self.passos}\n'
        string += f'Matou? {self.matou}\n'
        string += f'Tiros: {self.tiros}\n'
        
        if self.memoria != []:
            string += f'Memória: {self.memoria}\n'
        
        return string
        