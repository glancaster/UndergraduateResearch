import control as c
import numpy as np
import random
import matplotlib as plt

speedref = random.randint(5,10)
lag = c.tf([0.3,0.7],[9,10,2])
tf1 = c.tf([3,4],[5,6])
sys = speedref*tf1*lag
sysf = c.feedback(sys)
print(sysf)