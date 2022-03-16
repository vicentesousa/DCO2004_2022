import warnings                                      # Método para suprimir os avisos de exceções 
warnings.filterwarnings('ignore')                    # Método para suprimir os avisos de exceções

#Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt


## Geração do sinal cosenoidal
fsampling = 10                                     # Taxa de amostragem  (kHz)
tf = 200                                           # Tempo final 
t = np.arange(0,tf+1/fsampling,1/fsampling)        # Vetor tempo discreto, obedecendo o tempo de amostragem
fm = 0.04                                          # Frequência do sinal senoidal
Am = 2                                             # Amplitude do sinal senoidal
m = Am*np.cos(2*np.pi*fm*t)                        # Geração de amostras do sinal senoidal

plt.figure(figsize=(10,7))                         # Configura o tamanho da figura

plt.plot(t,m,'b',linewidth=2)                      # Plota gráfico do coseno com taxa de amostragem fsampling
plt.xlabel('Tempo')                                # Definição do texto do eixo X
plt.ylabel('Amplitude')                            # Definição do texto do eixo Y 
plt.grid()                                         # Desenhar o grid do gráfico                           

## Gráfico do coseno com nova taxa de amostragem = 0.08 (o dobro da banda do sinal)
fsampling = 0.08                                   # Taxa de amostragem (kHz)
t2 = np.arange(0,tf+1/fsampling,1/fsampling)       # Geração de amostras do sinal m(t) com nova taxa de amostragem
m2 = Am*np.cos(2*np.pi*fm*t2)                      # Geração de amostras do sinal m(t) com nova taxa de amostragem    
plt.plot(t2,m2,'r-s',linewidth=2)                  # Plota com nova taxa de amostragem (linha com marcador quadrado) 

## Gráfico do coseno com nova taxa de amostragem = 0.04 (igual a banda do sinal)
fsampling = 0.04                                   # Taxa de amostragem (kHz)
t3 = np.arange(0,tf+1/fsampling,1/fsampling)       # Geração de amostras do sinal m(t) com nova taxa de amostragem
m3 = Am*np.cos(2*np.pi*fm*t3)                      # Geração de amostras do sinal m(t) com nova taxa de amostragem
plt.plot(t3,m3,'k-o',linewidth=2)                  # Plota com nova taxa de amostragem (linha com marcador circular) 
plt.legend(['Taxa de amostragem = 10 kHz',         # Adiciona legenda ao gráfico
'Taxa de amostragem = 0.08 kHz',
'Taxa de amostragem = 0.04 kHz'])                  
plt.title('Sinal coseno com frequência = 0.04 kHz')# Adiciona título ao gráfico

plt.axis([0,2*1/fm,-3,4])                          # Zoom em dois períodos da onda

plt.show()
# A função 'whos' é responsável por mostrar todas as variáveis que foram criadas no workspace,
# identificando suas principais caracteristicas.
#ipython #%whos