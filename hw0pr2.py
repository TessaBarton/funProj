# hw0pr2.py
#
# Name(s): Theresa Barton
#
# Date:9/4/2013
#
#


import random

user = raw_input("Rock, Paper, scissors, you choose first, one is fair, one is foul, and one is useless: ")

if user == 'rock':                                          #always ties
     comp = user

elif user == 'paper':                                       #the foul one
    comp ='scissors'

else :
    comp = random.choice(['rock','paper','scissors'])       #the fair one

   

user2 = raw_input("Are you a gambler? You have a 2/3 chance that the last game wasn't good, and if you want to try again and win with rock paper scissors lizard spock,your last game will be null!")

if user2 == 'no':                               #new input, no or yes
    print 'the user (you) chose', user
    print 'the comp (I) chose', comp
else:
    user3 = raw_input("Glad you're game: rock, paper, scissors, lizard, spock")
    comp3 = random.choice(['rock','paper','scissors','lizard','spock'])

if user3 == comp3:
    print 'tie, tie, tie'
elif user3 == 'rock':
    print' the user (you) chose', user3
    print 'the comp (I) chose', comp3
elif user3 == 'lizard':
    if comp3 == 'rock': print 'I win!'
    elif comp3 == 'paper': print'You win!'
    elif comp3 == 'scissors': print 'I win'
    else: print 'You win'
elif user3 == "paper":
    if comp3 == 'rock': print 'You win!'
    elif comp3 == 'scissors': print 'I win!'
    elif comp3 == 'lizard': print 'You win'
    else: print 'You win'
elif user3 == 'scissors':
    if comp3 == 'rock': print 'I win'
    elif comp3 == 'lizard': print 'I win'
    elif comp3 == 'paper': print'You win!'
    else : 'I win'
else:
    if comp3 == 'paper': print 'you have been disproven, Spock!'            #disproved???
    elif comp3 == 'rock': print 'you have been stoned'                      #G-rated pls!
    elif comp3 == 'lizard': print 'you have been poisoned'
    else:print "I am not sure what scissors does to you anyway, spock!"    #I really don't





print' the user (you) chose', user3
print 'the comp (I) chose', comp3
    
                
        




