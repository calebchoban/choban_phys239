from radiativeTransferFunctions import *

pcToCm = 3.086E18

# all parameters given in cgs
density = 1; depth = 100*pcToCm;

print "Problem 1"
print "Column density of cloud is", calcColumnDensity(density,depth), "cm^-2"
print "a) cross section =", calcCrossSection(density, 10**-3, depth), "cm^2"
print "b) cross section =", calcCrossSection(density, 1, depth), "cm^2"
print "c) cross section =", calcCrossSection(density, 10**3, depth), "cm^2"
