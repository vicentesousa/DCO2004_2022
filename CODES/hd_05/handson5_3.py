from scipy.io import loadmat
import numpy as np
from scipy import fftpack 
import matplotlib.pyplot as plt
mat_data = loadmat('/home/dco2004/DCO2004_2022/MATERIAL/HD_05/signal.mat')      # Retorna um dicionário
t = mat_data['t'].flatten()
ts =  mat_data['Ts']
msg = mat_data['msg'].flatten()
fs = 1/ts
Ac = 1                                                 # Amplitude da portadora
fc = 25                                                # Frequência da portadora
c = Ac*np.cos(2*np.pi*fc*t)                            # Sinal portadora
s = c*msg                                              # Sinal AM-DSB-SC
# Cálculo do espectro do sinal
lfft = len(s)*10
freq = np.arange(-fs/2,fs/2,fs/lfft)
M_fft = np.fft.fft(s,n=lfft,axis=0)/np.sqrt(lfft)
M_sig= fftpack.fftshift(M_fft)
# Gráfico do sinal no tempo
plt.figure(1,[10,7])
plt.subplot(211)
plt.title("AM-DSB-SC no tempo")
plt.ylabel("Amplitude")
plt.xlabel("tempo [s]")
plt.plot(t,s,'b',t,msg,'y')
# Gráfico do espectro do sinal
plt.subplot(212)
plt.title("AM-DSB-SC na frequência ")
plt.ylabel("Amplitude")
plt.xlabel("Frequência (Hz)")
plt.plot(freq,np.abs(M_sig))
plt.xlim([-50,50])
plt.tight_layout()
plt.show()