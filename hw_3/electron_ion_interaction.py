import numpy as np

# Uses Euler Method to determine trajectory of electron interacting with ion
# Requires intial (x0,y0) position and velocity (vx0,vy0), the total time, and 
# number of steps.
def EulerSolver(x0, v0, num_steps, time, func):
	dt = time*1.0 / num_steps
	pos_x = np.zeros(num_steps); pos_x[0] = x0[0];
	pos_y = np.zeros(num_steps); pos_y[0] = x0[1];
	vel_x = np.zeros(num_steps); vel_x[0] = v0[0];
	vel_y = np.zeros(num_steps); vel_y[0] = v0[1];
	acc_x = np.zeros(num_steps); acc_x[0] = 0;
	acc_y = np.zeros(num_steps); acc_y[0] = 0;
	time = np.zeros(num_steps);

	for i in range(1,num_steps):
		time[i] = dt * i
		acc = func(pos_x[i-1],pos_y[i-1],vel_x[i-1],vel_y[i-1],time[i-1])
		if pos_x[i-1] == 0:
			angle = -np.pi/2;
		else:
			angle = np.arctan(-pos_y[i-1]/pos_x[i-1])
		acc_x[i-1] = acc * np.cos(angle)
		acc_y[i-1] = acc * np.sin(angle)
		vel_x[i] = vel_x[i-1] + dt*acc_x[i-1]
		pos_x[i] = pos_x[i-1] + dt*vel_x[i-1]
		vel_y[i] = vel_y[i-1] + dt*acc_y[i-1]
		pos_y[i] = pos_y[i-1] + dt*vel_y[i-1]

	return pos_x, pos_y, vel_x, vel_y, acc_x, acc_y, time


# Gives acceleration due to electric force on an electron from an ion of 
# charge Ze at the origin, given the position and velocity of the charge 
# in x,y coordinates
def electricForce(x, y, vx, vy, t):
	me = 9.11E-31; # electron mass (kg)
	e = 1.6E-19; # electron charge (C)
	perm = 8.85E-12;# vacuum permittivity (C V^-1 m^-1)
	Z = 10;
	dist = np.sqrt(x**2 + y**2)
	force = Z*e**2 / (4*np.pi*perm*dist**2)
	return force / me