# Parâmetros da onda
import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt

# Sinal em banda-base
fm = 10;                                                  # Frequência do sinal
Am = 1;                                                   # Amplitude do sinal 
fc = 6000;
Fs = 8*fc;                                                # Frequência de amostragem
t =  np.arange(0,1-1/Fs,1/Fs)                             # Eixo do tempo
m_t = Am*np.sin(2*np.pi*fm*t)+Am*np.sin(2*np.pi*0.4*fm*t) # Sinal em banda base

# Modulação FM
fc = 6000;                                                # Frequência da portadora
kf=160*np.pi;                                             # Sensibilidade de frequência 
m_intg=kf*np.cumsum(m_t)/Fs;                              # Integral com Kf
x = np.cos(2*np.pi*fc*t +m_intg )                         # Sinal modulado

# Hilbert
z= hilbert(x)                                             # Sinal analítico (real + imaginário)
inst_phase = np.unwrap(np.angle(z));                      # Fase instantânea com ajuste para variações bruscas de ângulo
p = np.polyfit(t,inst_phase,1);                           # Ajustar linearmente a fase instantânea
# Reavaliar o termo de compensação usando os valores ajustados
estimated = np.polyval(p,t);                               
demodulated = inst_phase - estimated;
demodulated_aux = np.concatenate(([demodulated[0]],demodulated))
demodulated=np.diff(demodulated_aux)/(1/Fs*kf);

# Gráficos
plt.title('Demodulação FM com a Transforda de Hilbert')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.plot(t,m_t,t,demodulated)
plt.ylim([-2,2])
plt.xlim([0,1])
plt.legend(['m(t) original','m(t) demodulado'])
plt.show()