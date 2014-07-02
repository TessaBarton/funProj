class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0,W):
            s += ' ' + `col`
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """for dropping a checker into the board: the first input
           col represents the index of the column to which the checker
           will be added; the second input ox will be a 1-character string
           representing the checker to add to the board.
        """
        H = self.height
        for row in range(0,H):   
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox
       
                
            
    def clear( self ):
        """Not much to say about clear( self ).
        """
        W = self.width
        H = self.height
        for row in range(0,H):
            for col in range(0,W):
                self.data[row][col] = ' '

    def allowsMove(self, c):
        """This method should return True if the calling object (of type Board)
           does allow a move into column c. It returns False if column c is not
           a legal column number for the calling object.
        """
        W = self.width
        H = self.height
        D = self.data
        if c in range(W) and self.data[0][c] == ' ':
            return True
        else:
            return False
    def isFull(self):
        """his method should return True if the calling object (of type Board)
           is completely full of checkers.
        """
        H = self.height
        W = self.width
        D = self.data
        for col in range(0,W):
            if self.allowsMove(col) == True:
                return False
        return True
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self, c):
        """It should remove the top checker from the column c
        """
        H = self.height
        for row in range(0,H):   
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                return
    def winsFor(self, ox):
        """input ox is a 1-character checker: either 'X' or 'O'.
           It should return True if there are four checkers of
           type ox in a row on the board.
        """
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
        for col in range(0,W):
            for row in range(0,H-3):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True
        for row in range(0,H-3):
            for col in range(0, W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    return True
        for row in range(0,H-3):
            for col in range(W-3,W):
                if D[row][col] == ox and \
                   D[row+1][col-1] == ox and \
                   D[row+2][col-2] == ox and \
                   D[row+3][col-3] == ox:
                    return True
            
        # how do I get him to return false?

    def hostGame(self):
        """It should host a game of connect four, using the methods
           listed above to do so  It should ask the user (with the
           input function)
        """
        print "Welcome to connect four!"
        while True:
            print self
            print " X, Your turn! "
            x_col = input( " \nPlace a checker " )
            while self.allowsMove( x_col ) == False:
                x_col = input("Choose a column: ")
            self.addMove(x_col, 'X')
            if self.winsFor( 'X' ) == True:
                print 'X Wins!'
                print self
                break
            print self
            print " O, Your turn! "
            o_col = input( " \nPlace a checker " )
            while self.allowsMove( o_col ) == False:
                o_col = input("Choose a column: ")
            self.addMove(o_col, 'O')
            if self.winsFor( 'O' ) == True:
                print "O Wins!"
                print self
                break
            if self.isFull() == True:
                print " TIE!"
                print self
                break
            
            
                   
        
        
            
                
        
