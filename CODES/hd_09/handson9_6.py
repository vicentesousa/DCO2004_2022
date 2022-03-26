from matplotlib import rc
import matplotlib.pylab as plt
import numpy as np
from scipy import stats

rc("text", usetex=True)


## Parâmetros
Eb = 1  # Energia dos pulsos (normalizada para 1)
Er0 = Eb  # Média da saída do correlator quando s0 é transmitido
Er1 = -Eb  # Média da saída do correlator quando s1 é transmitido
vtEbN0_dB = np.array([-10, 0, 10])  # Eb/N0s a simular em dB
vtEbN0 = 10 ** (vtEbN0_dB / 10)  # Eb/N0s a simular em linear
vtVar = Eb * Eb / vtEbN0 / 2  # Variância na entrada do detector (= EN0/2)
plt.figure(figsize=[10, 10])
for ik, (ebn0, var) in enumerate(zip(vtEbN0_dB, vtVar)):
    dStd = np.sqrt(var)
    x = np.arange(-15, 15, 0.001) * dStd + Eb  # Eixo
    ## Cálculo da distribuição Gausiana
    vtr_0 = stats.norm.pdf(
        x, loc=Er0, scale=dStd
    )  # Valores de r (distribuição de probalilidade r|s0)
    vtr_1 = stats.norm.pdf(
        x, loc=Er1, scale=dStd
    )  # Valores de r (distribuição de probalilidade r|s1)
    ## Gráficos
    #
    plt.subplot(len(vtEbN0_dB), 1, ik + 1)
    plt.plot(x, vtr_0)
    plt.plot(x, vtr_1)
    plt.title("$E_b$/$N_0$ = {} dB".format(ebn0))
    plt.legend([r"p(r$\vert s_0$)", r"p(r$\vert s_1$)"])
    plt.grid()
plt.show()