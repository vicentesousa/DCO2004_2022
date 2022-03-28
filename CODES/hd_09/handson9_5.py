from matplotlib import rc
import matplotlib.pylab as plt
import numpy as np
from scipy import stats

rc("text", usetex=True)


def simOrtogonal(EbN0_dB, samples):
    EbN0_dB = np.array(EbN0_dB)
    # Parâmetros
    dE = 1  # Energia do sinal s0 e s1
    dEbN0 = 10 ** (EbN0_dB / 10)  # Eb/No em escala linear
    dsgma = dE / np.sqrt(2 * dEbN0)  # Desvio padrão do ruído
    #
    ## Transmissão
    vtr0s = stats.norm.rvs(size=EbN0_dB.size * samples).reshape((EbN0_dB.size, samples))
    vtr1s = stats.norm.rvs(size=EbN0_dB.size * samples).reshape((EbN0_dB.size, samples))
    # Geração dos números binários 0 e 1 com igual probabilidade
    vtBin = stats.randint.rvs(0, 2, size=samples * EbN0_dB.size).reshape(
        (EbN0_dB.size, samples)
    )
    # Conta as ocorrências dos bits
    ## Recepção e detecção de erro
    for vtr0, vtr1, sigma, bits in zip(vtr0s, vtr1s, dsgma, vtBin):
        vtr0 *= sigma
        vtr1 *= sigma
        # Gera saída do correlator para cada transmissão de s0
        vtr0[bits == 0] += dE
        # Gera saída do correlator para cada transmissão de s1
        vtr1[bits == 1] += dE
    # Detecção: 0 se, r0>r1 e 1, se r0<r1
    vtBinDetec = vtr0s < vtr1s
    #
    # Detecção de erros (soma dos vetores originais e detectados)
    # 0 + 0 = 0 (acerto)
    # 1 + 1 = 2 (acerto)
    # 0 + 1 = 1 (erro)
    # 1 + 0 = 1 (erro)
    # Cálculo da BER
    return np.array(
        [
            np.where(bits + bits_detec == 1)[0].size / samples
            for bits, bits_detec in zip(vtBin, vtBinDetec)
        ]
    )


# Script do Python para simulação (e comparação com fórmula teórica) de
# transmissão sinais ortogonais
## Parâmetros
vtEbNoSim = np.arange(16)  # Valores de Eb/No a serem simulados (dB)
vtEbNoTeo = np.arange(-1, 15.1, 0.1)  # Valores de Eb/No para a curva teórica (dB)
vtnMCSamples = (  # Número de amostras de Monte Carlo a serem simuladas
    10,
    100,
    5000,
    10000000,
)
vtMarkers = (  # Marcadores dos gráricos (para diferenciar a legenda)
    "s",
    "o",
    "d",
    "*",
    "<",
)
plt.figure(figsize=[10, 10])
for samples, markerSim in zip(vtnMCSamples, vtMarkers):
    # Gera a curva BER vs Eb/No por meio do simulador simOrtogonal
    vtSimError = simOrtogonal(vtEbNoSim, samples)
    plt.semilogy(
        vtEbNoSim,
        vtSimError,
        markerSim,
        markersize=12,  
        label="BER simulada com {} amostras".format(samples)
    )
# Gera a curva Pe teórica vs Eb/No por meio do formulação
vtSNR = 10 ** (vtEbNoTeo / 10)
vtTeoError = 1 - stats.norm.cdf(np.sqrt(vtSNR))
plt.semilogy(vtEbNoTeo, vtTeoError, label="Teórico - $P_e$")
plt.legend(loc="lower left", fontsize=14)
plt.xlabel("SNR", fontsize=14)
plt.ylabel("BER ou $P_e$",  fontsize=14)
plt.show()