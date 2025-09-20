from vpython import *

 # Constants
ke = 9e9 # Electrostatic Constant
qproton = 1.6e-19
scaleFactor = 3e-11

 # Objects
particle = sphere(pos = vector(1e-10, 0, 0), radius = 2e-11, color = color.red)
xaxis = cylinder(pos=vec(-5e-10,0,0), axis=vector(10e-10,0,0), radius=2e-12)
yaxis = cylinder(pos=vec(0,-5e-10,0), axis=vector(0,10e-10,0), radius=2e-12)
zaxis = cylinder(pos=vec(0,0,-5e-10), axis=vector(0,0,10e-10), radius=2e-12)

 # The position of the arrow is the observation location:
Earrow = [arrow(pos = vector(3.1e-10,-2.1e-10,0), axis = vector(1e-10,0,0), color = color.orange)]
Earrow.append(arrow(pos = vector(3.1e-10,2.1e-10,0), axis = vector(1e-10,0,0), color = color.orange))
Earrow.append(arrow(pos = vector(-1.1e-10,-2.1e-10,0), axis = vector(1e-10,0,0), color = color.orange))
Earrow.append(arrow(pos = vector(-1.1e-10,2.1e-10,0), axis = vector(1e-10,0,0), color = color.orange))
Earrow.append(arrow(pos = vector(1e-10,0,3e-10), axis = vector(1e-10,0,0), color = color.orange))
Earrow.append(arrow(pos = vector(1e-10,0,-3e-10), axis = vector(1e-10,0,0), color = color.orange))

 # Calculations
for i in range(6) :
     # Write instructions to tell the computer how to calculate the correct 
     # electric field E1 at the observation location (the position of Electric field arrow1, named Earrow1):
    r = Earrow[i].pos - particle.pos
     # change the axis of Earrow1 to point in the direction of the electric field at that location
    E = (ke * qproton) / (mag(r)**2)
    print(E)
     # and scale it so it looks reasonable
    Earrow[i].axis = scaleFactor * E * r


