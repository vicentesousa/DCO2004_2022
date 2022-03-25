import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
# Distribuição
mu = 0                                       # Média
sigma = 1.0                                  # Desvio padrâo
T=0.001                                      # Taxa de amostragem
x=np.arange(-2,2+T,T)                        # Eixo x       
DistNorm=stats.norm.pdf(x,mu,sigma)          # Distribuição normal    
# Cálculo da probabilidade
limite_esquerdo = np.max(np.where(x<-sigma))
limite_direito = np.min(np.where(x>sigma))
indices = np.arange(limite_esquerdo+1,limite_direito)
prob1=np.sum(DistNorm[indices])*T*100        # Probabilidade de um evento ocorrer no intervalo
plt.figure(1,[8,6])
plt.plot(x,DistNorm,'k')                                       
plt.title('Probabilidade de = ' + str(prob1))      # Mostra valor verdadeiro de prob1
plt.fill_between(x[indices],DistNorm[indices],facecolor='midnightblue')
plt.show()
# calculando diretamente da integral
from sympy import *
init_printing(use_unicode=False, wrap_line=False, no_global=True)
x, f = symbols('x f')
f = 1/(sqrt(2*pi*sigma**2))*exp(-(x-mu)**2/(2*sigma**2))
prob2 = integrate(f, (x,-sigma,sigma))
print("Probabilidade pela integral da fórmula da PDF = "+str(prob1)+" %")
print('Probabilidade pela área da PDF {:02.4f}  %'.format(prob2*100))