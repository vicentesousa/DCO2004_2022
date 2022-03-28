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


def simAntipodal(EbN0_dB, samples):
    EbN0_dB = np.array(EbN0_dB)
    # Parâmetros
    dE = 1  # Energia do sinal s0 e s1
    dEbN0 = 10 ** (EbN0_dB / 10)  # Eb/No em escala linear
    dsgma = dE / np.sqrt(2 * dEbN0)  # Desvio padrão do ruído
    #
    ## Transmissão
    vtrs = stats.norm.rvs(size=EbN0_dB.size * samples).reshape((EbN0_dB.size, samples))
    # Geração dos números binários 0 e 1 com igual probabilidade
    vtBin = stats.randint.rvs(0, 2, size=samples * EbN0_dB.size).reshape(
        (EbN0_dB.size, samples)
    )
    # Conta as ocorrências dos bits
    ## Recepção e detecção de erro
    for vtr, sigma, bits in zip(vtrs, dsgma, vtBin):
        vtr *= sigma
        # Gera saída do correlator para cada transmissão de s0 e de s1
        vtr[bits == 0] += dE
        vtr[bits == 1] += -dE
    # Detecção: 0 se, r0>r1 e 1, se r0<r1
    vtBinDetec = vtrs < 0
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


# Script do Matlab para simulação (e comparação com fórmula teórica) de
# transmissão sinais ortogonais
## Parâmetros
vtEbN0Sim_db = np.arange(13)  # Valores de Eb/No a serem simulados (dB)
vtEbN0Teo_db = np.arange(0, 12.1, 0.1)  # Valores de Eb/No para a curva teórica (dB)
vtEbN0Teo = 10 ** (vtEbN0Teo_db / 10)
nMCSamples = int(1e6)

vtSimErrorAnti = simAntipodal(vtEbN0Sim_db, nMCSamples)
vtSimErrorOrto = simOrtogonal(vtEbN0Sim_db, nMCSamples)

## Calcula a Pe teórica
vtTeoErrorAnti = 1 - stats.norm.cdf(np.sqrt(2 * vtEbN0Teo))
vtTeoErrorOrto = 1 - stats.norm.cdf(np.sqrt(vtEbN0Teo))

plt.figure(figsize=[10, 10])
#
## Gráficos
plt.semilogy(vtEbN0Sim_db, vtSimErrorAnti, "or")
plt.semilogy(vtEbN0Teo_db, vtTeoErrorAnti, "r")
plt.semilogy(vtEbN0Sim_db, vtSimErrorOrto, "sk")
plt.semilogy(vtEbN0Teo_db, vtTeoErrorOrto, "k")
plt.legend(
    (
        "BER Antipodal",
        "$P_{e}$ Antipodal",
        "BER Ortogonal",
        "$P_{e}$ Ortogonal",
        "Location",
        "southwest",
    )
)
plt.xlabel("$E_b$/$N_0$")
plt.ylabel("BER (simulada) ou Pe (teórica)")
plt.title("Sinais Ortogonais vs Antipodais")
plt.show()