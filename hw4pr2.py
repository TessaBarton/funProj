
def numToBaseB( N,B ):
    """ takes as input a non-negative (0 or larger) integer N and a
        base B (between 2 and 10 inclusive) and returns a string
        representing the number N in base B.
    """
    if N == 0:
        return ''
    else:
        return numToBaseB( N/B,B ) + str( N%B )
    

def baseBToNum( S, B ):
    """takes as input a string S and a base B where S represents a
        number in base B where B is between 2 and 10 inclusive. turns to int
    """
    if S == '':
        return 0
    else:
        return B*baseBToNum(S[:-1],B )+ int( S[-1])

def baseToBase( B1,B2,s_in_B1):
    """takes three inputs: a base B1, a base B2 (both of which are
       between 2 and 10, inclusive) and s_in_B1, which is a string
       representing a number in base B1.
       baseToBase should return a string representing the same number
       in base B2.
    """
    J = baseBToNum(s_in_B1,B1)
    return numToBaseB(J,B2)
def add(S,T):
    """takes two binary strings S and T as input and returns their
        sum, also in binary.
    """
    J1 = baseBToNum( S,2 )
    J2 = baseBToNum( T,2 )
    R = J1+J2
    return numToBaseB( R,2)
def addB(S,T):
    """takes two strings as input. return a new string representing
        the sum of the two input strings. The sum needs to be computed
        using the binary addition algorithm.
    """
    if len(S)== 0 :
        return T
    if len(T) == 0:
        return S
    eS = S[-1]
    eT = T[-1]
    if eS == '0' and eT == '0':
        return addB(S[:-1],T[:-1]) + '0'
    if eS == '1' and eT == '0':
        return addB(S[:-1],T[:-1]) + '1'
    if eS == '0' and eT == '1':
        return addB(S[:-1],T[:-1]) + '1'
    if eS == '1' and eT == '1':
        return addB(addB(S[:-1],'1'),T[:-1]) + '0'
def frontNum(S):
    """counts number of first digit repeating in string of binary numbers
        returns number of numbers
    """
    if len(S) <= 1:
        return len(S)
    elif S[0] == S[1]:
        return frontNum(S[1:])+1
    else:
        return 1
def make7(S):
    """turns an binary string of arbitrary length into an 8 digit string
        with 0s out front
    """
    P = 7-len(S)
    if len(S) >= 65:
        return 'oh no! overflow'
    else:
        return P*'0' + S

def compress(S):
    """takes a binary string S of length less than or equal to 64 as
       input and returns another binary string as output. The output
       binary string should be a run-length encoding of the input
       string
       The first bit of each byte represents the bit that will appear
       next in the image, either 0 or 1.
       The final seven bits contain the number in binary of those bits
       that appear consecutively at the current location in the image.
    """
    if S == '':
        return ''
    else:
        F = frontNum( S )
        G = numToBaseB( F,2 )
        B = make7(G)
        H = S[0]
        return str(H) + B + compress(S[F:])

def uncompress(C):
    """that "inverts" or "undoes" the compressing in your compress
       function. Takes 8 bits of the compress and translates that into
       the original 1:1 binary string of an image
    """
    if C == '':
        return ''
    else:
        F = baseBToNum(C[1:8],2)
        return C[:1]*F + uncompress(C[8:])
    
    
    
    
