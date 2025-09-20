from vpython import *

 # Constants
ke = 9e9 # Electrostatic Constant
qe = 1.6e-19
s = 4e-11
R = 3e-10
scaleFactor = 1e-12
numObs = 24#24
obsStartRadius = 4

 # Objects
plus = sphere(pos=vector(s/2,0,0), radius=1e-11, color=color.red)
qplus = qe
neg = sphere(pos=vector(-s/2,0,0), radius=1e-11, color=color.blue)
qneg = -qe
obs = []

# Create the observation points
for theta in range(numObs):
	obs.append(sphere(pos=s/obsStartRadius*vector(obsStartRadius/2+cos(theta*2*pi/numObs), sin(theta*2*pi/numObs), 0), radius=5e-12, color=color.green, make_trail=True))
	print(obs[theta].pos)

 # Calculations
# test

for i in range(3600):#3600
	rate(30)
	for j in range(numObs):
		# electric field plus at the observation location:
		rplus = obs[j].pos - plus.pos
		if mag(rplus) < s/10:
			continue
		if mag(rplus) > s*5:
			obs[j].pos.x = -(obs[j].pos.x * 0.9)
			continue
		# electric field from plus at that location
		Eplus = (ke * qplus) / (mag(rplus)**2) 
		# electric field negative at the observation location:
		rneg = obs[j].pos - neg.pos
		if mag(rneg) < s/10:
			continue
		if mag(rneg) > s*5:
			obs[j].pos.x = -(obs[j].pos.x * 0.9)
			continue
		# electric field from neg at that location
		Eneg = (ke * qneg) / (mag(rneg)**2)
		# Find total electric field
		E = Eplus * rplus + Eneg * rneg
		# Find the unit vector
		rhat = E / mag(E)
		#print("Rhat: ", rhat)
		# and scale it so it looks reasonable
		#print("E:   ", mag(E))
		#print("s/4: ", s/16)
		if scaleFactor * mag(E) < s:
			obs[j].pos += scaleFactor * mag(E)/16 * rhat
		else:
			obs[j].pos += scaleFactor * rhat
		#print("Eplus[", Eplus, "] * rplus[", rplus, "], Charge", qplus)
		#print("Eneg[", Eneg, "] * rneg[", rneg, "], Charge", qplus)
		#print(" = E[", E, "]")
		#print(" obs: ", obs[j].pos, " E: ", mag(E))
