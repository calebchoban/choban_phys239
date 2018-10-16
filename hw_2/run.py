from radiativeTransferFunctions import *
import matplotlib.pyplot as plt

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

source = 1; init_intens=0;
#cross_sec = calcCrossSection(density, 10**0, depth)
#print "Problem 2"
#print calcSpecIntens(init_intens, cross_sec, source, depth, density, 100)

print "Problem 3"
print "Plot frequecy dependant cross section"
crit_freq = 1000
freq_range = [1, 2000]
steps = 10000
std_dev = 50
for crit_sec in cross_sects:
    cross_sec,freqs = calcFreqCrossSec(freq_range, steps, crit_sec, std_dev, crit_freq)
    plt.figure()
    plt.title(r'$\sigma_{\nu}$ for $\sigma_{\nu,o}=$ %.3e' % crit_sec)
    plt.plot(freqs, cross_sec)
    
print "Problem 4"



