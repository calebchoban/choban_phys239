import numpy as np 

# Calculates column density of uniform density cloud of a given depth
# Give parameters in cgs units
def calcColumnDensity(density, distance):
	return density*distance

# Finds cross section for given optical depth, density, and distance
def calcCrossSection(density, opt_depth, distance):
	return opt_depth / calcColumnDensity(density, distance)

# Calculates change in intensity of light rays of a given intial intensity, 
# through a cloud of a given cross section, depth, and source.
def calcSpecIntens(init_intens, cross_sec, source, distance, density, steps):
	ds = distance/steps # step size
	intens = np.zeros(steps)
	positions = np.arange(0, distance+ds, ds)

	for i, val in enumerate(intens):
		if i == 0:
			intens[i] = init_intens
			continue
		pos = positions[i]
		opt_depth  = cross_sec * calcColumnDensity(density, ds)
		intens[i] = intens[i-1]*np.exp(-opt_depth) + source*(1-np.exp(-opt_depth))

	return intens

# Calculates the cross section as a function of frequency in the shape of a 
# Gaussian centered at a specfic frequency.
def calcFreqCrossSec(freq_range, steps, amp, std_dev, crit_freq):
    # Check that given freq_rane is mcuh larger than FWH
    FWHM = 2.355 * std_dev
    if freq_range[1] - crit_freq < 5 * FWHM or crit_freq - freq_range[0] < 5 * FWHM:
        print FWHM
        print "Frequency range too small for given standard deviation"
        return
    df = (freq_range[1] - freq_range[0])/float(steps)
    freqs = np.arange(freq_range[0], freq_range[1], df)
    cross_section = amp * np.exp(-np.power(freqs - crit_freq,2)/(2*std_dev**2))
    return cross_section, freqs