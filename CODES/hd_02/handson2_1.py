#importando as bibliotecas necessárias:
import numpy as np             
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wv 
import os


# Parâmetros da onda:
tf = 1                         # Tempo de duração da nota
fc = 512                       # Frequência da nota Dó
fs = 100*fc                    # Frequencia de amostragem da nota. 
t =np.arange(0,tf+1/fs,1/fs)   # Vetor tempo. Para cada elemento do vetor t, haverá um elemento em y correspondente.
A = 1                          # Amplitude do sinal
y=A*np.cos(2*np.pi*fc*t)       # Sinal senoidal

plt.figure(1,figsize=[10,7])   # cria instância da figura para poder alterar seu tamanho
plt.plot(t,y, label='signal')  # Visualizar o sinal gerado  
plt.axis([0,0.02,-2,2])        # Zoom para melhor visualização
plt.grid(True)                 # Realiza a plotagem de uma grade para melhor vizualização e comparação
plt.show() 