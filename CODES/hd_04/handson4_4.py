import scipy.signal as sci
import numpy as np
import matplotlib.pyplot as plt
## Parâmetros do sinal 
fc=0.04                              # Frequência do seno
Fs=10                                # Frequência de amostragem
Ts = 1/Fs                            # Tempo entre amostras
A = 10                               # Amplitude do sinal
nC = 2000                            # Número de períodos da onda   
t=np.arange(0,nC/fc,Ts)              # Vetor tempo
x=A*np.cos(2*np.pi*fc*t)             # Gera o sinal x(n)
N = len(x)                           # Número de amostras do sinal

Nfft = 1000
Xfft=np.fft.fft(x,Nfft)              # Encontra a FFT
Xfft = np.array_split(Xfft,2)[0]
f=np.arange(0,0.5*Fs,Fs/Nfft)        # Eixo da frequência
plt.figure(1,[8,6])
plt.subplot(311)
plt.stem (f,abs(Xfft)/Nfft)          # Plota a espectro
plt.title('FFT do sinal')            # Configura título
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid()
plt.axis([0,2*fc,0,A**2/4])          # Zoom no gráfico


from spectrum.window import Window
hamming = Window(len(x),name='hamming')
f,pxx = sci.periodogram(x,window=hamming.data,fs=Fs,nfft=len(x),scaling='spectrum')
pwrest = pxx.max()
idx = pxx.argmax()

plt.subplot(312)
plt.plot(f,pxx)
plt.title('Periodograma')
plt.xlabel('Frequência')
plt.ylabel('Potência (W)')
plt.grid()
plt.axis([0,2*fc,0,A**2])

print('A potência máxima ocorre em ',f[idx],' Hz')
print('A potência estimada é',pwrest)

plt.subplot(313)
#construindo todo o procedimento com as funções da spectrum
import spectrum as spec 
data = spec.data_cosine(N=len(x), A=10, sampling=Fs, freq=fc)
p = spec.Periodogram(x, sampling=Fs,window='hamming')
p.run() #Recomputa a psd caso 'x' tenha sido alterado
p.plot()
plt.title("Periodograma (dB) da Spectrum")

plt.tight_layout()
plt.show()