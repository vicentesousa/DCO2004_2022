import numpy as np
import sounddevice as sd


# Duração de cada tom (em segundos).
time = 0.3

# Diconário de notas musicais (5ª oitava) - em frequência.
Do, Re, Mi, Fa, Sol, Silence = 528, 592, 665, 704, 790, 0

# Vetor de "música", usando o dicionário de notas pré-definido.
music = [Do, Re, Mi, Fa, Silence, Fa, Fa, Silence, Do, Re, Do, Re, Silence, Re,
           Re, Silence, Do, Sol, Fa, Mi, Silence, Mi, Mi, Silence, Do, Re, Mi, Fa,
           Silence, Fa, Fa]

for nota in music:
    if nota == Silence:
        sd.sleep(300)                                                                                 # Caso a nota seja Silence para de tocar por 300 milisegundos
    else:                                               
        fa = 100*nota                                                                                 # Escolhe a frequência de amostragem do tom corrente.
        t = np.arange(0, time, 1/fa)                                                                  # Gera o eixo do tempo para o tom corrente.
        y = np.cos(2*np.pi*nota*t)+0.8*np.cos(2*np.pi*0.01*nota*t)+0.8*np.cos(-2*np.pi*0.01*nota*t)   # Gera o tom corrente.
        sd.play(y, fa)                                                                                # Reproduzir o sinal gerado.
        sd.sleep(300)
        #sd.wait()                                                                                     # bloquear o interpretador Python até que a reprodução termine.
