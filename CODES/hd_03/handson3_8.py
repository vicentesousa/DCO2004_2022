from spectrum.window import Window
from matplotlib import pyplot as plt 
import numpy as np

N  = 256                               #número de amostras 
N1 = 1024                              #número de pontos da fft
fs = 128                               #frequência de amostragem (Hz)
f1 = 30                                #frequência do sinal (Hz)        
n  = np.arange(0,N)                    #index n
x  = np.cos(2.0*f1*np.pi*n/fs)         #gerando o sina
f  = np.arange(0,N1)*fs/N1;            #definição do eixo da frequência
h = Window(N, name= 'hamming')         #janela hamming
r = np.ones(N)                         #janela retangular

XR = np.fft.fft(x,N1)                  #fft 
XR = np.abs(XR)/N1                     #normalização
XH = x*h.data                          #janelamento
XH = np.fft.fft(XH,N1)                 #fft 
XH = np.abs(XH)/N1                     #normalização

plt.figure(1,[8,5])

#Sinal sem janela (retangular)
plt.subplot(211)
plt.plot(f[:N1//2],20.0*np.log10(XR[:N1//2]/max(XR)))
plt.axis([f[0],f[N1//2],-300,0])
plt.grid()
plt.title("Espectro de x(t) com janela tipo retangular")
plt.ylabel("Amplitude (dB)")

#Sinal com janela Hamming
plt.subplot(212)
plt.plot(f[:N1//2],20.0*np.log10(XH[:N1//2]/max(XH)))
plt.axis([f[0],f[N1//2],-300,0])
plt.grid()
plt.title("Espectro de x(t) com janela tipo Hamming")
plt.ylabel("Amplitude (dB)")

plt.tight_layout()
plt.show()