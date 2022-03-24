# Parâmetros
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
#
# Criação das funções, por questão de organização
def downsample(array,rate):
    return array[::rate]

def upsample(array,rate):
    from numpy import zeros
    ret =  zeros(rate*len(array))
    ret[::rate] = array 
    return ret
#
# Geração do sinal
T=0.002                                             # Taxa de amostragem (500kHz)
Tf=1                                                # Tempo final em segundos
t= np.arange(0,Tf,T)                                # Definição do eixo do tempo      
fm1=3                                               # Frequência senoide 1      
fm2=1                                               # Frequência senoide 2
m_t=np.sin(2*np.pi*fm2*t)-np.sin(2*np.pi*fm1*t)     # Sinal mensagem m(t)
ts=0.02                                             # Nova taxa de amostragem
N_samp=round(ts/T)                                  # Número de elementos 
#
# Amostragem 
s_out=downsample(m_t,N_samp)                        # Coleta 1 amostra a cada N_samp=10 amostras do sinal  
s_out=upsample(s_out,N_samp)                        # Retorna vetor amostrado com o número inicial de elementos
#
# Quantização
sig_max=max(s_out)                                  # Encontra pico máximo
sig_min=min(s_out) 
n = 8;                                              # Número de bits por nível
L= 2**n;                                            # Níveis de quantização
Delta=(sig_max-sig_min)/L                           # Intervalo de quantização (distância entre um nível e outro)
q_level=np.arange(sig_min+Delta/2,sig_max,Delta)    # Vetor com as amplitudes dos Q níveis 
sigp=s_out-sig_min                                  # Deixa o sinal somente com amplitudes positivas (shift para cima)
sigp=sigp*(1/Delta)                                
sigp=sigp + 1/2 +0.001                              # Tira elementos do zero 
qindex=np.round(sigp)                               # Encontra inteiro mais proximo para cada elemento
qindex[qindex>L] = L                                # Trunca o excedente de qindex 
qindex = qindex.astype(int)                         # Casting para inteiro (garantindo que é do tipo inteiro)
q_out=q_level[abs(qindex-1)]                        # Distribui nos níveis cada elemento   
#   
# Codificação
# A função map recebe dois parâmetros: uma função e um iterável, e aplica essa função a cada elemento do iterável
vet_bin  = map(np.binary_repr,qindex-1)             # Transforma para binário
# O retorno da função map é um 'map object', que é um iterável. Queremos trabalhar com um array da numpy e, para isso,
# precisamos fazer uma conversão, via função np.fromiter() "from iterable":
vet_bin = np.fromiter(vet_bin,dtype=np.int)
#
# Decodificação
# É simplesmente converter os elementos de vet_bin de inteiros: para evitar sintaxes e conversões complicadas, 
# vamos usar um laço para recuperar o vetor:
vet_dec_rec = np.ndarray(len(vet_bin),dtype = np.int)# Vetor vazio com o mesmo tamanho de vet_bin, tipo inteiro
for i in range(len(vet_dec_rec)):
    vet_dec_rec[i] = int(str(vet_bin[i]),2) 
# Lembrando que, para converter de binário para decimal com o "casting" int(numero,base), a variável 'numero'
# precisa ser uma string ('str')
revert=q_level[abs(vet_dec_rec)]
#
# Gráficos
plt.figure(1,[9,9])
plt.subplot(211)
plt.plot(t,m_t,t,q_out)
plt.title("Sinal Original vs Sinal Amostrado e Quantizado")
#plt.legend(["Sinal recuperado","Sinal quantizado"])
#
plt.subplot(212)
plt.plot(t,m_t,t,revert)
plt.title("Sinal Original vs Sinal Amostrado, Quantizado, Codificado e Decodificado")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

plt.show()