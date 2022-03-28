# Geração de Variável aleatória
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
#
# Parâmetros da Gaussiana
mu = 10                                            # Média
sigma = 2                                          # Desvio padrâo
vtnSamples = [1e2, 1e3, 1e5]                       # Número de amostras
vtSamples = sigma * np.random.randn(int(np.max(vtnSamples))) + mu  
for ik in range(0,len(vtnSamples)):
    nSamples = int(vtnSamples[ik])
    plt.figure(1,[15,5])
    plt.subplot(len(vtnSamples),1,ik+1)
    # PDF estimada
    binWidth = 0.1
    vtCurrentS = vtSamples[:nSamples]
    vtBins = np.arange(np.min(vtCurrentS),np.max(vtCurrentS),binWidth)     
    y, x = np.histogram(vtCurrentS,vtBins)                        
    plt.plot(x[1:len(x)],y/(binWidth*nSamples), label='PDF Estimada para N = {}'.format(nSamples))
    # PDF real
    plt.plot(x[1:len(x)], norm.pdf(x[1:len(x)],mu,sigma), label='PDF Real')
    plt.legend()
plt.show()