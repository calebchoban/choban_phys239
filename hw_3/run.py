import numpy as np
import matplotlib.pyplot as plt
from electron_ion_interaction import *



a0 = 5.3E-11 # Bohr radius (m)

# Initial conditions in SI units
y0 = 1000*a0; x0 = -10*y0
vx0 = 1E6; vy0 = 0;
T = 20*y0/vx0;
N = 10000;

pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)


f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=[38,12])
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.tick_params(axis='both', which='major', labelsize=16)
ax1.tick_params(axis='both', which='minor', labelsize=12)
ax1.xaxis.offsetText.set_fontsize(16)
ax1.yaxis.offsetText.set_fontsize(16)
ax1.plot(pos_x/a0, pos_y/a0, label=r'$e^{-}$ Trajectory')
ax1.set_xlabel(r'X Position ($a_{o}$)',fontsize=24)
ax1.set_ylabel(r'Y Position ($a_{o}$)',fontsize=24)
ax1.scatter([0],[0],marker='*',color='y',label="Ion",s=500)
ax1.axis('equal')
ax1.legend(fontsize=18)
ax2.plot(time, vel_x, label=r'$v_{x}$')
ax2.plot(time, vel_y, label=r'$v_{y}$')
ax2.legend(fontsize=24)
ax2.set_xlabel(r'Time ($s$)',fontsize=24)
ax2.set_ylabel(r'Velocity ($m/s$)',fontsize=24)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.tick_params(axis='both', which='major', labelsize=16)
ax2.tick_params(axis='both', which='minor', labelsize=12)
ax2.xaxis.offsetText.set_fontsize(16)
ax2.yaxis.offsetText.set_fontsize(16)
ax3.plot(time, acc_x, label=r'$a_{x}$')
ax3.plot(time, acc_y, label=r'$a_{y}$')
ax3.legend(fontsize=24)
ax3.set_xlabel(r'Time ($s$)',fontsize=24)
ax3.set_ylabel(r'Acceleration ($m^{2}/s$)',fontsize=24)
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax3.tick_params(axis='both', which='major', labelsize=16)
ax3.tick_params(axis='both', which='minor', labelsize=12)
ax3.xaxis.offsetText.set_fontsize(16)
ax3.yaxis.offsetText.set_fontsize(16)
plt.savefig("single_interaction.png")
