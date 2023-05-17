from mapa import Mapa
import random

class Agente():
    def __init__(self, mapa:Mapa):
        self.x = 0
        self.y = 0
        self.mapa = mapa
        self.mapa.posicao_agente(self.x, self.y)
        self.percepcoes, self.caminhos, self.casa = mapa.info(self.x, self.y)
        
        self.game_over = False
        self.ouro = 0
        self.capturado = False
        self.caiu = False
        self.passos = 0

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
            self.caminha()
    
    # def reacao(self):
    #     reacao = self.casa

    #     print('reacao', reacao)
        
    #     if reacao == 'P':
    #         self.game_over = True
    #     if reacao == 'M':
    #         self.game_over = True
        


    def caminha(self):
        # print('caminha')
        proximos = self.caminhos
        proximo = random.randint(0, len(proximos) - 1 )
        # print("proximo", proximo)
        proxima_casa = proximos[proximo]

        self.mapa.esvazia(self.x, self.y)

        self.x = proxima_casa[0]
        self.y = proxima_casa[1]
        self.percepcoes, self.caminhos, self.casa = self.mapa.info(self.x, self.y)
        self.mapa.posicao_agente(self.x, self.y)

    def __str__(self):
        string = 'Agente: \n'
        string += f'Percepcões: {self.percepcoes}\n'
        string += f'Ouro: {self.ouro}\n'
        string += f'Game Over: {self.game_over}\n'
        string += f'Casa: {self.casa}\n'
        string += f'Capturado: {self.capturado}\n'
        string += f'Caiu: {self.caiu}\n'
        string += f'Passos: {self.passos}\n'

        return string
        