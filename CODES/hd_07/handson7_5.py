lQuadrado = 5                                         # Comprimento do quadrado
rCirculo = lQuadrado                                  # Raio do circulo
vtPontos = [1e3,1e4,1e6]                              # 3 números de precisão : 1000, 10000, 1000000

import numpy as np
import matplotlib.pyplot as plt
for ik in range(0,len(vtPontos)):
    nPontos = vtPontos[ik]
    # Pocisionar ponto no quadrado: Mutiplicando um número aleatório de 0 a
    # 1 pelo comprimento do quadrado para distribuir aleatoriamente nas
    # duas dimenções.
    vtSamples = lQuadrado*np.random.rand(1,int(nPontos)) + 1j*lQuadrado*np.random.rand(1,int(nPontos))
    # Testa: 
    # Caso o modulo do vetor > raio do circulo --> 0 
    # Caso o modulo do vetor <= raio do circulo --> 1  
    indexPontCirculo =  np.abs(vtSamples) <= rCirculo 
    # Encontra o numero de elementos dentro da area do circulo.
    razaoArea = len(indexPontCirculo[indexPontCirculo>0])/nPontos
    # Multiplica por 4 pois foi realizado apenas para 1/4 da area do circulo
    valordePi = 4*razaoArea
    # Retorna o valor de pi estimado  
    plt.figure()
    plt.title("Simulação com "+str(nPontos)+" elementos")
    vtPontosCirculo = vtSamples[indexPontCirculo]    
    plt.scatter(vtPontosCirculo.real,vtPontosCirculo.imag)
    plt.show()
    print( ' --------Experimento {} ---------------'.format(ik))
    print("Valor real de pi = ",np.pi)
    print(' - Número de pontos = ', nPontos )
    print(' - Razão entre as areas =  ', razaoArea)
    print( ' - pi estimado =  ' , valordePi)
    print( ' - Erro =  ' ,np.pi-valordePi)      