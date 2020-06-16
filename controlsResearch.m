%% Undergraduate Research - Graham Lancaster, Mr. Myers
% Bistable Particle Deflector 
clc 
clear all
%% Sensor 
speed = 3



%% Deflector
n = [2,3]
d = [5,6,7]
sys=tf(n,d)
step(sys)

