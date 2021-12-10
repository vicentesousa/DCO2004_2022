clear all;close all;clc;
load('am_demo1.mat')      % Abre o sinal a ser modulado
fc = 25;
Ac = 1;
c = Ac*cos(2*pi*fc*t);
figure;
plot(t,carrier);
hold all;
plot(t,c);
legend('carrier','c')
title('carrier');
Ts = t(2)-t(1);
figure;
plot(t,msg);
save('signal.mat','msg','Ts','t');





