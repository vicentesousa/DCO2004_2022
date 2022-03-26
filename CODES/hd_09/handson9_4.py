from matplotlib import rc
import matplotlib.pylab as plt
import numpy as np
from scipy import stats

rc('text', usetex=True)

## Parâmetros
vtEbN0_dB = np.arange(-10, 10, 0.5)           # Vetor de Eb/N0 a simular
vtEbN0 = 10**(vtEbN0_dB/10)
vtPe = 1-stats.norm.cdf(np.sqrt(vtEbN0))
plt.semilogy(vtEbN0_dB, vtPe)
plt.title('Probabilidade de Erro - BPSK')
plt.xlabel("$E_b$/$N_0$")
plt.ylabel("$P_e$")
plt.grid()
plt.show()