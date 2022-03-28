from matplotlib import rc
import matplotlib.pylab as plt
import numpy as np

rc("text", usetex=True)

## Parametros
K = 20  # Número de amostras
l = list(range(1, K + 1))  # Eixo amostras

# Definindo forma de onda
s_0 = np.ones(K)  # Sinal 1: Um degrau
s_1 = np.hstack((np.ones(K // 2), -np.ones(K // 2)))  # Sinal 2: Soma de degraus

# Inicializando sinais de saida do correlator
r_0 = np.zeros(K)  # Inicializa vetor r_0
r_1 = np.zeros(K)  # Inicializa vetor r_1
vtVar = np.array([0, 0.1, 1])  # Variâncias a simular

# Figura para sinais no tempo
plt.figure(1, figsize=[10, 10])

plt.subplot(len(vtVar) + 1, 2, 1)
plt.plot(l, s_0, label="$s_0(t)$")
plt.legend()

plt.subplot(len(vtVar) + 1, 2, 2)
plt.plot(l, s_1, "r", label="$s_1(t)$")
plt.legend()

# Figura para saídas dos correlatores
plt.figure(2, figsize=[10, 10])
# Cálculo da saída do correlator para cada valor de variância do ruído
for ik, vt in enumerate(vtVar):
    vtNoise = np.sqrt(vt) * np.random.normal(0, 1, K)  # Vetor de ruído

    ## Sinais quando s_0 é transmitido
    rs_0 = s_0 + vtNoise  # Sinal recebido
    # Correlacionando sinais
    for n in range(K):
        r_0[n] = np.sum(rs_0[:n] * s_0[:n])
        r_1[n] = np.sum(rs_0[:n] * s_1[:n])

    ## Gráficos
    # Gráficos da autocorrelação
    plt.figure(2)
    plt.subplot(len(vtVar), 2, 2 * ik + 1)
    plt.plot(l, r_0, "-")
    plt.plot(l, r_1, "--")
    plt.legend([r"$r_{0}$", r"$r_{1}$"], loc="upper left")
    plt.xlabel(r"$\sigma^2$ = {} \& $s_0$ é transmitido".format(vt))

    # Gráficos do sinal+ruído no tempo
    plt.figure(1)
    plt.subplot(len(vtVar) + 1, 2, 2 * ik + 3)
    plt.plot(l, rs_0)
    plt.legend([r"$s_0(t)$ + n(t), $\sigma^2$ = {}".format(vt)])

    ## Sinais quando s_1 é transmitido
    rs_1 = s_1 + vtNoise  # Sinal recebido
    # Correlacionando sinais
    for n in range(K):
        r_0[n] = np.sum(rs_1[:n] * s_0[:n])
        r_1[n] = np.sum(rs_1[:n] * s_1[:n])

    ## Gráficos
    # Gráficos da autocorrelação
    plt.figure(2)
    plt.subplot(len(vtVar), 2, 2 * ik + 2)
    plt.plot(l, r_0, "-")
    plt.plot(l, r_1, "--")
    plt.legend([r"$r_{0}$", r"$r_{1}$"], loc="upper left")
    plt.xlabel(r"$\sigma^2$ = {} \& $s_1$ é transmitido".format(vt))

    # Gráficos do sinal+ruído no tempo
    plt.figure(1)
    plt.subplot(len(vtVar) + 1, 2, 2 * ik + 4)
    plt.plot(l, rs_1)
    plt.legend([r"$s_1(t)$ + n(t), $\sigma^2$ = {}".format(vt)])

plt.show()