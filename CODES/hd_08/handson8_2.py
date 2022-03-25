# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#
## Parâmetros
SNR_dB = 5                                              # SNR de entrada em dB
t = np.arange(0,0.5,0.0001)                              # Eixo do tempo
Ar = 2                                                   # Amplitude da parte real
Ai = 0.2                                                 # Amplitude da parte imaginária
fx = 10                                                  # Frequência da onda
x=Ar*np.cos(2*np.pi*fx*t)  + 1j*Ai*np.cos(2*np.pi*fx*t)  # Sinal qualquer x(t)
#
## Gearação das amostras do ruído complexo
N = len(x)                                               # Tamanho de x
Ps = np.sum(np.abs(x)**2)/N                              # Calcula a potência do sinal
SNR = 10**(SNR_dB/10)                                    # Calcula a SNR linear
Pn = Ps/SNR                                              # Calcula a potência do ruído
sigmaNormalizado = np.sqrt(Pn/2)                         # Desvio padrão normalizado do ruído complexo
#
media=0.0
nr = np.random.normal(media,sigmaNormalizado,N)          # Amostras da parte real do ruído 
ni = np.random.normal(media,sigmaNormalizado,N)          # Amostras da parte imaginária do ruído 
n = nr + 1j*ni                                           # Ruído complexo
y = x + n                                                # Sinal complexo ruidoso
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
# Gráficos: como se trata de sinal complexo, vamos mostrar sua magnitude
#
plt.figure(1,[10,7])
#
plt.subplot(311)
plt.title("Sinal original")
plt.plot(t,np.abs(x))
#
plt.subplot(312)
plt.title("Ruído AWGN")
plt.plot(t,np.abs(n))
#
plt.subplot(313)
plt.title("Sinal com ruído AWGN")
plt.plot(t,np.abs(y))
#
plt.tight_layout()
plt.show()