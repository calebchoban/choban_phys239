import numpy as np
import matplotlib.pyplot as plt
from electron_ion_interaction import *



a0 = 5.3E-11 # Bohr radius (m)

# Initial conditions in SI units
x0 = 0; y0 = 100*a0;
vx0 = 1E5; vy0 = 0;
T = 0.2*y0/vx0;
N = 10000;

pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)


f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=[38,12])
ax1.plot(pos_x/a0, pos_y/a0)
ax1.set_xlabel(r'X Position ($a_{o}$)')
ax1.set_ylabel(r'Y Position ($a_{o}$)')
ax2.plot(time, vel_x, label=r'$v_{x}$')
ax2.plot(time, vel_y, label=r'$v_{y}$')
ax2.legend()
ax2.set_xlabel("Time (s)")
ax2.set_ylabel(r'Velocity ($m/s$)')
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax3.plot(time, acc_x, label=r'$a_{x}$')
ax3.plot(time, acc_y, label=r'$a_{y}$')
ax3.legend()
ax3.set_xlabel("Time (s)")
ax3.set_ylabel(r'Acceleration ($m^{2}/s$)')
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.savefig("tests.png")
