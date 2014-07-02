########### TTS SECURITIES ############
import math

########### Helper Functions ##########

def menu():
    """ a function that simply prints the menu """
    print
    print "(0) Input a new list"
    print "(1) Print the current list"
    print "(2) Find the average price"
    print "(3) Find the standard deviation"
    print "(4) Find the min and its day"
    print "(5) Find the max and its day"
    print "(6) Your TT investment plan"
    print "(7) Find the mode"
    print "(9) Quit"
    print
    print
    print
    print

def avg(L):
    """ calculates the average of list L"""
    sm = 0
    for i in range(len(L)):
        sm = sm + L[i]
    av = float(sm/len(L))
    return(av)
        
def sigma(L):
    """ calculates the standard deviation of a list L"""
    m = avg(L)
    s =0
    for i in range(len(L)):
        s = s + (L[i]-m)**2
    j = (s/len(L))
    return(math.sqrt(j))

def smallest(L):
    """ finds the min of the list L, outputs the min and it's day"""
    j = L[0]
    p = 0
    for i in range(len(L)):
        if L[i] < j:
            j = L[i]
            p = i+1
    return [j,p]
def biggest(L):
    """ finds the max of the list L"""
    j = L[0]
    p = 0
    for i in range(len(L)):
        if L[i] > j:
            j = L[i]
            p = i+1
    return [j,p]
def plan(L):
    """ tells you a specific reccomendation time travel strate"""
    n = 0
    bestbuy = 0
    bestsell = 0
    for i in range(len(L)): #i is buy day
        for j in range(len(L)): # sell day
            if i < j:
                if n < L[j]-L[i]:
                    n = L[j]-L[i]
                    bestbuy = i
                    bestsell = j
    print ""
    print "buy on day", bestbuy, "at price", L[bestbuy], "$"
    print "sell on day", bestsell, "at price", L[bestsell], "$"
    print "\n For a total profit of", L[bestsell]-L[bestsell], "$"
    
                
                
            

############ Main #####################
def tts():
    """ the main user-interaction loop """

    L = [0] # a list

    while True:                             #start loop
        print "\nWelcome"
        menu()
        uc = input ("Choose an option: ")

        if uc == 0:                          # new list
            L = input("Enter a new list: ")
            
        elif uc == 1:                        # print list
            print "\nDay Price"
            print "--- -----"
            for i in range(len(L)):
                print i, "   ", L[i]

        elif uc == 2:                        #avg
            mean = avg(L)
            print"\nThe average is",mean

        elif uc == 3:                        #stdev
            s = sigma(L)
            print"\nThe standard deviation is",s

        elif uc == 4:                        #min
            sml = smallest(L)
            print"\nThe minimum is", sml[0], "on day", sml[1]

        elif uc == 5:                        #max
            bg = biggest(L)
            print "\n the max is", bg[0], "on day", bg[1]

        elif uc == 6:
            plan(L)

        elif uc == 9:
            break

        else:
            print "Not a valid option"
            
    print
    print "XOXOXOXOXOXOXOXO"
            

    

