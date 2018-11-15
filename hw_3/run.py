import numpy as np
import matplotlib.pyplot as plt
from electron_ion_interaction import *



a0 = 5.3E-11 # Bohr radius (m)
"""
###############################################################################
# Single particle trajectory ################################################## 

# Initial conditions in SI units
# Should have x0 >> y0 and assume overall time is the time it would take
# v0 to cross a distance of 2*x0
# Need a long T since in order to have good resolution for discrete 
# Fourier transform
y0 = 1000*a0; x0 = -100*y0;
vx0 = 1E6; vy0 = 0;
T = np.abs(2*x0/vx0);
N = 100000;

pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)

# Calculate power spectrum and zoom in on non-zero regions
power_spec, freq = powerSpectrum(acc_x,acc_y,N,T)
pow_max = np.max(power_spec)
power_spec /= pow_max
mask = power_spec>0.01
power_spec = power_spec[mask]
freq = freq[mask]

# Here we only choose data near the ion to make the graphs nice
mask = np.sqrt(pos_x**2 + pos_y**2) < 10*y0;
masked_pos_x = pos_x[mask]
masked_pos_y = pos_y[mask]
masked_vel_x = vel_x[mask]
masked_vel_y = vel_y[mask]
masked_acc_x = acc_x[mask]
masked_acc_y = acc_y[mask]
masked_time = time[mask]

###############################################################################
# Plot all of the information for a single particle trajectory
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=[24,16])

# Plot particle trajectory ####################################################
ax1.set_title("Particle Trajectory",fontsize=24)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.tick_params(axis='both', which='major', labelsize=16)
ax1.tick_params(axis='both', which='minor', labelsize=12)
ax1.xaxis.offsetText.set_fontsize(16)
ax1.yaxis.offsetText.set_fontsize(16)
ax1.plot(masked_pos_x/a0, masked_pos_y/a0, label=r'$e^{-}$ Trajectory')
ax1.set_xlabel(r'X Position ($a_{o}$)',fontsize=24)
ax1.set_ylabel(r'Y Position ($a_{o}$)',fontsize=24)
ax1.scatter([0],[0],marker='*',color='y',label="Ion",s=500)
ax1.axis('equal')
ax1.legend(fontsize=18)

# Plot Velocity ###############################################################
ax2.set_title("Velocity",fontsize=24)
ax2.plot(masked_time, masked_vel_x, label=r'$v_{x}$')
ax2.plot(masked_time, masked_vel_y, label=r'$v_{y}$')
ax2.legend(fontsize=24)
ax2.set_xlabel(r'Time ($s$)',fontsize=24)
ax2.set_ylabel(r'Velocity ($m/s$)',fontsize=24)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.tick_params(axis='both', which='major', labelsize=16)
ax2.tick_params(axis='both', which='minor', labelsize=12)
ax2.xaxis.offsetText.set_fontsize(16)
ax2.yaxis.offsetText.set_fontsize(16)

# Plot Acceleration ###########################################################
ax3.set_title("Acceleration",fontsize=24)
ax3.plot(masked_time, masked_acc_x, label=r'$a_{x}$')
ax3.plot(masked_time, masked_acc_y, label=r'$a_{y}$')
ax3.legend(fontsize=24)
ax3.set_xlabel(r'Time ($s$)',fontsize=24)
ax3.set_ylabel(r'Acceleration ($m^{2}/s$)',fontsize=24)
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax3.tick_params(axis='both', which='major', labelsize=16)
ax3.tick_params(axis='both', which='minor', labelsize=12)
ax3.xaxis.offsetText.set_fontsize(16)
ax3.yaxis.offsetText.set_fontsize(16)

# Plot power spectrum #########################################################
ax4.set_title("Acceleration Power Spectrum",fontsize=24)
ax4.plot(freq, power_spec,'o')
ax4.set_xlabel(r'$\omega$ ($\frac{rad}{s}$)',fontsize=24)
ax4.set_ylabel("Amplitude",fontsize=24)
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax4.tick_params(axis='both', which='major', labelsize=16)
ax4.tick_params(axis='both', which='minor', labelsize=12)
ax4.xaxis.offsetText.set_fontsize(16)
ax4.yaxis.offsetText.set_fontsize(16)

plt.savefig("single_interaction.png")
plt.close()
"""

