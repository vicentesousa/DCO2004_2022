#extraindo os arrays das janelas
# a classe Window possui um atributo chamado 'data' : array com os valores de amplitude
#usaremos esse atributo para trabalhar com os valores da janela
from spectrum.window import Window
from matplotlib import pyplot as plt 
import numpy as np
N_pontos = 1024 
b = Window(N_pontos, name= 'blackman')             #janela do tipo blackman
f = Window(N_pontos, name= 'flattop')              #janela do tipo flattop
h = Window(N_pontos, name= 'hamming')              #janela do tipo hamming

x = np.linspace(0,N_pontos-1,N_pontos)             #eixo horizontal
plt.figure(1,[8,6])                                #cria figura vazia, de tamanho 10x7
plt.plot(x,b.data,'r',x,f.data,'y',x,h.data,'b')   #plota as linhas das janelas
plt.legend(['Blackman','Flattop','Hamming'])       #escolhe as legendas
plt.title("Janelas")
plt.show()