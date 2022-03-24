from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftshift,ifft

# Para diminuir o tamanho do código desse experimento, coletaremos todos os dados Passo 1 da Prática 1
# e trabalharemos com o sinal gerado lá. Todas as variáveis terão o mesmo nome.
# O arquivo .mat deve sempre está na pasta em que o script está. Se necessário, rode o Passo 1 da Prática 1!!!
variaveis = loadmat('/home/dco2004/DCO2004_2022/notebooks/Amostragem.mat')
T = float(variaveis['T'])
lfft = int(variaveis['lfft'])
N_samp = int(variaveis['N_samp'])
S_out = variaveis['S_out'].flatten()
s_out = variaveis['s_out'].flatten()
m_t = variaveis['m_t'].flatten()
t = variaveis['t'].flatten()
freq = variaveis['freq'].flatten()
Bs = fm1 = float(variaveis['fm1'])

# Reconstrução realizando a filtragem no domínio da frequência
BW=10                                                        # Largura de banda de 10
H_lpf=np.zeros(lfft)                                         # Zera vetor filtro
H_lpf[lfft//2-BW:lfft//2+BW-1]=1                             # Define 1 na frequência desejada
S_recv=N_samp*S_out*H_lpf                                    # Filtragem ideal
s_recv=np.real(ifft(fftshift(S_recv)))                       # Reconstroi o sinal no tempo
s_recv=s_recv*np.max(m_t)/np.max(s_recv)                     # Dá ganho pro sinal reconstruído

#  Reconstrução realizando a filtragem no domínio do tempo por meio 
#  de uma interpolação explícita (usando a função sinc)
# Gera laço para somatório
Tsinc = 0.002                                                # Passo de tempo da sinc
Tfsinc = 50                                                  # Tempo Final da sinc
tsinc = np.arange(0,Tfsinc,Tsinc)                            # Eixo de tempo da sinc
nSamples = len(s_out)                                        # Mede-se o comprimento do sinal
xSamples = np.arange(0,nSamples)                             # Vetor ordenado de amostras
s_recvSinc=0
for ik in xSamples:      
    Nx_sinc = s_out[ik]*np.sinc(2*np.pi*Bs*(tsinc-ik*T))     # Cria sinc para a amostra ik
    s_recvSinc = s_recvSinc+Nx_sinc                          # Faz somatórios das sincs
    
s_recvSinc=s_recvSinc[0:lfft]                                # Corrige comprimento do vetor
s_recvSinc=s_recvSinc*(np.max(m_t)/np.max(s_recvSinc))       # Ajusta o ganho
S_recvSinc = fftshift(fft(s_recv,lfft)/lfft)

# Gráficos Reconstrução realizando a filtragem no domínio da frequência
# Plota espectro do sinal regenerado pelos dois métodos
plt.figure(1,[10,7])
plt.subplot(321)
plt.title("Espectro do sinal amostrado")
plt.plot(freq,np.abs(S_out))
plt.xlim([-150,150])
plt.ylim([0,0.06])
#
plt.subplot(323);
plt.plot(freq,abs(S_recv))
plt.title("Regeneração no domínio da frequência")
plt.xlabel("Frequência [Hz]")
plt.xlim([-150,150])
plt.ylim([0,0.6])
#
plt.subplot(325)
plt.plot(freq,abs(S_recvSinc))
plt.title("Regeneração no domínio do tempo")
plt.xlabel("Frequência [Hz]")
plt.xlim([-150,150])
plt.ylim([0,0.6])
# Plota sinal regenerado pelos dois métodos
plt.subplot(322)
plt.plot(t,m_t)
plt.title("Sinal original")
#
plt.subplot(324);
plt.plot(t,s_recv[:lfft])
plt.title("Regeneração no domínio da frequência")
#
plt.subplot(326)
plt.plot(t,s_recvSinc[:lfft])
plt.title("Regeneração no domínio do tempo");
plt.xlabel("Frequência [Hz]");
plt.tight_layout()
plt.show()