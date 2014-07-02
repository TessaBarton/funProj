# Hw 10, pr2 for CS 5 gold, 2009
#
# The Board class from CS 5 Hw #10
# for use as a starting point for
# Hw#11, the Player class (and AI)
#

import random


# assume 7 column, 6 row

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [ [' ']*width for row in range(height) ]
        # do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it


    def set_board( self, LoS ):
        """ sets the board to the characters in the
            list of strings named LoS
        """
        for row in range( self.height ):
            for col in range( self.width ):
                self.data[row][col] = LoS[row][col]
                

    def setBoard( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'


    def set( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print self

    def clear( self ):
        """ the software version of the little
            blue slider that releases all of the checkers!
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1
        
    def addMove2( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove( self, col ):
        """ removes the checker from column col """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return
        
    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull( self ):
        """ returns True if the board is completely full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True

    def gameOver( self ):
        """ returns True if the game is over... """
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX( self, row, col, ox ):
        """ checks if the spot at row, col is legal and ox """
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor( self, ox ):
        """ checks if the board self is a win for ox """
        for row in range( self.height ):
            for col in range( self.width ):
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col, ox ) and \
                   self.isOX( row+2, col, ox ) and \
                   self.isOX( row+3, col, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row, col+1, ox ) and \
                   self.isOX( row, col+2, ox ) and \
                   self.isOX( row, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col+1, ox ) and \
                   self.isOX( row+2, col+2, ox ) and \
                   self.isOX( row+3, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col-1, ox ) and \
                   self.isOX( row+2, col-2, ox ) and \
                   self.isOX( row+3, col-3, ox ):
                    return True
        return False

    def hostGame( self ):
        """ hosts a game of Connect Four """

        nextCheckerToMove = 'X'
        
        while True:
            # print the board
            print self

            # get the next move from the human player...
            col = -1
            while not self.allowsMove( col ):
                col = input('Next col for ' + nextCheckerToMove + ': ')
            self.addMove( col, nextCheckerToMove )

            # check if the game is over
            if self.winsFor( nextCheckerToMove ):
                print self
                print '\n' + nextCheckerToMove + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a draw.\n\n'
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print 'Come back soon 4 more!'

    def playGame(self, px, po):
        """it calls on the nextMove method in px and po, which will be objects of type Player in order to play a game.
           This method is the heart of the Player class!you should handle the case in which either px or po is the
           string 'human' instead of an object of type Player. In this
           'human' case, the playGame method should simply puase and
           ask the user to input the next column to move for that
           player, with error-checking just as in hostGame.
        """
        nextCheckerToMove = 'X'
        
        while True:
            # print the board
            print self

            # get the next move from the human player...
            col = 0
            if px == 'human':
                while not self.allowsMove( col ):
                    col = input('Next col for ' + 'X' + ': ')
            else:
                col = px.nextMove( self )
                print col
            self.addMove( col, 'X' )
            if self.winsFor( 'X' ):
                print self
                print '\n' + "X" + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a draw.\n\n'
                break
            
            if po == 'human':
                while not self.allowsMove( col ):
                    col = input('Next col for ' + 'O' + ': ')
            else:
                col = po.nextMove( self )
                print col
            self.addMove( col, 'O' )
            
            # check if the game is over
            if self.winsFor( 'O' ):
                print self
                print '\n' + "O" + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a draw.\n\n'
                break
            


        print 'Come back soon 4 more!'
 ###################################################

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor
            string, either 'LEFT', 'RIGHT', or 'RANDOM'
        """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    def oppCh(self):
        """should return the other kind of checker or playing piece,
           i.e., the piece being played by self's opponent. In particular,
           if self is playing 'X', this method returns 'O'
        """
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'
        else:
            return 'Error in self.ox'
    def scoreBoard(self, b):
        """should return a single float value representing the score of the
           input b, which you may assume will be an object of type Board.
           This should return 100.0 if the board b is a win for self. It should
           return 50.0 if it is neither a win nor a loss for self, and it should
           return 0.0 if it is a loss for self (i.e., the opponent won).
        """
        if b.winsFor( self.ox ) == True:
            return 100.0
        elif b.winsFor( self.oppCh()) == True:
            return 0.0
        else:
            return 50.0
        
    def tiebreakMove(self, scores):
        """this method takes in scores,If there is only one highest score in that
           scores list, this method should return its COLUMN number,
           If there is more than one highest score because of a tie, this
           method should return the COLUMN number of the highest score
           appropriate to the player's tiebreaking type.
        """
    
        L = [i for i in range(len(scores))if scores[i] == max(scores)]
        if len(L) == 1:
            return L[0]
        elif len(L) != 1:
            if self.tbt == 'RIGHT':
                return L[-1]
            elif self.tbt == 'LEFT':
                return L[0]
            elif self.tbt == 'RANDOM':
                bagel = random.choice(L)
                return bagel
    def scoresFor(self, b):
        """ Its job is to return
           a list of scores, with the cth score representing the "goodness"
           of the input board after the player moves to column c.
        """
        scores = [50.0]*b.width
        for col in range(b.width):
            if b.allowsMove(col) == False:
                scores[col] = -1.0
            elif b.winsFor(self.ox) == True:
                scores[col] = 100.0
            elif b.winsFor(self.oppCh()) == True:
                scores[col]=0.0
            if self.ply == 0 and col == b.width:
                return scores
            elif self.ply > 0 and b.allowsMove(col) != False:
                b.addMove2(col, self.ox)
                opp  = Player(self.oppCh(), self.tbt, self.ply-1)
                badL = opp.scoresFor( b )
                if 100.0 in badL:
                    scores[col] = 0.0
                elif 0.0 in badL:
                    scores[col] = 100.0
                else:
                    scores[col] = 50.0
                b.delMove(col)
        return scores

    def nextMove(self, b):
        """takes in b, an object of type Board and returns an integer --
           namely, the column number that the calling object (of class
           Player) chooses to move to.
        """
        chips = self.scoresFor(b)
        move = self.tiebreakMove(chips)
        return(move)
    
    
        
                
                
            
            
        
        
        
        

        
