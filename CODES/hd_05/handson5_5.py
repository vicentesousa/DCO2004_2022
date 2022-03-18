import numpy as np
from scipy import fftpack 
import matplotlib.pyplot as plt
from scipy import signal

Ts=1e-4                                                    # Período de amostragem
fs=1/Ts                                                    # Frequencia de amostragem
t = np.arange(5e3)*Ts                                      # Definição do vetor tempo
fc = 500                                                   # Frequencia da portadora.
fm = 150                                                   # Frequencia do sinal
Am=1.0                                                     # Amplitude do sinal senoidal
Ac=1.0                                                     # Amplitude da portadora
carrier = Ac*np.cos(2*np.pi*fc*t)                          # Sinal portadora
m_t = Am*np.cos(2*np.pi*fm*t)*np.exp(-t*20)                # Sinal mensagem
lmt = len(m_t)                                             # Comprimento do vetor mensagem
# Sinal na frequência
M_t = 2.0*np.abs(fftpack.fftshift(fftpack.fft(m_t,lmt)))/lmt
freq_m = np.arange(-fs/2,fs/2,fs/lmt)                      # Eixo da frequência para M(f)

## Modulação SSB
# Modulação DSB-SC
x_AM = m_t*carrier                                         # Onda Modulada DSB-SC 
lfft = len(x_AM)                                           # Comprimento do sinal DSB-SC
lfft = int(2**np.ceil(np.log2(lfft)))                      # Comprimento do sinal DSB-SC potência de dois
# Onda Modulada AM-DSB-SC na Frequência
X_AM = 2.0*np.abs(fftpack.fftshift(fftpack.fft(x_AM,lfft)))/lfft 
freq = np.arange(-fs/2,fs/2,fs/lfft)                       # Eixo da frequência 
L_lsb = int(np.floor(fc*Ts*lfft))                          # Local na frequência que se encontra a LSB.
# Filtragem da LSB
Filt_LSB = np.ones(lfft)                                   # Vetor filtro LSB (degrau) na frequencia 
Filt_LSB[lfft//2-L_lsb:lfft//2+L_lsb] = np.zeros(2*L_lsb)  # Definindo zeros na LSB
X_SSB_USB = X_AM*Filt_LSB                                  # Filtrando a frequência LSB
#Filtragem da USB
Filt_USB = np.zeros(lfft)                                  # Vetor filtro USB na frequencia  
Filt_USB[lfft//2-L_lsb:lfft//2+L_lsb] = np.ones(2*L_lsb)   # DOnde tinha 1 agora tem 0
X_SSB_LSB = X_AM*Filt_USB                                  # Filtrando a frequência USB

# USB tempo
# Inversa de fourrier
s_ssb_USB = np.real(fftpack.ifft(fftpack.fftshift(X_SSB_USB)))        
s_ssb_USB = s_ssb_USB[:lmt]                                # Ajustando o comprimento do vetor
# LSB tempo
# Inversa de fourrier
s_ssb_LSB =  np.real(fftpack.ifft(fftpack.fftshift(X_SSB_LSB)))     
s_ssb_LSB = s_ssb_LSB[:lmt]                                # Ajustando o comprimento do vetor

## Demodulação
# Demodulação SSB-USB
s_dem_USB= s_ssb_USB*carrier*2                             # Multiplicação com a portadora em fase
B_m=1000                                                   # Banda para filtragem 
h=signal.firwin(50,B_m*Ts)                                 # Filtro
s_rec_USB=signal.lfilter(h,1e-4,s_dem_USB)                 # Sinal filtrado
# Espectro do sinal USB 
lfft=len(s_rec_USB)                                        # Comprimento do sinal recuperado
lfft=int(2**np.ceil(np.log2(lfft)))                        # Transformando para uma potencia de 2
# Sinal recuperado na frequência
SSB_freq_USB = fftpack.fftshift(fftpack.fft(s_rec_USB,lfft)/lfft)          
s_rec_USB = (max(m_t)/max(s_rec_USB))*s_rec_USB            # Amplificando o sinal

# Demodulação SSB-LSB
s_dem_LSB= s_ssb_LSB*carrier*2;                            # Multiplicação com a portadora em fase
B_m=1000                                                   # Banda para filtragem 
h=signal.firwin(50,B_m*Ts)                                 # Filtro
s_rec_LSB =signal.lfilter(h,1e-4,s_dem_LSB)                # Sinal filtrado
# Espectro do sinal LSB 
lfft=len(s_rec_LSB)                                        # Comprimento do sinal recuperado
lfft=int(2**np.ceil(np.log2(lfft)))                        # Transformando para uma potência de 2
# Sinal recuperado na frequência
SSB_freq_LSB = fftpack.fftshift(fftpack.fft(s_rec_LSB,lfft)/lfft)          
s_rec_LSB = (max(m_t)/max(s_rec_LSB))*s_rec_LSB            # Amplificando o sinal

## Gráficos dos sinais no tempo
# Sinal modulado USB
plt.figure(1,[10,7])
plt.subplot(411)
plt.title("Sinal modulado USB")
plt.plot(t,s_ssb_USB)
plt.legend(["Sinal USB"])
plt.ylim([-1e-4,1e-4])
plt.xlim([0,0.5])
# Sinal gerado vs sinal demodulado
plt.subplot(412)
plt.title("Sinal modulante vs sinal demodulado - Tempo")
plt.plot(t,m_t,t,s_rec_USB)
plt.legend(["m(t) Gerado','m(t) Demodulado"])

## Gráfico do espectro do Sinal 
# Espectros USB e LSB
plt.subplot(413)
plt.title("Espectro do sinal modulado USB e LSB")
plt.plot(freq,(X_SSB_USB),freq,(X_SSB_LSB)) 
plt.xlim([-1e3,1e3])
plt.ylim([0.0,0.05])
plt.legend(["Sinal USB","Sinal LSB"])
# Espectros LSB e m(t)
plt.subplot(414)
plt.title("Espectro do sinal modulante vs sinal demodulado")
plt.plot(freq_m,M_t,freq,2.0*np.abs(SSB_freq_USB)) 
plt.legend(["m(t)","LSB"])
plt.xlim([-1e3,1e3])
plt.ylim([0.0,0.1])
plt.tight_layout()
plt.show() 