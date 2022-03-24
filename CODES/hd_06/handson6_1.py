# Parâmetros
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift

# Criação das funções, por questão de organização
def downsample(array,rate):
    return array[::rate]

def upsample(array,rate):
    from numpy import zeros
    ret =  zeros(rate*len(array))
    ret[::rate] = array 
    return ret

T=0.002                                                 # Taxa de amostragem (500kHz)
Tf=1                                                    # Tempo final em segundos
t= np.arange(0,Tf,T)                                    # Definição do eixo do tempo      
fm1=3                                                   # Frequência senoide 1      
fm2=1                                                   # Frequência senoide 2
m_t=np.sin(2*np.pi*fm2*t)-np.sin(2*np.pi*fm1*t)         # Sinal mensagem m(t)
ts=0.02                                                 # Nova taxa de amostragem
N_samp=round(ts/T)                                      # Número de elementos 
# T/ts deve ser, preferencialmente, inteiro.

## Amostragem 
s_out=downsample(m_t,N_samp)                            # Coleta 1 amostra a cada N_samp=10 amostras do sinal  
s_out=upsample(s_out,N_samp)                            # Retorna vetor amostrado com o número inicial de elementos

## Espectro
lfft=len(m_t)                                           # Comprimento da fft
M_f=fftshift(fft(m_t,lfft)/lfft)                        # Sinal m_t na frequência 
S_out=fftshift(fft(s_out,lfft)/lfft)                    # Sinal s_out na frequência
Fs=1/T 
freq = np.arange(-Fs/2,Fs/2,Fs/lfft)

#plotting
plt.figure(1,[10,2])
#
plt.plot(t,s_out,t,m_t)
plt.title("Sinal Original e Sinal Amostrado")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
#plt.show()
plt.figure(2,[9,2])
#
#
plt.subplot(121)
plt.plot(freq,np.abs(M_f))
plt.xlim([-50,50])
plt.ylim([0,0.6])
plt.title("M(f)")
#
plt.subplot(122)
plt.plot(freq,np.abs(S_out))
plt.title("M(f) do sinal amostrado")
plt.xlim([-120,120])
plt.ylim([0,0.06])
#
plt.tight_layout()
plt.show()