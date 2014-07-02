#
# hw2pr2.py
#
# Name:
#

import random  

def rs():
    """ rs chooses a random step and returns it 
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])
def rwpos( start, nsteps ):
    """ rwpos t returns the position of the sleepwalker
        after nsteps random steps, where each step moves
        according to rs(), which means either plus 1 or
        minus 1 from the previous position.

        args: an integer start, representing the
        starting position of our sleepwalker, and
        a nonnegative integer nsteps, representing the
        number of random steps to take from this starting
        position.
    """
    
    if nsteps == 0:
        return start
        
    else :
        print "start is_" + str(start + rs())
        return rwpos(start + rs() , (nsteps-1))
        

def rwsteps( start, low, hi ):
    """ It should simulate a random walk, printing
        each step (see below). Also, as soon as the
        sleepwalker reaches at or beyond the low or hi
        value, the random walk should stop. When it does
        stop, rwsteps must return the number of steps that
        the sleepwalker took in order to finally reach the
        lower or upper bound.

        start, representing the starting position of our
        sleepwalker,
        an integer low, which will always be nonnegative,
        representing the smallest value our sleepwalker will be allowed to wander to, and
        an integer hi, representing the highest value our
        sleepwalker will be allowed to wander to.
    """
    if start == low or start == hi:
        return 0
    else:
        newstart = start + rs()
        print "|"+str(" "*(newstart))+"i"+(" "*(hi-newstart))+"|" 
        rest_of_steps = rwsteps( newstart, low, hi )
        return rest_of_steps + 1

def rwposPlain( start, nsteps ):
    """ same as rpos, but doesnt print and calculates
        final position minus the starting position.
    """
    if nsteps == 0:
        return start
    else :
        return rwposPlain(start + rs(), (nsteps-1))


    
"""What is the average final signed-displacement for a
    random walker after making 100 random steps?

    I found the average signed displacement to be 0. I created
    a list comprehension that simulated taking 100 random steps
    667 times. although it was not always 0, it was usually pretty close
    this makes sense.
    >>> avg100()
    0
"""

def avg100():
    """ finds average final displacement of walker starting at zero,
        and going 100 steps.
    """
    LC = [ rwposPlain(0,100) for x in range(667) ]
    return (sum(LC))/667

"""What about after N random steps?
    after N random steps I found the value of the signed displacement was
    also centered at zero. I created list comprehensions where n can be inputted
    as N increased, the closeness to zero also increased.
    >>> avgN(105)
    0
    >>> avgN(2)
    -1
"""


def avgN(N):
    """ finds average final displacement of walker starting at zero,
        and going N steps.
    """
    LC = [ rwposPlain(0,N) for x in range(667) ]
    return (sum(LC))/667

"""What is the average squared-displacement for a random walker after making 100 random steps?
    I used the same list comp as above, but squared the rposPlain input.
    I found that the average squared displacement was centered at 100. I do not know why
    I think it is becuase it made every input squared, but in that case it should
    have always outputted 100.
    
"""
def sd100():
    LC = [ (rwposPlain(0,100))**2 for x in range(667) ]
    return (sum(LC))/667
"""What about after N random steps, in terms of N?
    I used the same list comp as the avgN function, and squared the output of
    the rwposPlain. I found that the squared displacemtn was usually close to N.
    I dont know why it was not exactly N.
"""
def sdN(N):
    LC = [ (rwposPlain(0,N))**2 for x in range(667) ]
    return (sum(LC))/667

