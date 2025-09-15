# this one has a little bit of inertia/acceleration

from vpython import *

 # Constants
ke = 9e9 # Electrostatic Constant
qe = 1.6e-19
s = 4e-11
R = 3e-10
scaleFactor = 1e-12

numObs = 36
numParticles = 14      #   3<x<9      x<=16
chargeArrangement = 1 # 0:-+-+-+, 1: ---+++

startRadius = 4 # radius of s/[x] for obs from their particle 

class chargedParticle:
	def __init__(self, charge, posx, posy, posz):
		self.charge = charge * qe
		self.sphere = sphere( 
			pos=vector(posx, posy, posz), 
			radius=1e-11, 
			color=color.red if charge > 0 else color.blue
		)
class lineParticle:
    def __init__(self, posx, posy, posz):
        self.velocity = vector(0,0,0)
        self.isDead = False
        self.sphere = sphere(
            pos=vector(posx, posy, posz),
            radius=5e-12,
            color=color.green,
            make_trail=True
        )

# Objects
# list of charged particles
particles = []
obs = []

# Create rod of particles
initX = s * numParticles / 2
for i in range(numParticles):
	if chargeArrangement == 0: # 0:-+-+-+
		particles.append(
			chargedParticle(
				1 if i % 2 == 0 else -1, 
				initX - s * i, 0, 0
			)
		)
	elif chargeArrangement == 1: # 1: ---+++
		particles.append(
			chargedParticle(
				1 if i < numParticles / 2 else -1, 
				initX - s * i, 0, 0
			)
		)

# Create the observation points around the postive charges
positives = 0 # number of positive particles
for particle in particles:
	if particle.charge > 0:
		for theta in range(numObs):
			# full circle (theta*2pi) split into [numObs] parts
			angle = theta * 2 * pi / numObs 
			radius = s / startRadius
			obs.append( 
                lineParticle(
                    particle.sphere.pos.x + radius * cos(angle),
                    particle.sphere.pos.y + radius * sin(angle),
                    particle.sphere.pos.z
                )
			)


 # Calculations
for i in range(3600):#3600
	rate(30)
	for line in obs: # for each electric field line
		if line.isDead: continue
		E = vector(0,0,0)   # create blank force vector
		for particle in particles: # calculate force from each particle
			# electric field at the observation location:
			r = line.sphere.pos - particle.sphere.pos # dist from particle
			# checking distances
			if mag(r) < s/10:
				line.isDead = True
				continue
			if mag(r) > s*10:
				scene.autoscale = False
			if mag(r) > s*20:
				line.isDead = True
				line.sphere.clear_trail()
				continue
			# electric field from particle at that location
			E += r * (ke * particle.charge) / (mag(r)**2)
		if mag(E) < s/10:
			line.isDead = True
			continue
		# Find the unit vector
		rhat = E / mag(E)
		# print("E:      ", E)
		# print("mag(E): ", mag(E))
		# print("rhat:   ", rhat)
		# and scale it so it looks reasonable
		#if scaleFactor * mag(E) < s:
		#line.sphere.pos += scaleFactor * mag(E)/16 * rhat
		#else:
		#line.sphere.pos += scaleFactor * rhat
		#print(" obsv: ", obs[j].pos, " Enet: ", mag(E))
		line.velocity = scaleFactor * rhat + line.velocity / 2
		line.sphere.pos += line.velocity
		#print(" = E[", E, "]")
