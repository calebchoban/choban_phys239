import numpy as np 

# Calculates column density of uniform density cloud of a given depth
# Give parameters in cgs units
def calcColumnDensity(density, distance):
	return density*distance

# Finds cross section for given optical depth, density, and distance
def calcCrossSection(density, opt_depth, distance):
	return opt_depth / calcColumnDensity(density, distance)