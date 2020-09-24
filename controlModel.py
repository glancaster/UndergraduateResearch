import control as c
import numpy as np
import random as r
import matplotlib
import bokeh as bk 
import pandas as pd
import time 
import math as m

##setup##
g = -9.81
dt = (r.randint(50,100)/100)
dx = r.randint(1,500)/100
vx = dx/dt
vy = (.5-0.5*g*dt**2)/dt  

xt=5-(1+dx)
t = (xt)/vx 
theta = m.atan(0.5/dx)

act_time = .5 #time it takes system from start to finish 

proj_time = t
time_to_actuate = -act_time + proj_time


##set up prints##
print('ball speed',vx)
print('dx:',dx)
print('dt:',dt)
#print('xo:',xo)
print('xt:',xt)

print('controller time',proj_time)
print('actuation time',float(time_to_actuate))

##open loop##
actuated = False
def act():
    print('actuated')

while True:
    time.sleep(time_to_actuate)
    act()
    break

## visuals ##
import matplotlib.pyplot as plt

# Data for plotting
t = np.arange(dt, proj_time, 0.01)
y = 9.5 + vy*t + 0.5*g*t**2


fig, ax = plt.subplots()
ax.plot(t, y)

ax.set(xlabel='time (s)', ylabel='position-y (m)',
       title='projectile line')
ax.grid()

fig.savefig("test.png")
plt.show()





