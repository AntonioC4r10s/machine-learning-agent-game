# Projeto "Mundo de Wumpus"

<img src="https://cdna.artstation.com/p/assets/images/images/059/177/696/large/elijah-kuzmichov-wumpus.jpg?1675808223" alt="Wumpus" width="900">


<div style="text-align: justify;">
Este projeto tem como objetivo cumprir as etapas proposta na disciplina de Intetligẽncia Computacional e Intetligência Artificial, onde artavés da idéia do Mundo de Wumpus é abordada algumas métodos para a resolução do problema determinado pelo jogo. Abaixo temos a descrição de cada umas das etapas.<br><br>
This project aims to fulfill the steps proposed in the discipline of Computational Intelligence and Artificial Intelligence, where through the idea of the World of Wumpus some methods for solving the problem determined by the game are approached. Below is a description of each of the steps.
</div>

## Etapa 1 - Gerador aleatório de ambientes do "Mundo de Wumpus"
- [x] Tamanho (n) = Ordem (n) da matriz quadrada (n >= 3). Linha e coluna = (n - 1)
- [x] Objetos: poços (p), Wumpus (W) e ouro (o). Quantidade? 
- [x] A partir dos objetos , posicionar no ambiente, também, as percepções geradas por cada um deles.
- [x] A casa (0, 0) é a única que não pode ter nenhum objeto, pois é a posição inicial do agente.
- [x] Onde houver poço não pode ser posicionado o ouro e o Wumpus. No entanto, estes podem ser posicionados 
em quaisquer uma das outras casas.

<div style="text-align: justify;">
Nesta etapa, primeiramente foi criado uma estrutura (Classe) denominada Mapa(), onde servirá como base para a contrução de um mapa para o mundo de wumpus nas demais etapas, foram definidos os seguintes atributos para a geração de uma matriz em um mapa:
</div>

* altura 
* largura 
* número de poços 
* número de monstros 
* número de ouros

<div style="text-align: justify;">
A partir destas definições, foram criadas funções internas na classe onde foi possível definir que a cada vez que for chamado o método de crição (__init__) do método, será criado uma matriz AxL aleatória com o número pré-definido de elementos referentes ao game. Ao executar o main desta etapa, teremos por exemplo o seguinte resultado:
<div>
<br>
<p align="center">
<img src="src/etapa_1/img/print_exemplo_2.jpg" alt="Exemplo para a etapa 1" width="160">
</p>

Ou seja, é gerada a matriz e é exibida as suas caractristicas e a representação da mesma ao usuário.



## Etapa 2 - Agente Reativo (versão 1)
- [x] O comportamento do agente é definido a partir de seu conjuntos de regras:
      Se <percepções> então <ação>
- [x] Este conjunto de regras (ou base de conhecimento) deve ser especificado por meio de uma tabela.
- [x] A partir da especificação, o próximo passo é codificar o agente e integrar o 'gerador aleatório de ambientes', de forma a possibilitar a realização de testes de validação para posterior avaliação de peformance.

## Etapa 3 - Agente Reativo (versão 2)
- [x] Estrutura de memória, que pode ser: uma lista; uma matriz - réplica do ambiente, com anotações feitas pelo agente; ou, outra estrutura de dados definida como mais adequada pela equipe.
- [x] Mecanismo mais inteligente para escolha da regra a ser aplicada, em caso de duas ou mais possíveis de serem utilizadas em determinado instante. Na primeira versão foi utilizada a Estratégia Aleatória. Logo, há liberdade para definir a melhor estratégia para essa finalidade.
- [x] Além disso, uso do conhecimento registrado na memória para auxiliar o processo de escolha da regra a ser aplicada (Inferência? Planejamento?).

## Etapa 4 - Agente de Aprendizagem
- [x] O mecanismo utilizado para a aprendizagem do Agente do Mundo de Wumpus deve ser idealizado e projetado via Algoritmos Genéticos para, posteriormente, ser codificado;
- [x] Cada componente ou processo do Algoritmo Genético deverá ser projetado com o foco na resolução do problema de “sair da casa (0,0), pegar o ouro e voltar à casa (0,0)';
- [x] Além do caminhando, deverão ser considerados os poços, ouro e wumpus (até o momento, temos um gerador aleatório de ambientes com dimensão n > 3);

