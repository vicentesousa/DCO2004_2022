# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#
## Parâmetros
EbN0_dB = 0                                           # Eb/N0 de entrada
Ns = 10**5                                             # Número de símbolos simulados
#
# Sinal BPSK gerado manualmente
bits = np.random.rand(1,Ns) > 0.5                      # Gera 0s e 1s com mesma probabilidade
simbolo = 2*bits-1                                     # Modulação BPSK: 0 -> -1; 1 -> 1 
sigmaRuido = 10**(-EbN0_dB/(2*10))                     # Desvio padrão do ruído AWGN 
sigmaNorm = sigmaRuido/np.sqrt(2)                      # Amostras do ruído AWGN
media = 0.0
nr = np.random.normal(media,sigmaNorm,Ns)              # Amostras da parte real do ruído 
ni = np.random.normal(media,sigmaNorm,Ns)              # Amostras da parte imaginária do ruído 
n = nr + 1j*ni                                         # Ruído complexo
y = simbolo + n                                        # Sinal ruidoso
#
# Gráficos
plt.figure(1,[7,7])
index1s = np.nonzero(simbolo.real>0)
index0s = np.nonzero(simbolo.real<=0)
plt.plot(y[index1s].real,y[index1s].imag,'ro')
plt.plot(y[index0s].real,y[index0s].imag,'bs')
plt.title("Diagrama de constelação BPSK")
plt.legend(["Bit 1 transmitido","Bit 0 transmitido"]);
#
plt.axis('equal')
plt.show()