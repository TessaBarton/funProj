## Theresa Barton Hw1Pr3

def mult( a,b ): 
    """  mult returns the product of its two input integers
             inputs: n and m are both integers
             outputs: the result of multiplication
    """
    if b == 0 :
        return 0
    elif b < 0:
        return -a + mult( a,b+1 )
    else:
        return a+mult( a,b-1 )



def dot( l,k ):
    """ dot returns the dot product of the two lists, l, k.
             input: lists of integers of equal length!
             output: the dot product (multiply together and then add elements)
    """
    if len(l) != len(k) :
        print (0.0)
    elif len(l)==len(k)== 0 :
        return 0
    else:
        return (l[0]*k[0]) + dot(l[1:],k[1:])

def ind( e,L ):
    """ ind returns the indx at which element e is first found in list l
        input: element e, list L, put in form os string
        output: value of index at which e is first found in L
    """
    if e == L[0]:
        return 0
    elif e not in L:
        return len(L)
    else:
        return 1+ind(e,L[1:])



def letterScore( let ):
    """  takes single character string, produces value of character if scrabble
         input: single character
         output: value as scrabble tile
    """
    if let in ['a','n','o','e','r','s','t','u','i','l']:
        return 1
    elif let in ['b','c','p','m']:
       return 3
    elif let in ['d','g']:
        return 2
    elif let in ['f','h','v','y','w']:
        return 4
    elif let in ['j','x'] :
        return 8
    elif let in ['q','z']:
        return 10
    elif let in ['k']:
        return 5
    else:
        return 0

def scrabbleScore ( S ):
    """ calculates the score of a word in scrabble
        output: numerical score of letters
        input: lowercase string of charactars a-z
    """
    if S[0] == '':
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore (S[1:])

def one_dna_to_rna( c ):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide
    """
    if c == 'A': return 'U'
    elif c == 'T': return 'A'
    elif c == 'C': return 'G'
    elif c == 'G': return 'C'
    else: return 'Not a base'
        
def transcribe( S ):
     """ transcribes sequence of mRNa from single strand S of DNA
        input: DNA string
        output: mRNA
     """
     if S == '':
        return ''
     else:
        return one_dna_to_rna(S[0])+transcribe(S[1:])


#
# I finished all of the CodingBat STRING problems.
#
    
     
