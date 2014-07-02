#
# hw11pr2.py
#

import math
from visual import *

class Alien:
    """ This class represents a three-eyed alien object...
    """

    def __repr__(self):
        """ The printable representation of an Alien """
        s = ''
        s += "This alien is at "
        s += str( self.f.pos )
        s += " with vel = " + str( self.vel )
        return s

    # The constructor, named __init__ (as always in Python)
    def __init__(self, init_framepos):
        """ The constructor creates a frame (container)
            at initial location init_framepos
        """
        # a frame is VPython's collection of shapes
        # within a single coordinate system
        self.f = frame(pos=init_framepos)

        # the alien's velocity
        self.vel = vector(0,0,0)

        # all of these parts are within the frame self.f
        self.body = sphere(pos=vector(0,0,0),
                           radius=1,
                           color=color.green,
                           frame=self.f)
        
        self.left_eye = sphere(pos=self.body.pos + vector(.35,.5,.6),
                               radius=0.30,
                               color=color.white,
                               frame=self.f)
        
        self.right_eye = sphere(pos=self.body.pos + vector(-.35,.5,.6),
                                radius=0.30,
                                color=color.white,
                                frame=self.f)
        self.nose = pyramid(pos=self.body.pos + vector(0,0,1),
                                axis = vector(0,0,1),
                                frame=self.f,
                                color=color.red)
                            


    def check_for_collision( self, collider, r ):
        """ checks for a collision with the collider
            at a radius of r
        """
        # mag is the magnitude of a vector, similar to abs for numbers
        if mag( self.f.pos - collider.pos ) < r:
            return True  # collided (within r)
        else:
            return False




