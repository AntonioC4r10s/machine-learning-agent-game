from mapa import Mapa


class Agente():
    def __init__(self, mapa:Mapa):
        self.x = 0
        self.y = 0
        self.mapa = mapa
        self.mapa.posicao_agente(self.x, self.y)
        self.percepcoes = mapa.info(self.x, self.y)
