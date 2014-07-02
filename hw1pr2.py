#
# hw1pr2.py (Lab1, part 2)
#
# Name: Theresa Barton
# 9/11-12/2012


def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x
def sq(x):
    """ output: sq returns square of input
        input x: a number (int or float)
    """
    return x**2
def interp (low, hi, fraction):
    """ output: interp returns a number witch represents the number which falls at the specified fraction di
        stance between the low and the hi
        input: low, hi, fraction real numbers
    """
    x = hi-low
    y = fraction*x
    return float(low + y)

def checkends(s):
    """ output:tells you if the if the first charactar in the string matches the last character
        input:alphanumeric string
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

def flipside(s):
    """ output: string whose first half is s's second half and whose second half is s's first half.
        input: a string s
    """
    x = len(s)
    n = int(.5*(x))
    return s[n:]+s[:n]

def convertFromSeconds(s):
    """ output:(days, hours, minutes, seconds) represented in a nonnegative integer of seconds
        input: nonnegative integer of seconds
    """
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s/ (60*60)
    s = s % (60*60)
    minutes = s/ (60)
    s= s % 60
    seconds = s
    return [days, hours, minutes, seconds]

def front3(s):
    """ output: first three charactars in the string 3x
        input: alphanumeric string
    """
    z = s[:3]
    return 3*z

def married(low,hi):\
    """ output date when it is optimal to pop the question.
        input lowest age when man considers woman wife material input highest age willing to wait to get married
    """
    z= hi-low
    j= z*.368
    return low+j


    

