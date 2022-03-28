import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
# Parâmetros da Gaussiana
lambd=1                                               # Média
nSamples = int(1e5)                                   # Número de amostras
# Amostras geradas pelo método de inversão
vtU = np.random.rand(nSamples)                        # Amostras com distribuição uniforme
vtX = -lambd*np.log(1-vtU);                           # Amostras exponenciais geradas pelo método de inversão
# PDF das amostras geradas
binWidth = 0.1
vtBins = np.arange(np.min(vtX),np.max(vtX),binWidth)     
plt.subplot(211)
y, x = np.histogram(vtX,vtBins)                        
plt.plot(x[1:len(x)],y/(binWidth*nSamples), label='PDF das amostras - método da inversão')
# PDF teórica
xe = np.linspace(expon.ppf(0.01),expon.ppf(0.99), 100)
plt.plot(xe, expon.pdf(xe),'r-', alpha=lambd, label='PDF Teórica')
plt.legend()
#plt.show()
# CDF
plt.subplot(212)
# CDF teórica
plt.plot(vtBins, expon.cdf(vtBins,scale=1/lambd), label='CDF Teórica')
# CDF estimada pelas amostras
#y, x = np.histogram(vtX,vtBins, cumulative=True)                        
cumhist = np.cumsum(y/(nSamples)*1)
plt.plot(x[1:len(x)],cumhist, label='CDF das amostras - método da inversão')
plt.legend()
plt.show()