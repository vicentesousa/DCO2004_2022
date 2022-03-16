import numpy as np
import matplotlib.pyplot as plt

## Geração do sinal cosenoidal
fsampling = 10                                               #Taxa de amostragem
tf = 200                                                     #Tempo entre amostras
t =  np.arange(0,tf+1/fsampling,1/fsampling)                 #Eixo do tempo
fm = 0.04                                                    #Frequência da senoide
Am = 2                                                       #Amplitude da senoide
m = Am*np.cos(2*np.pi*fm*t)                                  #Sinal senoidal

## Plot do sinal M(f): single-sided amplitude spectrum.
# Visualizando a amplitude do espectro com um tamanho arbitrário para a fft
lfft = 1000
## Construção do single-sided amplitude spectrum.
yfft = np.fft.fft(m,lfft)/lfft                               # Cálculo da FFT via função do Matlab
freq1 = np.arange(0,fsampling/2,fsampling/lfft)              # Definição do eixo das frequências unilateral
yfftuni = yfft[0:lfft//2]                                    # Coleta da FFT unilateral

plt.figure(1,[10,7])
plt.subplot(121)
plt.stem(freq1,np.abs(yfftuni))                              # Plotagem do espectro unilateral M(f)
plt.title('Espectro unilateral')                             # Configuração do título do gráfico 
plt.xlabel('Frequencia (kHz)')                               # Configuração do eixo x do gráfico 
plt.ylabel('|M(f)|')                                         # Configuração do eixo y do gráfico  
plt.grid()                                                   # Adiona o grid  
plt.axis([0,0.1,0,1.2])                                      # Zoom do gráfico

## Plot do sinal M(f): double-sided amplitude spectrum.
# Colocando as frequência no lado esquerdo 
plt.subplot(122)
## Construção do double-sided amplitude spectrum.
lfftd = 1000
yfftd = np.fft.fft(m,lfftd)/lfftd                            # Cálculo da FFT via função do Matlab
yfftd = np.fft.fftshift(yfft)
# Definição do eixo das frequências unilateral
freqd = np.fft.fftfreq(lfftd,1/fsampling)
freqd = np.fft.fftshift(np.fft.fftfreq(lfftd,1/fsampling))
plt.stem(freqd,np.abs(yfftd))                                # Plotagem do espectro unilateral M(f)
plt.title('Espectro bilateral')                              # Configuração do título do gráfico 
plt.xlabel('Frequencia (kHz)')                               # Configuração do eixo x do gráfico 
plt.ylabel('|M(f)|')                                         # Configuração do eixo y do gráfico  
plt.grid()                                                   # Adiona o grid  
plt.axis([-0.05,0.05,0,1.2])                                 # Zoom do gráfico

plt.show()