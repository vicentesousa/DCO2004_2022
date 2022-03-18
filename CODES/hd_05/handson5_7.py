import numpy as np
import scipy.fftpack as ff
from scipy import signal
import matplotlib.pyplot as plt

ts = 1e-4                                        # Tempo de amostragem
t = np.arange(-0.04,0.04,ts)                     # Vetor do tempo
fc = 300;                                        # Frequência da portadora
# Sinal modulante (duas funções triângulo)
# m = 1-|t| , if |t|<1
# m = 0 , if |t|>1
Ta = 0.01                                                
mp1 = (1-np.absolute((t+0.01)/Ta))*((t+0.01)/Ta>=-1)*((t+0.01)/Ta<1) 
mp2 = (1-np.absolute((t-0.01)/Ta))*((t-0.01)/Ta>=-1)*((t-0.01)/Ta<1) 
msg = mp1-mp2;                                   # Sinal modulante

# Espectro do sinal modulante
lfft = len(t)                                    # Comprimento do vetor t
lfft = int(2**np.ceil(np.log2(lfft)))            # Transforma o comprimento em potência de 2
Mf = ff.fftshift(ff.fft(msg,lfft,axis=0)/np.sqrt(lfft))       
freqm = np.arange(-lfft/2,lfft/2,1)/(lfft*ts)    # Eixo da frequência

# Definição do Filtro
B_m = 100                                        # Largura de banda B_m Hz
h = signal.firwin(80,B_m*ts,window='hamming')    # Filtro passa-baixa

# Modulação FM
kf = 160*np.pi
m_int = kf*ts*np.cumsum(msg)                     # kf*Integral de m(t)
sfm = np.cos(2*np.pi*fc*t+m_int)                 # Sinal modulado em FM

# Espectro do sinal modulado
Sf = ff.fftshift(ff.fft(sfm,lfft,axis=0)/np.sqrt(lfft))       
  
# Demodulação FM
s_fmdiff = np.concatenate(([sfm[0]],sfm),axis=0)
s_fmdem = np.diff(s_fmdiff)/(ts*kf)              # Diferenciador repetindo o primeiro elemento 
s_fmrec = np.select([s_fmdem>0],[s_fmdem])       # Parte 1 da detecção de envoltória: retificação 
s_dem = signal.lfilter(h,1,s_fmrec)              # Parte 2 da detecção de envoltória: filtragem

# Espectro do sinal modulado
Mf_rec = ff.fftshift(ff.fft(s_dem,lfft,axis=0)/np.sqrt(lfft))       

# Gráficos no tempo
plt.figure(1,[10,7])
# Sinal demodulado
plt.subplot2grid((2, 2), (0, 0), colspan=2)
plt.plot(t,sfm)
plt.title('Sinal modulado FM')
plt.xlabel('Tempo [s]') 
plt.ylabel('s(t)')
# Sinal modulante 
plt.subplot2grid((2, 2), (1, 0))
plt.plot(t,msg)
plt.title('Sinal modulante')
plt.xlabel('Tempo [s]') 
plt.ylabel('m(t)')
# Sinal demodulado
plt.subplot2grid((2, 2), (1, 1))
plt.plot(t,s_dem,'r')
plt.title('Sinal demodulado')
plt.xlabel('Tempo [s]') 
plt.ylabel('m(t) recuperado')

plt.tight_layout()
plt.show()

# Espectro dos sinais
plt.figure(1,[10,7])
# Sinal demodulado
plt.subplot2grid((2, 2), (0, 0), colspan=2)
plt.plot(freqm,np.abs(Sf))
plt.xlim([-500,500])
plt.title('Sinal modulado FM')
plt.xlabel('Frequência [Hz]') 
plt.ylabel('S(f)')
# Sinal modulante 
plt.subplot2grid((2, 2), (1, 0))
plt.plot(freqm,np.abs(Mf))
plt.title('Sinal modulante')
plt.xlabel('Frequência [Hz]') 
plt.ylabel('M(f)')
plt.xlim([-500,500])
# Sinal demodulado
plt.subplot2grid((2, 2), (1, 1))
plt.plot(freqm,np.abs(Mf_rec))
plt.title('Sinal demodulado')
plt.xlabel('Frequência [Hz]') 
plt.ylabel('M(f) recuperado')
plt.xlim([-500,500])

plt.tight_layout()
plt.show()