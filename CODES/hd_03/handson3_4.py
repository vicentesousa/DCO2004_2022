import numpy as np
import matplotlib.pyplot as plt
## Geração do sinal cosenoidal
fsampling = 10                                               #Taxa de amostragem
tf = 200                                                     #Tempo entre amostras
t =  np.arange(0,tf+1/fsampling,1/fsampling)                 #Eixo do tempo
fm = 0.04                                                    #Frequência da senoide
Am = 2                                                       #Amplitude da senoide
m = Am*np.cos(2*np.pi*fm*t)                                  #Sinal senoidal

## Visualizando a amplitude do espectro com um tamanho arbitrário para a FFT
plt.figure(1,[10,7])                                         #instância de figure, de número 1 e tamanho 10x7

lfft = 1000                                                  # Tamanho da FFT
yfft = np.fft.fft(m,lfft)/lfft                               # Cálculo da FFT via função do Matlab
freq1 = np.arange(0,fsampling/2,fsampling/lfft)              # Definição do eixo das frequências unilateral
yfftuni = yfft[0:lfft//2]                                    # Coleta da FFT unilateral


## Visualizando a amplitude do espectro com um tamanho arbitrário para a FFT
lfft2 = 512                                                  # Tamanho da FFT
yfft2 = np.fft.fft(m,lfft2)/lfft2                            # Cálculo da FFT via função do Matlab
freq2 = np.arange(0,fsampling/2,fsampling/lfft2)             # Definição do eixo das frequências unilateral
yfftuni2 = yfft2[0:lfft2//2]                                 # Coleta da FFT unilateral


## Gráficos com a função plt.plot()
plt.figure(1,[10,7])
plt.subplot(211)
plt.plot(freq1,np.abs(yfftuni))                              # Plotagem do espectro unilateral M(f)
plt.grid()
plt.title('Tamanho da FFT = '+str(lfft))
plt.axis([0,0.1,0,1.2])

plt.subplot(212)
plt.plot(freq2,np.abs(yfftuni2))                             # Plotagem do espectro unilateral M(f)
plt.grid()
plt.title('Tamanho da FFT = '+str(lfft2))
plt.axis([0,0.1,0,1.2])



#Gráficos com a função pĺt.stem()
plt.figure(2,[10,7])
plt.subplot(211)
plt.stem(freq1,np.abs(yfftuni))                              # Plotagem do espectro unilateral M(f)
plt.grid()
plt.title('Tamanho da FFT = '+str(lfft))
plt.axis([0,0.1,0,1.2])

plt.subplot(212)
plt.stem(freq2,np.abs(yfftuni2))                             # Plotagem do espectro unilateral M(f)
plt.grid()
plt.title('Tamanho da FFT = '+str(lfft2))
plt.axis([0,0.1,0,1.2])

plt.show() 

