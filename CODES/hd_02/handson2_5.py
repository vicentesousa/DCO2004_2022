import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt
import sounddevice as sd

soundFile = '/home/dco2004/DCO2004_2022/MATERIAL/HD_02_PYTHON/sound_01.wav'               # Especifica do local e nome do arquivo de áudio
dFa,vtSom = wv.read(soundFile)                                   # Abre arquivo de áudio de um arquivo
# vtSom: amplitude das amostras de som
# dFa: frequência de amostrasgem do som (amostragem no tempo)
vtSom = 4.0*vtSom
vtSomint16 = vtSom.astype('int16')                               #converte de float64 para int16 para reduzir ruído
wv.write('/home/dco2004/DCO2004_2022/MATERIAL/HD_02_PYTHON/4xsound_01.wav',dFa,vtSomint16)#salva amomstra de som para ser reproduzida
#reproduz a amostra de som salva
#os.system('cvlc --play-and-exit ../MATERIAL/HD_02_PYTHON/4x_sound_01.wav')           
dta = 1/dFa                                                      # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                                     # Tempo da última amostra do sinal de áudio
vtTSom = np.arange(0,dTFinal+dta,dta)                            # Eixo temporal do arquivo de áudio
plt.figure(1,[10,7])
font = {'family' : 'DejaVu Sans','weight' : 'bold','size': 12}   #Configura a fonte do título
plt.rc('font', **font)
plt.plot(vtTSom,vtSom)                                           # Plota gráfico do áudio
plt.title('Sinal de Áudio')                                      # Configura título do gráfico
plt.ylabel('Amplitude')                                          # Configura eixo X do gráfico
plt.xlabel('Tempo (s)')                                          # Configura eixo Y do gráfico
plt.ylim([-120000,100000])                                       # Configura eixo Y do gráfico

sd.play(vtSom,dFa)                                               # Reproduz o audio

plt.show()