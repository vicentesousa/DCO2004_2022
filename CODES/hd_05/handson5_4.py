from scipy.io import loadmat
import numpy as np
from scipy import fftpack 
import matplotlib.pyplot as plt
from scipy.signal import freqz
from scipy import signal

mat_data = loadmat('/home/dco2004/DCO2004_2022/MATERIAL/HD_05/signal.mat')      # Retorna um dicionário
t = mat_data['t'].flatten()
ts =  float(mat_data['Ts'])
msg = mat_data['msg'].flatten()
fs = 1/ts
Ac = 1                                                 # Amplitude da portadora
fc = 25                                                # Frequência da portadora
c = Ac*np.cos(2*np.pi*fc*t)                            # Sinal portadora
s = c*msg                                              # Sinal AM-DSB-SC

# Demodulação AM-DSB-SC
mr = 2*s*c;

# Filtragem do sinal
nyq_rate = fs / 2.0
cutoff_hz = 10                                         # Banda do sinal
h=signal.firwin(50,cutoff_hz/nyq_rate)                 # Coeficientes do filtro
mr_filtrado=signal.lfilter(h,1,mr)                     # Sinal filtrado

# Espectro do sinal antes da filtragem
lfft = len(mr)*10                                      # Comprimento da fft (Arbitrário)
freq = np.arange(-fs/2,fs/2,fs/lfft)
M_fft = np.fft.fft(mr,n=lfft,axis=0)/np.sqrt(lfft)
M_sig= fftpack.fftshift(M_fft)
# Gráfico do sinal no tempo
plt.figure(1,[10,7])
plt.subplot(311)
plt.title("Sinal s(t)*c(t) no receptor antes da filtragem")
plt.ylabel("Magnitude")
plt.xlabel("Frequência [Hz]")
plt.plot(freq ,abs(M_sig))
plt.xlim([-100,100])

# Resposta em frequência do filtro
plt.subplot(312)
[freq,amp] = freqz(h,fs)
plt.plot(freq*fs/(2*np.pi),10*np.log10(abs(amp)))
plt.title("Resposta em frequência do filtro")
plt.ylabel("Magnitude")
plt.xlabel("Frequência [Hz]")

# Espectro do sinal depois da filtragem
lfft = len(mr_filtrado)*10                                      # Comprimento da fft (Arbitrário)
freq = np.arange(-fs/2,fs/2,fs/lfft)
M_fft = np.fft.fft(mr_filtrado,n=lfft,axis=0)/np.sqrt(lfft)
M_sig= fftpack.fftshift(M_fft)
plt.subplot(313)
plt.title("Sinal s(t)*c(t) no receptor depois da filtragem")
plt.ylabel("Magnitude")
plt.xlabel("Frequência [Hz]")
plt.plot(freq ,abs(M_sig))
plt.xlim([-100,100])
plt.tight_layout()
plt.show()

# Gráfico do sinais modulante e demodulado
plt.figure(2,[10,7])
plt.title("AM-DSB-SC no tempo")
plt.ylabel("Amplitude")
plt.xlabel("tempo [s]")
plt.plot(t,msg,'b',t,mr_filtrado,'y')
plt.legend(['Sinal modulado s(t)','Sinal m(t) demodulado']);
plt.tight_layout()
plt.show()