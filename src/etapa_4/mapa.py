import random

class Mapa():
    def __init__(self, altura, largura, num_pocos, num_monstros, num_ouros):
        self.altura = altura
        self.largura = largura
        self.num_pocos = num_pocos
        self.num_monstros = num_monstros
        self.num_ouros = num_ouros
        self.matriz = [[0 for i in range(altura)] for j in range(largura)]
        
         # Adiciona poços
        for _ in range(num_pocos):
            self._adiciona_elemento_aleatorio('P')
        
        # Adiciona monstros
        for _ in range(num_monstros):
            self._adiciona_elemento_aleatorio('M')
        
        # Adiciona ouros
        for _ in range(num_ouros):
            self._adiciona_elemento_aleatorio('G')

        
    def _adiciona_elemento_aleatorio(self, elemento):
        while True:
            x = random.randint(0, self.altura-1)
            y = random.randint(0, self.largura-1)
            if (x, y) != (0, 0) and self.matriz[x][y] == 0:
                self.matriz[x][y] = elemento
                return

    def info(self, x, y):
        coordenada_vizinhos = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

        vizinhos = []
        percepcao = []
        caminhos = []
        casa = []

        try:
            casa.append(self.matriz[x][y])
        except:
            pass

        for coordenada in coordenada_vizinhos:
            try:
                if self.matriz[coordenada[0]][coordenada[1]] != 0 and coordenada[0] >= 0 and coordenada[1] >= 0:
                    vizinhos.append(self.matriz[coordenada[0]][coordenada[1]])
            except:
                pass

        for coordenada in coordenada_vizinhos:
            try:
                if coordenada[0] >= 0 and coordenada[1] >= 0:
                    caminhos.append([coordenada[0], coordenada[1]])
            except:
                pass

        if(vizinhos.count('M')):
            percepcao.append('fedor')
        if(vizinhos.count('P')):
            percepcao.append('brisa')
        
        if(casa.count('G')):
            percepcao.append('brilho')

        # print(f'coordenada [{x}]x[{y}]')
        # print(f'elementos na casa atual: {casa}')
        # print(f'vizinhos: {vizinhos}')
        # print(f'percepções: {percepcao}')

        for caminho in caminhos:
            if caminho[0] >= self.altura or caminho[1] >= self.altura:
                caminhos.remove(caminho)

        # return percepcao, caminhos, casa
        return casa[0]

    def __str__(self):
        string = ''
        for linha in reversed(self.matriz):
            for elemento in linha:
                string = string + str(elemento) + ' '
            string = string + '\n'
        return string
    
    
    def posicao_agente(self, x, y):
        self.matriz[x][y] = 'A'

    def esvazia(self, x, y):
        self.matriz[x][y] = 0

# altura, largura, num_pocos, num_monstros, num_ouros
# mapa = Mapa(3,3,2,1,1)
# print(mapa)
# mapa.info(1, 0)