#
# bounce.py
#
# example that comes with VPython
#

from visual import *

floor = box(length=4, height=0.5, width=4, color=color.blue)

ball = sphere(pos=(0,4,0), color=color.green)
ball.vel = vector(0,-1,0)

RATE = 30
dt = 1.0/RATE
while 1:
    rate(RATE)
    ball.pos = ball.pos + ball.vel*dt
    if ball.y < 1:
        ball.vel.y = -ball.vel.y

    else:
        ball.vel.y = ball.vel.y - 100*dt
