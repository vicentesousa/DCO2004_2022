import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
#
# Parâmetros da distribuição
vtMu = [0, -10, 10]                  # Valores de média da Gaussiana
vtVar = [1, 5, 10]                   # Valores de variância da Gaussiana
x = np.arange(-20,20,0.1)     
#
# Variando a média e plotando os gráficos
plt.figure(1,[15,5])
sigma = np.sqrt(vtVar[0]);
for il in range(0,len(vtMu)):
    mu = vtMu[il]
    plt.subplot(2,2,1)
    plt.plot(x, norm.pdf(x,mu), label='Média = {}'.format(mu))
    plt.subplot(2,2,2)
    plt.plot(x, norm.cdf(x,mu), label='Média = {}'.format(mu))
# Variando a variância e plotando os gráficos
mu = vtMu[0];
for il in range(0,len(vtVar)):
    sigma = np.sqrt(vtVar[il]);
    plt.subplot(2,2,3)
    plt.plot(x, norm.pdf(x,mu,sigma), label='$\sigma$ = {:01.2f}'.format(sigma))
    plt.subplot(2,2,4)
    plt.plot(x, norm.cdf(x,mu,sigma), label='$\sigma$ = {:01.2f}'.format(sigma))
        
plt.subplot(2,2,1)
plt.legend()
plt.subplot(2,2,2)
plt.legend()
plt.subplot(2,2,3)
plt.legend()
plt.subplot(2,2,4)
plt.legend()
plt.show()