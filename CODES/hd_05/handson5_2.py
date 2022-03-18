import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack

tau = 1e-4                                                      # Constante de tempo do detector de envelope
Ts=1e-6                                                         # Definição do período
t = np.arange(1000)*Ts                                          # Definição do vetor tempo
fc = 10000                                                      # Frequência da portadora.
fm = 1500                                                       # Frequência do sinal
Mu = 0.6                                                        # Índice de modulaçao.
Ac = 1.0
x_AMo = Ac*(1.0+Mu*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t);  # Onda Modulada AM-DSB

x_envIdeal = np.abs(Ac*(1.0+Mu*np.cos(2*np.pi*fm*t)))           # Envoltória ideal

# Detector de envoltória
x_AM = x_AMo*(x_AMo>0)                                          # Efeito do diodo (semiciclo positivo)
x_env = np.zeros(len(x_AM))
Ns = len(x_AM)
out = -1
for i in range(Ns):
    inp = x_AM[i]
    if inp>=out:
        out = inp            # Caso 1: x_am(t) > Vc(t) (carga do capacitor)
    else:
        out *= (1-Ts/tau)    # Caso 2: x_am(t) < Vc(t) (descarga do capacitor)
    x_env[i] = out

# gráfico composto
plt.figure(1,[10,7])
plt.title("Detecção de envoltória")
plt.ylabel("Amplitude")
plt.xlabel("Tempo(ms)")
envoltoria_ideal = plt.plot(t*1000,x_envIdeal)
sinal_transmitido = plt.plot(t*1000,x_AM)
detector_de_saida = plt.plot(t*1000,x_env)
plt.grid()
plt.legend(["Envoltória ideal","Onda AM retificada","Envoltória recuperada"])
plt.show()

## Gráficos com a função plt.plot()
plt.figure(1,[10,7])
plt.subplot(311)
plt.plot(t*1000,x_envIdeal)                             
plt.title("Envoltória ideal")
plt.ylabel("Amplitude")

plt.figure(1,[10,7])
plt.subplot(312)
plt.plot(t*1000,x_AM)                             
plt.title("Onda AM retificada")
plt.ylabel("Amplitude")

plt.figure(1,[10,7])
plt.subplot(313)
plt.plot(t*1000,x_env)                             
plt.title("Envoltória recuperada")
plt.ylabel("Amplitude")
plt.xlabel("Tempo(ms)")

plt.subplots_adjust(hspace=0.3) # Ajustando espaço entre subplots

plt.show()