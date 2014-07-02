#
# for testing VPython...
#

from visual import *
c = cylinder(pos=(0,0,0))

c.color = (1.0,0.0,1.0)

print "c.pos is", c.pos  # vector
print "c.color is", c.color
sleep(2)

#c.pos = vector(10,10,0)
#print "x,y,z", c.pos.x, c.pos.y, c.pos.z


scene.autoscale = False
b = box(pos=(4,0,0))
b.color = color.red

s = sphere(pos=(0,0,4))
s.color = color.blue



while True:
  rate(100) # limits the loop rate in hz 
  dt = 0.01 # the loop time
  s.pos += dt*vector(0,1.0,0)
  print "s.pos is", s.pos




