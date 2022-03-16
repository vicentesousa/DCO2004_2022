import numpy as np
#Geração da Janela
fc = 8                                         #frequência do cosseno
fsampling = 64.0                               #frequência de amostragem
tf = 2                                         #segundos
t_amostragem = 1.0/fsampling                   #tempo de amostragem
Am = 1.0                                       #amplitude
t = np.arange(0,tf,t_amostragem)               #determinação do eixo de tempo
m1 = Am*np.cos(2*np.pi*fc*t)                   #sinal senoidal puro
m2 = np.zeros(len(t))                          #Sinal de zeros 
m2[len(t)//3:len(t)*2//3] = 1                  #Sinal de zeros com "1" entre 1/3 a 2/3 de seu comprimento (janela quadrada) 
m = m1*m2                                      #Sinal resultante


#Efeito da janela na frequência do sinal
lfft = 600                                     #número de pontos da fft
m1fft = np.abs(np.fft.fft(m1,lfft))            #cálculo da fft para a senoide
m2fft = np.abs(np.fft.fft(m2,lfft))            #cálculo da fft para a janela
mfft = np.abs(np.fft.fft(m1*m2,lfft))          #cálculo da fft para sinal com janela

freq1 = np.linspace(0.0,fsampling/2,lfft//2)   #definição do eixo unilateral das  frequências

m1fftuni = m1fft[:lfft//2]                     #fft unilateral 
m2fftuni = m2fft[:lfft//2]                     #fft unilateral janela
mfftuni  = mfft[:lfft//2]                      #fft unilateral senoide com janela

#Gráficos
import matplotlib.pyplot as plt
plt.figure(1,[8,10])

grafico_1 = plt.subplot(611)
plt.title("Senoide no tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("g(t)")
plt.grid()
plt.ylim([-1.2,1.2])
plt.stem(t,m1)

grafico_2 = plt.subplot(612)
plt.title("Janela no tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("g(t)")
plt.grid()
plt.ylim([-1.2,1.2])
plt.stem(t,m2)


grafico_3 = plt.subplot(613)
plt.title("Senoide com janela no tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("g(t)")
plt.grid()
plt.ylim([-1.2,1.2])
plt.stem(t,m)

#transformação dos sinais no tempo para frequência 
grafico_4 = plt.subplot(614)
plt.title("Senoide na frequência")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|G(f)|")
plt.grid()
plt.plot(freq1,m1fftuni)


grafico_5 = plt.subplot(615)
plt.title("Janela na frequência")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|G(f)|")
plt.grid()
plt.plot(freq1,m2fftuni)

grafico_6 = plt.subplot(616)
plt.title("Senoide com janela no tempo")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|G(f)|")
plt.grid()
plt.plot(freq1,mfftuni)

plt.tight_layout()                             #ajusta o espaçamento entre os plots
plt.show()