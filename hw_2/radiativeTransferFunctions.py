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
# given function with given parameters for that function.
def calcFreqCrossSec(freq_range, steps, function, params='None'):
    # Check that given freq_rane is mcuh larger than FWH
    df = (freq_range[1] - freq_range[0])/float(steps)
    freqs = np.arange(freq_range[0], freq_range[1], df)
    cross_section = function(params, freqs)
    return cross_section, freqs

def gaussian(params, data):
    amp = params[0]; std_dev = params[1]; center = params[2]
    return amp * np.exp(-np.power(data - center,2)/(2*std_dev**2))

def const(params, data):
    return np.full(np.shape(data),params)
    