import numpy as np
from matplotlib import pyplot as plt
import scipy.fftpack as ff
from scipy import signal

ts = 1e-4
fs = 1/ts
t = np.arange(0,5000,1)*ts
fc = 500
fm = 150                                                   # Frequencia do sinal
Am=1                                                       # Amplitude do sinal senoidal
Ac=1                                                       # Amplitude da portadora
carrierc = Ac*np.cos(2*np.pi*fc*t)                         # Sinal portadora cosseno
carriers = Ac*np.sin(2*np.pi*fc*t)                         # Sinal portadora seno
m1_t = Am*np.cos(2*np.pi*fm*t)*np.exp(-t*5)                # Sinal mensagem
m2_t = Am*np.exp(-t*40)                                    # Sinal mensagem

lfft = len(t)                                              # FFT com o mesmo comprimento do sinal (t , m1_t e m2_t)
lfft = int(2**np.ceil(np.log2(lfft)+1))
freqm = np.arange(-fs/2,fs/2,fs/lfft)
M1 = ff.fftshift(ff.fft(m1_t,lfft)/np.sqrt(lfft))          # Sinal m1_t na frequência
M2 = ff.fftshift(ff.fft(m2_t,lfft)/np.sqrt(lfft))          # Sinal m2_t na frequência

# Modulação QAM
# Modulação - Soma de duas DSB-SC ortogonais
x_qam = (m1_t)*(carrierc)+(m2_t)*(carriers)                # Sinal QAM no tempo
# Sinal na frequência
X_QAM=ff.fftshift(ff.fft(x_qam,lfft,axis=0)/lfft)          # Sinal QAM na frequência
# Demodulação
# Separando os sinais
m1_dem = x_qam*np.cos(2*np.pi*fc*t)*2                      # Demodulando m1_t
m2_dem = x_qam*np.sin(2*np.pi*fc*t)*2                      # Demodulando m2_t

M1_dem = ff.fftshift(ff.fft(m1_dem,lfft)/np.sqrt(lfft))    # m1_t na frequência antes da filtragem
M2_dem = ff.fftshift(ff.fft(m2_dem,lfft)/np.sqrt(lfft))    # m2_t na frequência antes da filtragem

# Geração do filtro e filtragem do sinal
B_m = 150                                                  # Banda do filtro
a = 1                                                      # Numerador
b = signal.firwin(40, cutoff=B_m*ts, window='hamming')     # Denominador
m1_rec=signal.lfilter(b,a,m1_dem)                          # Filtrando m1_dem 
M1_rec=ff.fftshift(ff.fft(m1_rec,lfft)/np.sqrt(lfft))      # Espectro do sinal demodulado m1_rec 
m2_rec=signal.lfilter(b,a,m2_dem)                          # Filtrando m2_dem
M2_rec=ff.fftshift(ff.fft(m2_rec,lfft)/np.sqrt(lfft))      # Espectro do sinal demodulado m2_rec
m1_rec = (max(m1_t)/max(m1_rec))*m1_rec                    # Amplificando o sinal m1_rec
m2_rec = (max(m1_t)/max(m2_rec))*m2_rec                    # Amplificando o sinal m2_rec

# Graficos dos sinais no tempo
plt.figure(1,[10,7])
# Sinal QAM
plt.subplot(411)
plt.title("Sinal QAM no tempo")
plt.plot(t,x_qam)
plt.xlim([0,0.08])
# Sinal m1(t) demodulado
plt.subplot(412)
plt.title("Sinal em fase (m$_1$(t)) - Tempo")
plt.plot(t,m1_t,t,m1_rec)
plt.legend(["m$_1$(t) original","m$_1$(t) demodulado"])
plt.xlim([0,0.08])
# Sinal m2(t) demodulado
plt.subplot(413)
plt.title("Sinal em quadratura (m$_2$(t)) - Tempo")
plt.plot(t,m2_t,t,m2_rec)
plt.legend(["m$_2$(t) original","m$_2$(t) demodulado"])
plt.xlim([0,0.08])

## Gráficos do espectro
# Espectro do sinal QAM
plt.subplot(414)
plt.title("Espectro do sinal QAM")
plt.plot(freqm,np.abs(X_QAM))
plt.xlim([-1500,1500])
plt.tight_layout()
plt.show()

plt.figure(2,[10,7])
# m1(t)*c(t) não filtrado
plt.subplot(221)
plt.title("m$_1$(t)*c(t) não filtrado")
plt.plot(freqm,np.abs(M1_dem))
plt.xlim([-1500,1500])
# m1(t)*c(t) filtrado = m1(t) recuperado
plt.subplot(223)
plt.title("m$_1$(t) original vs recuperado")
plt.plot(freqm,np.abs(M1),freqm,np.abs(M1_rec))
plt.legend(["Original","Demodulado"])
plt.xlim([-1500,1500])
# m2(t)*c(t) não filtrado
plt.subplot(222)
plt.title("m$_2$(t)*c(t) não filtrado")
plt.plot(freqm,np.abs(M2_dem))
plt.xlim([-1500,1500])
# m1(t)*c(t) filtrado = m1(t) recuperado
plt.subplot(224)
plt.title("m$_2$(t) original vs recuperado")
plt.plot(freqm,np.abs(M2),freqm,np.abs(M2_rec))
plt.legend(["Original","Demodulado"])
plt.xlim([-1500,1500])

plt.tight_layout()
plt.show()