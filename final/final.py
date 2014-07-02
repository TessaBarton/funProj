# Theresa Barton
# Picobot- room filling program optimization via genetic algorithm generation
# 9-12-13

# import libraries

import random
import math

# defined values

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5

# classes
def valid(pattern):
    """ args: pattern (in form NxEx... ) where the capital letters are walls and the x's are empty squares
        outputs: list [] of direction strings ('N',....) for the rule.
        error handling
    """
    moves = []
    if 'x' in pattern:
        if pattern[0] == 'x':
            moves += 'N'
        if pattern[1] == 'x':
            moves += 'E'
        if pattern[2] == 'x':
            moves += 'W'
        if pattern[3] == 'x':
            moves += 'S'
        return moves
    else:
        print 'ERROR_IN_PATTERN' 

class Program:
    """ represents a single picobot program
    """
    def __init__(self):
        """sets self.rules to be an empty dictionary
        """
        self.rules = {}
        
    def __repr__(self):
        """returns a string representation of the program
        """
        keylist = self.rules.keys()
        keylist.sort()
        rulesstring = ''
        for i in keylist:
            var = self.rules[i]
            rulesstring += str(i[0]) + ' ' + str(i[1])  + ' ' +'->'+ ' ' + str(var[ 0 ])+ ' '  + str(var[1])+'\n'
        return rulesstring


    def randomize(self):
        """ should generate a random, full set of rules for the dictionary, self.rules, basically
            it assigns random (legal) values to all possible keys.
        """
        startingstates = range(NUMSTATES + 1)    
        patterns = [ 'xxxx', 'Nxxx','NExx','NxWx','xxxS','xExS', 'xxWS', 'xExx','xxWx']
        for i in startingstates:
            for j in patterns:
                moves             = valid(j)
                move              = random.choice(moves)
                newstate          = random.choice(startingstates)
                self.rules[(i,j)] = (move,newstate)
    def getMove(self, state, surroundings):
        """ takes in integer state and surroundings ( 1, "xExx") and returns a
            tuple that contains the next move and the new state
        """
        newMove = self.rules[(state,surroundings)]
        return newMove

    def mutate(self):
        """ rewrites a randomly selected rule in the dictionary, changing the associated
            value
        """
        keylist  = self.rules.keys()
        target   = random.choice(keylist)
        states   = range(NUMSTATES + 1)
        moves    = valid(target[1])
        move     = random.choice(moves)
        newstate = random.choice(states)
        self.rules[target] = (move,newstate)
    
   
    def crossover(self, other):
        """takes an other program of type program as input. you need to intitialize
            and randomize this other. then....SEX! just kidding, just some classic
            genetics. it should produce an new offspring program that contains some of the
            rules of self and osmeo fthe rules from other. Don't modify the parents
        """
        p = Program()
        p.rules     = {}
        cross       = random.choice(range(1,3))
        states      = range(cross + 1)
        patterns    = [ 'xxxx', 'Nxxx','NExx','NxWx','xxxS','xExS', 'xxWS', 'xExx','xxWx']
        for i in states:
            for j in patterns:
                p.rules[(i,j)] = self.rules[(i,j)]
        statestwo   = range(cross,6)
        for i in statestwo:
            for j in patterns:
                p.rules[(i,j)] = other.rules[(i,j)]
        return p
        
    
    # note to self, you did not test to make sure that this covers every val in the 
        
                

class World:
    """ simulates a whole picobot enviroment, usually 25X25 empty room, and picobot robot
    """
    def __init__(self, initial_row, initial_col, program):
        """ contains information about where picobot is (row,col), the curent state
            for picobot (which will change) and a LOL that hods the 2d room
            and program, which tells us which program is directing picobots actions
            in the room
        """
        self.prow    = initial_row
        self.pcol    = initial_col
        self.state   = 0
        self.prog    = program
        self.room    =[ [' ']*WIDTH for row in range(HEIGHT) ]
        for i in range(WIDTH):
            self.room[0][i]     = '-'
            self.room[HEIGHT-1][i]= '-'
        for i in range(HEIGHT):
            self.room[i][0]     = '|'
            self.room[i][WIDTH-1] = '|'
        self.room[0][0]         = '+'
        self.room[0][HEIGHT-1]    = '+'
        self.room[WIDTH-1][0]     = '+'
        self.room[WIDTH-1][HEIGHT-1]= '+'

    def __repr__(self):
        """shows the maze with the space character to unvisited cells, the walls with whatever
           character(s) you've chosen, the Picobot's position in
           the maze, and o (lower-case o) characters for empty but
           previously-visited locations in the maze.
        """
        # step method changes blanks to 'o's
        self.room[self.prow][self.pcol] = 'P'
        s = ''
        for row in range(HEIGHT):
            for col in range(WIDTH):
                s += self.room[row][col]
            s+= '\n'
        return s

    def getCurrentSurroundings(self):
        """ returs the surroundings ie walls or blanks of picobot
        """
        surroundings = ''
        if self.room[self.prow-1][self.pcol] ==  '-':
            surroundings += 'N'
        else:
            surroundings += 'x'
        if self.room[self.prow][self.pcol+1] == '|':
            surroundings += 'E'
        else:
            surroundings += 'x'
        if self.room[self.prow][self.pcol-1] == '|':
            surroundings += 'W'
        else:
            surroundings += 'x'
        if self.room[self.prow+1][self.pcol] ==  '-':
            surroundings += 'S'
        else:
            surroundings += 'x'
        
        
        return surroundings
        
        
    def step(self):
        """ moves picobot one step and updates self.room + self.row,self.col,
            self.state
        """
        self.room[self.prow][self.pcol] = 'o'
        sur     = self.getCurrentSurroundings()
        state   = self.state
        move    = self.prog.getMove(state,sur)
        self.state = move[1]
        if move[0] == 'N':
            self.prow -= 1
        if move[0] == 'E':
            self.pcol += 1
        if move[0] =='W':
            self.pcol -= 1
        if move[0] == 'S':
            self.prow += 1
        
        
    def run(self, steps):
        """inputs number of steps to move, executes that number of steps
        """
        while steps > 0:
            self.step()
            steps -= 1

    def fractionVisitedCells(self):
        """that returns the floating-point fraction of cells in self.room
           that are marked as visited (including Picobot's current location).
        """
        p          = 0
        pixels     = WIDTH*HEIGHT*1.0
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.room[i][j] == 'o' or self.room[i][j] == 'P':
                    p += 1
        return p/pixels

