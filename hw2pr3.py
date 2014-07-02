#
# gold hw2pr3.py
#
# Name(s): Theresa Barton
#

from turtle import *


# an example: poly(sz,n,N)
def poly( sz, n, N ):
    """ poly draws a regular polygon with
        sz: # of pixels per side
        n:  # of sides yet to draw
        N:  # of sides in the whole polygon
    """
    if n < 1:
        return
    else:
        forward( sz )
        right( 360.0/N )
        poly( sz, n-1, N )

#
# try this out:
# >>> poly(50,7,7); done()
#
# you can customize, too:
# >>> width(5)
# >>> shape( 'turtle' )
# >>> color( 'darkgreen' )
# >>> poly(50,7,7); done()
#


#
# Here, you'll write spiral, svtree, and snowflake
#       and, if you like, your own custom-artwork f'n...
#

def spiral( initialLength, angle, multiplier ):
    """ draws spiral with customizeable intital side lenghts, angles
        and how quickly it gets small. Recurses until the side length
        is less than 1 pixel or greater than 1000 pixels
    """
    if initialLength <= .1 or initialLength >= 1000:
        return 0
    else :
        right(angle)
        forward(initialLength)
        return spiral(initialLength*multiplier, angle, multiplier)
def svtree( trunklength, levels ):
    """draws tree
    """
    if levels == 0: 
        return 
    else:
        forward(trunklength)
        width(1)
        color( 'green')
        left(30)
        svtree(trunklength/2,levels-1)
        right(60)
        color( 'blue' )
        width(.5)
        svtree(trunklength/2,levels-1)
        color( 'yellow')
        width(.25)
        left(30)
        back(trunklength)
        
        
  
    
    
