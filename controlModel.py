import control as c
import numpy as np
import random
import matplotlib as plt

vel1 = random.randint(5,10) #m/s 
vel2 = vel1 + 0.1*9.81
height = 2 #m
time = height/velStart
mass = 3 #kg
accel = 9.81 
force = mass * accel
velEnd = velStart + time*accel
var =[vel1,vel2,time,force,velEnd]
print(var)

