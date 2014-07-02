#
# hw2pr1.py (Week 2's CS lab)
#
# Name: Theresa Barton
#
#   (this will be our final "named" hw week...)


# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """ doubler!  input: x, a number """
    return 2*x

def sq(x):
    """ squarer!  input: x, a number """
    return x**2



# examples for getting used to list comprehensions...

def lc_mult( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each multiplied by 2**
    """
    return [ 2*x for x in range(N) ]

def lc_idiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        WARNING: this is INTEGER division...!
    """
    return [ float(x/2) for x in range(N) ]

def lc_fdiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        NOTE: this is floating-point division...!
    """
    return [ float(x)/2 for x in range(N) ]


# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs( N ):
    """ returns a list of evenly spaced left hand endpoints in the unit interval
        args: N= the number of fragments of the unit interval
    """
    return [ float(x)/N for x in range(N) ]


def unitfracs2( N ):
    """ returns a list of evenly spaced left hand endpoints in the unit interval
        args: N= the number of fragments of the unit interval
    """
    return [ float(x)/N for x in range(N) ]

def scaledfracs(low,hi,N):
    """ returns N equally sized fragments from the number segment from low to hi
        args: low, hi, number of fragments
    """
    return [low+x*(hi-low) for x in unitfracs(N) ]
def sqfracs(low,hi,N):
    """ takes output from scaled fracs, and squares it
        args, low number hi number number of intervals
    """
    return [ x**2 for x in scaledfracs(low,hi,N)]

def f_of_fracs(f,low,hi,N):
    """ applies function to equally sized fragments from the number segment from low to hi
        args: low, hi, number of fragments, function to be applied
    """
    return [ f(x) for x in scaledfracs(low,hi,N)]
import math
def c(x):
    return (4 - x**2)**0.5
def integrate(f,low,hi,N):
    """ integrate returns an estimate of the definite integral
          of the function f (the first input)
          with lower limit low (the second input)
          and upper limit hi (the third input)
          where N steps are taken (the fourth input)

        integrate simply returns the sum of the areas of rectangles
        under f, drawn at the left endpoints of N uniform steps
        from low to hi
    """
    return sum(f_of_fracs(f,low,hi,N))*(((1.0*hi)-low)/N)
def recip(x):
    """ the reciprocator! input: val, a number """
    return 1.0/x
def ln(x,N):
    """ computes the natural logarithm of a given x.
        args: x is the hi component, N will determine the number of slices
        bzw the accuracy.
    """
    return integrate(recip,1.0,x,N)


""" Q1.
Using left handed endpoints on increasing functions, integrate will always underestimate functions like this becuase
some area will always be left between the riemann sum rectangle and the function value

a function that would be over estimated would be decreasing on the interval
y=-x^2+2x+10 would be overestimated on this interval

    Q2.
>> integrate(c,0,2,2)
3.732050807568877
>>> integrate(c,0,2,20)
3.2284648797549815
>>> integrate(c,0,2,200)
3.1511769448395297
>>> integrate(c,0,2,2000)
3.1425795059119643

Well the integral is becoming pi (3.14159) I think because the formula for the area
of a circle is pi times the radius squared, and 2 squared is the same as 2*2 =4
so if we are only looking at one forth of the circle the area would be exactly equal to pi, becuase we
take area 4pi and divide by 4

    Q3.
Above


"""

