import numpy as np

# Como visto anteriormente, para economizar linhas de código, uma boa prática é resumir a conversão 
# binário/decimal em duas funções:
def de2bi(sinal):
    from numpy import fromiter,binary_repr,round 
    sinal_bin = round(sinal).astype(int)
    return fromiter(map(binary_repr,sinal_bin),dtype=int)
#
def bi2de(sinal):
    from numpy import ndarray
    sinal_dec = ndarray(len(sinal),dtype=int)
    for i in range(len(sinal_dec)):
        sinal_dec[i] = int(str(sinal[i]),2)  
    return sinal_dec
#
## Parâmetros dos sinais
t = np.arange(0,10,0.01)
f1=0.5
f2=0.2
A = 10
sinal01=A*np.cos(2*np.pi*f1*t)
sinal02=A*np.cos(2*np.pi*f2*t)
#
# Quantização e codificação
# Sinal 1
sig_quan01= sinal01-np.min(sinal01)+1      # Todos elementos positivos
sig_quan01= np.round(sig_quan01)           # Transforma sinal em números inteiros
sig_code01= de2bi(sig_quan01)              # Transforma em sinal binário 
# Sinal 2
sig_quan02= sinal02-np.min(sinal02)+1      # Todos elementos positivos
sig_quan02= np.round(sig_quan02)           # Transforma sinal em números inteiros
sig_code02= de2bi(sig_quan02)              # Transforma em sinal binário 
# Multiplexação
frameSize = 4;                            # Tamanho do quadro (número máximo de sinais a serem multiplexados)      
mux_sig = np.zeros(len(sig_code01)*frameSize,dtype=int)
# mux_sig é um simples array de 4000 elementos, cada um sendo um binário completo
for i in range(1,len(sig_code01)+1): 
    mux_sig[4*(i-1)]      =   sig_code01[i-1]  # Indexação em python começa em 0
    mux_sig[4*(i-1)+1]    =   0
    mux_sig[4*(i-1)+2]    =   sig_code02[i-1]
    mux_sig[4*(i-1)+3]    =   0
#
#Demultiplexador de sinais    
demux_01 = np.zeros(1000,dtype=int)
demux_02 = np.zeros(1000,dtype=int)
for i in range(1,1001):
    demux_01[i-1]= mux_sig[(i-1)*4 ]
    demux_02[i-1]= mux_sig[(i-1)*4 + 2]
# Decodifcação    
sig_rec01 = bi2de(demux_01)
sig_rec02 = bi2de(demux_02)
# Teste se decoficação funcionou
if (np.array_equal(sig_rec01,sig_quan01)):
   print("Sinais sig_rec01 e sig_quan01 são iguais: decodficação realizada com sucesso!!!")
else:
   print("Sinais sig_rec01 e sig_quan01 são diferentes: decodficação falhou!!!")
if (np.array_equal(sig_rec02,sig_quan02)):
   print("Sinais sig_rec02 e sig_quan02 são iguais: decodficação realizada com sucesso!!!")
else:
   print("Sinais sig_rec02 e sig_quan02 são diferentes: decodficação falhou!!!")