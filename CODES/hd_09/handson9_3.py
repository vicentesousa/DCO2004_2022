from matplotlib import rc
import matplotlib.pylab as plt
import numpy as np
from scipy import stats

rc('text', usetex=True)

## Parâmetros
Eb = 1                             # Energia dos pulsos (normalizada para 1)
Er0 = Eb                           # Média da saída do correlator 0
Er1 = 0                            # Média da saída do correlator 1
vtEbN0_dB = np.array([-10, 0, 10]) # Eb/N0s a simular em dB
vtEbN0 = 10**(vtEbN0_dB/10)        # Eb/N0s a simular em linear
vtVar = Eb*Eb/vtEbN0/2             # Variância na entrada do detector (= EN0/2)
plt.figure(figsize=[12, 10])
for ik, (vt, db) in enumerate(zip(vtVar, vtEbN0_dB)):
    dStd = np.sqrt(vt)
    x = np.arange(-7.5, 7.5, 0.001)*dStd+Eb  # Eixo
    ## Cálculo da distribuição Gausiana
    vtr_0 = stats.norm.pdf(x, loc=Er0, scale=dStd)   # Valores de r0 (distribuição de probalilidade r0|s0)
    vtr_1 = stats.norm.pdf(x, loc=Er1, scale=dStd)   # Valores de r1 (distribuição de probalilidade r1|s0)
    ## Gráficos
    #
    plt.subplot(len(vtEbN0_dB), 1, ik+1)
    plt.plot(x, vtr_0)
    plt.plot(x, vtr_1)
    plt.title(r"$E_b$/$N_0$ = {} dB".format(db))
    plt.legend((r"p($r_{1}\vert s_0$)",r"p($r_{0}\vert s_0$)"))
    plt.grid()
plt.show()