# helpers

TRIALS = 30
STEPS  = 1500
NTILE = .85

def genPop(size):
    """takes as input a population size and returns a population (a Python list)
       of that many random Picobot programs
    """
    pop       = [Program() for i in range(size)]
    poprandom = [p.randomize() for p in pop]
    return pop
    
    

def evaluateFitness(program, trials, steps):
    """Args: picobot prog, trials(number of randing starting points to be tested) steps,
             allowed number of steps for each programs sim
       Returns: fitness (fp val betwixt 0.0 and 1.0) that from fractionVisitedCells
    """
    total = 0*1.0
    for i in range(trials):
        row = random.choice(range(1,WIDTH-1))    # range probs, gave up and changed it up
        col = random.choice(range(1,HEIGHT-1))
        w = World(row,col,program)
        w.run(steps)
        total += w.fractionVisitedCells()
    return total/trials

def fitSort(L,keep):
    """ arg: a list of tuples to be sorted, the top ntile - magic number
    """
    L.sort()
    seg         = int(len(L)*keep)
    Lnew        = L[seg:]
    bestprogs   = []
    for i in Lnew:
        bestprogs.append(i[1])
    return bestprogs
def fitBest(L):
    """ literally the same as the last one, except returns only the very best prog
    """
    besttuple =max(L)
    return besttuple[1]
    
def ave(List):
    """ calculates the mean of a list """
    s = sum(List)
    l = len(List)
    return s/l

def proCreate(besttile,popsize,muterate):
    """ breeds a new generation (basic!) of the same size as the old.
    """
    offspring = []
    kiddies   = popsize - len(besttile)    # we are the 90%, well,..
    for i in besttile:
       offspring.append(i)
    for i in range(kiddies):
        parentone = random.choice(besttile)
        parenttwo = random.choice(besttile)
        baby      = parentone.crossover(parenttwo)
        offspring.append(baby)
    for j in offspring:
        coinflip = random.choice(range(muterate))
        if coinflip == 1:
            j.mutate()
    return offspring
        
# main

def GA(popsize,numgens):
    """ args: size of populations, number of generations
        generates popsize random progs
        evaluates the fitness of all those programs
        extract a subset of those programs
        create a new population (eeeee)
    """
    population = genPop(popsize)
    gen        = numgens
    itr        = 0
    while gen > 0:
        itr += 1
        #fitness of current population
        fitlist    = []
        fitprint   = []
        for i in population:
            fit    = evaluateFitness(i,TRIALS,STEPS)
            fitprint.append(fit)
            fitlist.append(tuple((fit,i)))
        print 'Generation', numgens - gen ,'\n'
        print '  ' + 'Average Fitness', ave(fitprint), '\n'
        print '  ' + 'Best Fitness', max(fitprint),'\n'
        gen -= 1
        # optimization step
        if itr<= 10:
            besttile   = fitSort(fitlist,.9)    # fitlist is tuples, fitSort just returns the programs for the best tuple
        else:
            besttile   = fitSort(fitlist,.9)
        if itr <= 5:
            muterate   = 1
            population = proCreate(besttile,popsize,muterate)
        else:
            muterate   = 3
            population = proCreate(besttile,popsize,muterate)
            
            
    # conclusion
    fitlist        = []
    for i in range(0,len(population)):
        prog       = population[i]
        fit        = evaluateFitness(prog,TRIALS,STEPS)
        fitlist.append(tuple((fit,prog)))
    print 'The optimized picobot program is:'
    print fitBest(fitlist)


        

    
        
    
        

    
    

                
        
            
        
        
        
                

    
    
