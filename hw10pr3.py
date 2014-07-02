#####
def createDictionary( filename ):
    """(1) one to process a file and create a dictionary of legal word
        transitionstakes in a string, the name of a text file containing
        some sample text
    """

    f = open( filename )
    text = f.read()
    f.close()

    LoW = text.split()
    d = {}
    prevwd = '$'
    for nextwd in LoW:
        if prevwd not in d:
            d[prevwd]=[nextwd]
        else:
            d[prevwd] += [nextwd]
        prevwd = nextwd
#####
def generateText( d, n ):
    """(2) another to actually generate the new text.
    """
       
    
