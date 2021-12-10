% Pacientes
clc; clear all; close all;
%% Dados
Tf=10;                                                      % Segundos
Fs=3000;                                                     % Frequência de amostragem
T=1/Fs;                                                     % Período de amostragem
t=0:T:Tf-T;                                                 % Eixo do tempo
for ik=1:5
    fm1=ik*10;                                              % Frequencia do sinal
    eval(['sinal_' num2str(ik) ' = ik*cos(2*pi*fm1*t);']);  % Sinal Paciente 
    eval(['plot(t,sinal_' num2str(ik) ');']);               % Plota sinal
    hold all;
end
axis([0 1/10 -ik ik]);
%% Save
save('Pacientes.mat','Fs','sinal_1','sinal_2','sinal_3','sinal_4','sinal_5');