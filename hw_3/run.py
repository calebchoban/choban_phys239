import numpy as np
import matplotlib.pyplot as plt
from electron_ion_interaction import *



a0 = 5.3E-11 # Bohr radius (m)

# Initial conditions in SI units
x0 = 0; y0 = 400*a0;
vx0 = 10E4; vy0 = 0;
T = 4;
N = 10;

pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)

print time, pos_x, vel_x
plt.plot(time, pos_x)
plt.savefig("test.png")