soundFile = '/home/dco2004/DCO2004_2022/MATERIAL/HD_02_PYTHON/sound_01.wav'               # Especifica do local e nome do arquivo de áudio

import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt
import sounddevice as sd


dFa,vtSom = wv.read(soundFile)                                   # Abre arquivo de áudio de um arquivo
# vtSom: amplitude das amostras de som
# dFa: frequência de amostrasgem do som (amostragem no tempo)

dta = 1/dFa                                                      # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                                     # Tempo da última amostra do sinal de áudio
vtTSom = np.arange(0,dTFinal+dta,dta)                            # Eixo temporal do arquivo de áudio
plt.figure(1,[10,7])
plt.plot(vtTSom,vtSom)                                           # Plota gráfico do áudio

font = {'family' : 'DejaVu Sans','weight' : 'bold','size': 12}   #Configura a fonte do título
plt.rc('font', **font)
plt.title('Sinal de Áudio')                                      # Configura título do gráfico
plt.ylabel('Amplitude')                                          # Configura eixo X do gráfico
plt.xlabel('Tempo (s)')                                          # Configura eixo Y do gráfico
plt.ylim([-32000,25000])


sd.play(vtSom,dFa)                                               # Reproduz o audio vtSom

# Reproduz arquivo de áudio
# os.system('cvlc --play-and-exit ./MATERIAL/HD_02_PYTHON/sound_01.wav')           
# Mostra informações gerais sobre o arquivo
print('Amostragem:')
print(' Taxa de amostragem = ',dFa,' Hz')
print(' Tempo entre amostras = ',dta,' Segundos')
print(' ')
print('Quantização e Codificação:')
print(' ')
print('Informações gerais do arquivo de áudio:')
print(' Número de amostras = ',len(vtSom),' amostras')
print(' Número de canais = ',vtSom.shape) 
print(' Duração = ',len(vtSom)*dta,' segundos')
plt.show()