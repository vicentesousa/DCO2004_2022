import warnings                                      # Método para suprimir os avisos de exceções 
warnings.filterwarnings('ignore')                    # Método para suprimir os avisos de exceções

import numpy as np
import matplotlib.pyplot as plt
import time
## Geração do sinal cosenoidal
fsampling = 10                                       # Taxa de amostragem
T =1/fsampling                                       # Tempo entre amostras
L = 2000                                             # Número de amostras
t = np.arange(0,(L-1)*T+1/fsampling,1/fsampling)     # Eixo do tempo
fm = 0.04                                            # Frequência da senoide
Am = 2                                               # Amplitude da senoide
m = Am*np.cos(2*np.pi*fm*t)                          # Sinal senoidal
# Warning for Python version before 3.8: 
# start_time = time.clock()            # Primeira medição de tempo: inicia a contagem before Python 3.8 version
start_time = time.process_time()       # Primeira medição de tempo: inicia a contagem for Python 3.8 version

## Montando a DFT
N=len(m)                                             # Comprimento do sinal m(t)
n=np.arange(0,N)                                     # Vetor n
k=np.arange(0,N)                                     # Vetor k
WN=np.exp(-1j*2*np.pi/N)                             # Cálculo de Wn = e^{-j2pi/N}
nn=np.outer(n,k)                                     # Monta a Matriz DFT
WNnk=WN**nn                                          # Monta a Matriz DFT
X=np.inner(m,WNnk.T/L)                               # Implementa o somatório da DFT via operação matricial    
f = fsampling/2*np.linspace(0,1,int((L/2)+1))             # Monta o eixo das frequências
# Medição de tempo de execução
# stop_time = time.clock()                           # Medição de tempo de execução: contagem before Python 3.8 version
stop_time = time.process_time()                      # Medição de tempo de execução contagem for Python 3.8 version
tempo_DFT = stop_time - start_time                   # Conta tempo de execução até esse ponto do código
print('Tempo da DFT = ',tempo_DFT,'s')               # Mostra tempo de execução
plt.stem(f,2*np.abs(X[0:L//2+1]))                    # Mostra gráfico do espectro 
plt.axis([0,0.1,0,2.2])                              # Zoom para melhor visualização 
plt.show()
#ipython #%whos