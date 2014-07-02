# 
# Name: Theresa Barton
#
# hw1pr1.py (Lab 1, part 1)
# slicing and indexing challenges
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]     
print answer0

# Problem 1:
# Creating the list [7,1] from pi and e
answer1 = e[1:]  
print answer1


answer2 = pi[::-2]  
print answer2

answer3 = pi[1:]   
print answer3

answer4 = e[::-2]+pi[::2]   
print answer4


# starting strings for Lab 1:
h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

answer6 =  c[0:4]+m[1:3]+c[6:]
print answer6


answer7 =  h[1:]+m[1:]
print answer7

answer8 = h[0:3]+m[3]+h[4]+3*(h[0:3])
print answer8

answer9 = c[3:6]+c[1]+m[0]+h[:-3:-1]+c[-2::-4] 
print answer9

answer10 = c[::2]+h[1:3]+c[0]+h[1]+c[2:4]
print answer10



