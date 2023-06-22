class agente():
    def __init__(self, id):
        self.id = id
        self.sequencia = []
        self.pontos = 0


    def __str__(self):
        string = f'Individuo {self.id} - Pontuação: {self.pontos} - sequencia: {self.sequencia}'
        
        return string

def imprimir_individuos(geracao: list[agente]):
    i = 0
    print("\n")
    for individuo in geracao:
        print(f'{i}' , individuo)
        i += 1

def media_de_pontos_da_geracao(geracao: list[agente]):

    media = 0
    i = 0
    for individuo in geracao:
        media += individuo.pontos
        i += 1
    media = media/len(geracao)
    return media