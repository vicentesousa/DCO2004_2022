import numpy as np
from matplotlib import pyplot as plt
M =1000                                # Número de atrasos
N =1000                                # Número de amostras
f1=10                                  # Frequência do seno (kHz)
Fs=2000                                # Frequência de amostragem (kHz)
n =np.arange(0,N)                      # Vetor com índices de amostra
Am=5                                   # Determina a amplitude
x=Am*np.sin(2*np.pi*f1*n/Fs)           # Gera o sinal x(n)
t=np.arange(1,N+1)*(1/Fs)              # Definiçao do eixo do tempo
#implementaçao:
def xcorr(sinal):
    N = len(sinal)
    rxx = np.zeros([N],dtype = float)
    for m in range(N):
        for n in range(N-m):
            rxx[m] = rxx[m]+x[n]*x[n+m]
    rxx = rxx/N
    return rxx
Rxx = xcorr(x)
#Plotagem:
plt.figure(1,[8,6])
#Plota x[n]
plt.subplot(211)
plt.title("Sinal senoidal")
plt.ylabel("Amplitude")
plt.xlabel("Tempo [s]")
plt.grid()
plt.axis([0,0.5,-5,5])
plt.plot(t,x)
#Plota Autocorrelação
plt.subplot(212)
plt.plot(Rxx)
plt.xlabel("Atrasos")
plt.ylabel("Autocorrelação")
plt.title("Autocorrelação do sinal senoidal")
plt.grid()

plt.tight_layout()
plt.show()