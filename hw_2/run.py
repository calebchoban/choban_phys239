from radiativeTransferFunctions import *
import matplotlib.pyplot as plt
import numpy as np

pcToCm = 3.086E18

# all parameters given in cgs
density = 1; depth = 100*pcToCm;

print "Problem 1"
cross_sects = np.zeros(3)
print "Column density of cloud is", calcColumnDensity(density,depth), "cm^-2"
cross_sects[0] = calcCrossSection(density, 10**-3, depth)
print "a) cross section =", cross_sects[0], "cm^2"
cross_sects[1] = calcCrossSection(density, 1, depth)
print "b) cross section =", cross_sects[1], "cm^2"
cross_sects[2] = calcCrossSection(density, 10**3, depth)
print "c) cross section =", cross_sects[2], "cm^2"


print "Problem 3"
print "Plot frequecy dependant cross section"
crit_freq = 1000
freq_range = [1, 2000]
steps = 10000
std_dev = 50
for crit_sec in cross_sects:
    cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
    plt.figure()
    plt.title(r'$\sigma_{\nu}$ for $\sigma_{\nu,o}=$ %.3e' % crit_sec)
    plt.plot(freqs, cross_sec)




"""
print "Problem 4"
crit_freq = 1000
freq_range = [1, 2000]
steps = 1000
std_dev = 50
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row',figsize=[16,12])
# Very large optical depth at all frequencies
crit_sec = cross_sects[2]
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, crit_sec, std_dev, crit_freq)
init_intens = 1; source = 3; 
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax1.plot(freqs, intensities)
ax1.set_title(r'$\tau_{\nu}(D)\gg 1$')

ax2.set_title(r'$I_{\nu}(0)=0$ and $\tau_{\nu}(D)<1$')

ax3.set_title(r'$I_{\nu}(0)<S_{\nu}$ and $\tau_{\nu}(D)<1$')

ax4.set_title(r'$I_{\nu}(0)>S_{\nu}$ and $\tau_{\nu}(D)<1$')

ax5.set_title(r'$I_{\nu}(0)<S_{\nu}$ and $\tau_{\nu}(D)<1$ while $\tau_{\nu,o}(D)>1$')

ax6.set_title(r'$I_{\nu}(0)>S_{\nu}$ and $\tau_{\nu}(D)<1$ while $\tau_{\nu,o}(D)>1$')
"""

