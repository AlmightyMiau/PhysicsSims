from vpython import *

 # Constants
ke = 9e9 # Electrostatic Constant
qe = 1.6e-19
s = 4e-11
R = 3e-10
scaleFactor = 1e-10

 # Objects
plus = sphere(pos=vector(s/2,0,0), radius=1e-11, color=color.red)
qplus = qe
neg = sphere(pos=vector(-s/2,0,0), radius=1e-11, color=color.blue)
qneg = -qe

 # Calculations
theta = 0
while theta < 2*pi:
	rate(6)
	# The position of the arrow is the observation location:
	obs = arrow(pos=R*vector(cos(theta),sin(theta),0), axis=vector(1e-10,0,0), color=color.orange)
	# electric field plus at the observation location:
	rplus = obs.pos - plus.pos
	# electric field from plus at that location
	Eplus = (ke * qplus) / (mag(rplus)**2) 
	# electric field negative at the observation location:
	rneg = obs.pos - neg.pos
	# electric field from neg at that location
	Eneg = (ke * qneg) / (mag(rneg)**2)
	# Find total electric field
	E = Eplus * rplus + Eneg * rneg
	# and scale it so it looks reasonable
	obs.axis = scaleFactor * E 
	print("theta: ", theta, " obsv: ", obs.pos, " Enet: ", mag(E))
	theta += pi/6


 # Calculations in a different plane
theta = 0
while theta < 2*pi:
	rate(6)
	# The position of the arrow is the observation location:
	obs = arrow(pos=R*vector(cos(theta),0,sin(theta)), axis=vector(1e-10,0,0), color=color.orange)
	# electric field plus at the observation location:
	rplus = obs.pos - plus.pos
	# electric field from plus at that location
	Eplus = (ke * qplus) / (mag(rplus)**2) 
	# electric field negative at the observation location:
	rneg = obs.pos - neg.pos
	# electric field from neg at that location
	Eneg = (ke * qneg) / (mag(rneg)**2)
	# Find total electric field
	E = Eplus * rplus + Eneg * rneg
	# and scale it so it looks reasonable
	obs.axis = scaleFactor * E 
	print("theta: ", theta, " obsv: ", obs.pos, " Enet: ", mag(E))
	theta += pi/6