###############################################################################
# Run simulation for various impact parameters and initial velocities to see
# change in peak frequency in power spectrum

# First look at changes in impact parameters ##################################
range_y0 = 1000*a0*np.arange(1,10,1);
impact_param = np.zeros(len(range_y0))
impact_max_freq = np.zeros(len(range_y0))
N = 100000;

for i,y0 in enumerate(range_y0):
    # Initial conditions in SI units
    # Should have x0 >> y0 and assume overall time is the time it would take
    # v0 to cross a distance of 2*x0
    # Need a long T since in order to have good resolution for discrete 
    # Fourier transform
    x0 = -100*y0;
    vx0 = 1E6; vy0 = 0;
    T = np.abs(2*x0/vx0);
    
    
    pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)
    
    # Calculate impact parameter
    impact_param[i] = pos_y[np.argmin(np.abs(pos_x))]/a0
    
    # Calculate power spectrum and zoom in on non-zero regions
    power_spec, freq = powerSpectrum(acc_x,acc_y,N,T)
    impact_max_freq[i] = freq[np.argmax(power_spec)]

    
# Second look at changes in initial velocity ##################################
range_vx0 = 1E6*np.arange(1,10,1);
vel_max_freq = np.zeros(len(range_vx0))
N = 10000

for i,vx0 in enumerate(range_vx0):
    # Initial conditions in SI units
    # Should have x0 >> y0 and assume overall time is the time it would take
    # v0 to cross a distance of 2*x0
    # Need a long T since in order to have good resolution for discrete 
    # Fourier transform
    y0 = 1000*a0; x0 = -100*y0;
    vy0 = 0;
    T = np.abs(2*x0/vx0);
    
    pos_x, pos_y, vel_x,vel_y, acc_x, acc_y, time = EulerSolver([x0,y0],[vx0,vy0],N,T,electricForce)
    
    # Calculate power spectrum and zoom in on non-zero regions
    power_spec, freq = powerSpectrum(acc_x,acc_y,N,T)
    vel_max_freq[i] = freq[np.argmax(power_spec)]
        
# Plot the results for both
f, (ax1, ax2) = plt.subplots(1, 2, figsize=[24,12])

# Plot particle trajectory ####################################################
ax1.set_title("Max Frequency w.r.t Impact Parameter",fontsize=18)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.tick_params(axis='both', which='major', labelsize=16)
ax1.tick_params(axis='both', which='minor', labelsize=12)
ax1.xaxis.offsetText.set_fontsize(16)
ax1.yaxis.offsetText.set_fontsize(16)
ax1.plot(impact_param, impact_max_freq)
ax1.set_xlabel(r'Impact Parameter ($a_{o}$)',fontsize=24)
ax1.set_ylabel(r'$\omega_{max}$ ($\frac{rad}{s}$)',fontsize=24)
#aax1.axis('equal')

ax2.set_title("Max Frequency w.r.t Initial Velocity",fontsize=18)
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.tick_params(axis='both', which='major', labelsize=16)
ax2.tick_params(axis='both', which='minor', labelsize=12)
ax2.xaxis.offsetText.set_fontsize(16)
ax2.yaxis.offsetText.set_fontsize(16)
ax2.plot(range_vx0, vel_max_freq)
ax2.set_xlabel(r'$v_{x,o}$ ($m/s$)',fontsize=24)
ax2.set_ylabel(r'$\omega_{max}$ ($\frac{rad}{s}$)',fontsize=24)
#ax2.axis('equal')

plt.savefig("peak_frequency.png")