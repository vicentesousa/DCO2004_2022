# AWGN_Real.m
## Parâmetros
import numpy as np
import matplotlib.pyplot as plt
#
SNR_dB = 10                                    # Determina o valor da SNR em dB
t = np.arange(0,5,0.0001)                      # Eixo do tempo
A = 2                                          # Amplitude do sinal de entrada x(t)
x=A*np.cos(2*np.pi*10*t)                       # Sinal qualquer x(t)
#
## Montagem do vetor ruído 
N = len(x)                                     # Calcula o comprimento de x
Ps = np.sum(np.abs(x)**2)/N                    # Calcula a potência do sinal
SNR = 10**(SNR_dB/10)                          # Calcula a SNR linear
Pn = Ps/SNR                                    # Calcula a potência do ruído
noiseSigma = np.sqrt(Pn)                       # Desvio padrão  para ruído AWGN (amostras reais)
# Geração manual das amostras de ruído 
media = 0.0
desvio_padrao=1.0
n = np.random.normal(media,noiseSigma,N)       # Amostras de ruído 
y = x + n                                      # Sinal Ruidoso
#
# Estimação da SNR pelas amostras do sinal recebido
pTx = (np.linalg.norm(x)**2)/N                 # Potência do sinal x(t)
pNe = (np.linalg.norm(n)**2)/N                 # Potência estimada do ruído
SNR1 = pTx/pNe;                                # Estimação da SNR linear
SNR1= 10*np.log10(SNR1)                        # SNR em dB
#
# Mostrar informações
print('Estimação de SNR: ')
print('   SNR de entrada: {} dB'.format(SNR_dB))
print('   Estimação da SNR pelas amostras do sinal recebido: {} dB'.format(SNR1))

## Gráficos
plt.figure(1,[7,5])
#
plt.subplot(311)
plt.title("Sinal original")
plt.plot(t,x)
plt.xlim([0,1]) 
#
plt.subplot(312)
plt.title("Sinal com ruído AWGN")
plt.plot(t,y)
plt.xlim([0,1]) 
#
plt.subplot(313)
plt.title("Ruído AWGN")
plt.plot(t,n)
plt.xlim([0,1]) 
#
plt.tight_layout()
plt.show()