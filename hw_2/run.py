from radiativeTransferFunctions import *
import matplotlib.pyplot as plt
import numpy as np

pcToCm = 3.086E18

# all parameters given in cgs
density = 1; depth = 100*pcToCm;

###############################################################################

print "Problem 1"
cross_sects = np.zeros(3)
print "Column density of cloud is", calcColumnDensity(density,depth), "cm^-2"
cross_sects[0] = calcCrossSection(density, 10**-3, depth)
print "a) cross section =", cross_sects[0], "cm^2"
cross_sects[1] = calcCrossSection(density, 1, depth)
print "b) cross section =", cross_sects[1], "cm^2"
cross_sects[2] = calcCrossSection(density, 10**3, depth)
print "c) cross section =", cross_sects[2], "cm^2"

###############################################################################

print "Problem 3"
print "Plot frequecy dependant cross section"
crit_freq = 1000
freq_range = [0, 2000]
steps = 10000
std_dev = 100
foutname = "problem3"
titles = ['a','b','c']
for i,crit_sec in enumerate(cross_sects):
    cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
    plt.figure()
    plt.title(r'$\sigma_{\nu}$ for $\sigma_{\nu,o}=$ %.3e' % crit_sec)
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\sigma_{\nu}$')
    plt.plot(freqs, cross_sec)
    plt.savefig(foutname+titles[i]+'.png')

###############################################################################

print "Problem 4"
print "Plot specific intensities for given cases"
crit_freq = 1000
freq_range = [0, 2000]
# Used for text on dashed lines in plot 
x_coord = freq_range[0] + (freq_range[1] - freq_range[0]) * 5./6.
steps = 1000
std_dev = 100
source = 3
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row',figsize=[16,12])

# Very large optical depth at all frequencies
crit_sec = cross_sects[2]
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, const, crit_sec)
init_intens = 1
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax1.set_ylim([0,4])
ax1.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax1.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax1.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax1.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax1.plot(freqs, intensities)
ax1.set_title(r'$\tau_{\nu}(D)\gg 1$')
ax1.set_ylabel(r'$I_{\nu}$')

# Zero initial intensity and low optical depth
crit_sec =  calcCrossSection(density, 0.75, depth)
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
init_intens = 0
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax2.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax2.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax2.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax2.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax2.plot(freqs, intensities)
ax2.set_title(r'$I_{\nu}(0)=0$ and $\tau_{\nu}(D)<1$')

# Initial intensity less than source and low optical depth
optical_depth = 0.75
init_intens = 1.5
crit_sec =  calcCrossSection(density, optical_depth, depth)
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax3.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax3.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax3.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax3.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax3.plot(freqs, intensities)
ax3.set_title(r'$I_{\nu}(0)<S_{\nu}$ and $\tau_{\nu}(D)<1$')

# Initial intensity greater than source and low optical depth
source = 1
init_intens = 2
optical_depth = 0.75
crit_sec =  calcCrossSection(density, optical_depth, depth)
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax4.set_ylim([0,4])
ax4.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax4.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax4.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax4.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax4.plot(freqs, intensities)
ax4.set_title(r'$I_{\nu}(0)>S_{\nu}$ and $\tau_{\nu}(D)<1$')
ax4.set_xlim(freq_range)
ax4.set_xlabel(r'$\nu$')
ax4.set_ylabel(r'$I_{\nu}$')

# Initial intensity less than source and low optical depth expect at critical freq
source = 3
init_intens = 1.5
optical_depth = 10
crit_sec =  calcCrossSection(density, optical_depth, depth)
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax5.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax5.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax5.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax5.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax5.plot(freqs, intensities)
ax5.set_title(r'$I_{\nu}(0)<S_{\nu}$ and $\tau_{\nu}(D)<1$ while $\tau_{\nu,o}(D)>1$')
ax5.set_xlim(freq_range)
ax5.set_xlabel(r'$\nu$')


# Initial intensity greater than source and low optical depth expect at critical freq
source = 1
init_intens = 2
optical_depth = 10
crit_sec =  calcCrossSection(density, optical_depth, depth)
cross_sec,freqs = calcFreqCrossSec(freq_range, steps, gaussian, [crit_sec, std_dev, crit_freq])
intensities = np.zeros(np.size(cross_sec))
for i,sec in enumerate(cross_sec):
    intensities[i] = calcSpecIntens(init_intens, sec, source, depth, density, steps)[-1]
ax6.plot(freqs, np.full(np.shape(freqs),source), '--k')
ax6.plot(freqs, np.full(np.shape(freqs),init_intens), '--k')
ax6.annotate(r'$S_{\nu}$', xy=(x_coord,source+0.1), xycoords='data')
ax6.annotate(r'$I_{\nu}(0)$', xy=(x_coord,init_intens+0.1), xycoords='data')
ax6.plot(freqs, intensities)
ax6.set_title(r'$I_{\nu}(0)>S_{\nu}$ and $\tau_{\nu}(D)<1$ while $\tau_{\nu,o}(D)>1$')
ax6.set_xlim(freq_range)
ax6.set_xlabel(r'$\nu$')

plt.savefig("problem4.png")