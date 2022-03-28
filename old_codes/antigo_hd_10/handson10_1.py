from matplotlib import pylab as plt
import numpy as np
from scipy import stats

def rcosfir(r, N_T, rate, T):
    if isinstance(N_T, int):
        N_T = np.hstack((N_T, N_T))

    N_T[0] = -abs(N_T[0])
    time_T = np.arange(0, 1/rate, max(N_T[1], abs(N_T[0])))
    b=firrcos(rate*(N_T[1]-N_T[0]),1/(2*T),r,rate/T,-N_T[0]*rate)*rate

    return b

def firrcos(N, fc, R, fs, delay):
    # Check if the filter order is a positive, even integer
    assert (N >= 0) and (N % 2 == 0)
    # Cast to enforce Precision Rules

    L = N+1 # Length of window

    # Check for valid cutoff frequency
    assert 0 < fc < fs/2

    # Check for valid rolloff values
    # check if input arguments are valid 
    # assert 0 >= R <= 1
    # check for range of input arguments
    assert (fc + R*fc) <= fs/2

    assert 0 <= delay <= L

    n = (np.arange(L)-delay) / fs

    return normal_design(n,fc,fs,R)

def normal_design(n,fc,fs,R):
    mask = np.isclose(abs(abs(4*R*fc*n) - 1.0), 0)
    b = np.zeros(n.shape)
    if mask.any():
        nind = n[mask]
        b[mask] = np.sinc(2*fc*nind)/fs \
                * np.cos(2*np.pi*R*fc*nind) \
                / (1.0 - (4*R*fc*nind)**2)

    b[np.invert(mask)] = R / (2*fs) * np.sin(np.pi/(2*R))

    return 2*fc*b

def eyediagram(x, n, period=None, offset=None):
    """Draw the eye diagram using all parts of the given signal x"""
    if period is None:
        period = n
    if offset is None:
        offset = n
        
    if len(x) % n > 0:
        x = x[ 0 : len(x) - (len(x) % n)]
        #x = np.hstack((x, np.zeros(n - (len(x) % n))))
    t = np.tile(np.arange(-period/2, period/2), (n, 1))
    y = np.reshape(x, (-1, n)).T
    plt.figure()
    plt.plot( t, y, 'b-')
    plt.ylim((-np.max(np.abs(x)),np.max(np.abs(x))))
    plt.tight_layout()

def upsample(signal, rate):
    ret = np.zeros(rate*len(signal))
    ret[::rate] = signal
    return ret

def raisedCosineDesign(alpha, span, L):
    t = np.arange(-span/2, span/2 + 1/L, 1/L) # +/- discrete-time base
    with np.errstate(divide='ignore', invalid='ignore'):
        A = np.divide(np.sin(np.pi*t),(np.pi*t)) #assume Tsym=1
        B = np.divide(np.cos(np.pi*alpha*t),1-(2*alpha*t)**2)
        p = A*B
    #Handle singularities
    p[np.argwhere(np.isnan(p))] = 1 # singularity at p(t=0)
    # singularity at t = +/- Tsym/2alpha
    p[np.argwhere(np.isinf(p))] = (alpha/2)*np.sin(np.divide(np.pi,(2*alpha)))
    return p

peSim = 64                                        # Período do símbolo (amostras/símbolo)
nsCL = 4                                          # Número de símbolos o cosseno levantado se espalhará (ISI)
roff = 0.25                                       # Fator de decaimento do cosseno levantado
nSimbs = 400                                      # Número de símbolos transmitidos 
vtSim = 2*stats.randint.rvs(0, 2, size=nSimbs)-1  # Símbolos
dup = upsample(vtSim, peSim)                      # Símbolos (sobreamostragem)
#hrc1 = rcosfir(roff, nsCL, peSim, 1)               # Cosseno levantado
hrc = raisedCosineDesign(roff, nsCL, peSim )               # Cosseno levantado
yrcosAll = np.convolve(dup, hrc)                  # Símbolos transmitidos com o cosseno levantado
yrcos = yrcosAll[nsCL*peSim-1:-nsCL*peSim]        # Trem de pulso cosseno levantado
# Configuração dos gráficos no tempo
nSim2Plot = 20                                    # Número de símbolos para o gráfico no tempo
# gráfico pulso cosseno levantado
plt.subplot(3, 1, 1)
plt.plot(hrc)
plt.title('Filtro cosseno levantado')
plt.subplot(3, 1, 2)
plt.plot(yrcosAll[:nSim2Plot*peSim])
plt.title('Sequência de símbolos com pulso cosseno levantado')
plt.axis([0, peSim*nSim2Plot, -1.5, 1.5])
plt.subplot(3, 1, 3)
t = np.arange(len(hrc))
for i, symbol in enumerate(vtSim):
    plt.plot(t + i*peSim, symbol*hrc)
plt.axis([0, peSim*nSim2Plot, -1, 1])
plt.title('Ilustração da ISI com pulso cosseno levantado')
# Diagrama de olho
#eyediagram(yrcos, 2*peSim, peSim )                  # Diagrama de olho do cosseno levantado
#plt.title('Diagrama de olho do pulso cosseno levantado')
#plt.show()
#
# Pulso retangular
hT = np.ones(peSim)   # Pulso retangular do transmissor (NRZ)
# Aplicando o pulso a sequência de símbolos 
ynrzAll = np.convolve(dup, hT)                            # Símbolos transmitidos com pulso retangular
ynrz = ynrzAll[:-peSim]                            # retira o último símbolo  
# gráfico pulso rentangular
plt.figure()
plt.subplot(2, 1, 1)
thT = np.arange(-peSim/2, peSim/2)
plt.stairs(
    np.hstack(([thT[0]-1], thT, [thT[-1]+1])),
    np.hstack(([0], hT, [0])))


plt.title('Filtro retangular')
plt.subplot(2, 1, 2)                                    # Número de símbolos para o gráfico no tempo
plt.plot(ynrzAll[:nSim2Plot*peSim])
plt.title('Sequência de símbolos com pulso retangular')
# Diagrama de olho
eyediagram(ynrz, 2*peSim, peSim)                   # Diagrama de olho do cosseno levantado
plt.title('Diagrama de olho do pulso rentagular')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
#
# Pulso meia senoide
hSin = sin(pi*np.arange(peSim)/peSim)   # Pulso meia senoide
# Aplicando o pulso a sequência de símbolos 
ysinAll = conv(dup, hSin)                          # Símbolos transmitidos com pulso meia senoide
ysin = ysinAll[:-peSim]                     # retira o último símbolo  
# gráfico pulso meia senoide
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(hSin)
plt.title('Filtro meia senoide')
plt.subplot(2, 1, 2)                                    # Número de símbolos para o gráfico no tempo
plt.plot(ysinAll[:nSim2Plot*peSim])
plt.title('Sequência de símbolos com pulso meia senoide')
# Diagrama de olho
eyediagram(ysin, 2*peSim, peSim)                   # Diagrama de olho do pulso meia senoide
plt.title('Diagrama de olho do pulso meia senoide')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()