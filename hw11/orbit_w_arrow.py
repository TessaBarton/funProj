#
# orbit example, with force arrow
#


from visual import *

e = sphere(pos=(0,0,10),color=color.blue) #earth
s = sphere(color=color.yellow,radius=2)   #sun
a = arrow(pos=e.pos, axis=(0,0,-2),
          shaftwidth=0.3)


scene.autoscale = False    # allow our own motions

e.vel = vector(5,0,0)      # initial velocity

RATE = 50
dt = 1.0/RATE
k = 70.0                   # G!

diff = s.pos - e.pos       # vector difference
force = k*diff/(mag(diff)**2)  # mag
conv = 2.0/mag(force)      # conversion factor to arrow length

while True:
    rate(RATE)
    diff = s.pos - e.pos   # vector difference
    force = k*diff/(mag(diff)**2)  # mag
    e.vel += dt*force      # acceleration d.e.
    e.pos += dt*e.vel      # velocity d.e.
    a.axis = conv*mag(force)*norm(force)
    a.pos = e.pos - (1 + mag(a.axis))*norm(diff)
    
