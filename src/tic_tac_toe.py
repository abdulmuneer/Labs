
'''
Created on May 27, 2012

@author: MUNEER
'''

#global variables
X = 'X'
O = 'O'


def detect_winner(position):
    '''
    returns the winner of the game.
    If the game is a draw, function returns None
    '''
    #three cells should be identical in rows, columns or diagonals \
    #in a 3x3 matrix
    #the input 'position' is a 2d matrix of 3x3 size.
    
    #extracts column-wise grouping
    column1, column2, column3 = [], [], []
    for i in range(3):
        column1.append(position[i][0])
        column2.append(position[i][1])
        column3.append(position[i][2])
    
    diagonals = (
                 (position[0][0], position[1][1], position[2][2]),
                 (position[2][0], position[1][1], position[0][2])
                 )
    directions = {
                    #collection of adjacent cells of particular direction
                    'horizontal' : position ,
                    'vertical' : (column1, column2, column3),
                    'diagonal' : diagonals
                    }
    for cases in directions.values():
        for positions in cases:
            if len(set(positions)) == 1:
                return positions[0]
    return None #Game is a Draw.§

def detect_starter(position):
    '''
    identifies who started the game.
    '''
    #the starter would have played odd number of times\
    # when the game is finished
    count = {X : 0,
             O : 0
             }
    for rows in position:
        for players in rows:
            count[players] += 1
    return X if count[X]%2 else 'O'
    
def clean_input(position):
    '''
    verifies if the input is valid or not w.r.t. tic-tac-toe
    '''
    for rows in position:
        if len(rows) != 3:
            return False
        if not set(rows).issubset(set([X,O])):
            return False
    return True
            

def main():
    '''
    gets the input (final position) from user.
    prints who started the game and also the game result.
    '''
    position = []
    print "Enter the game position. Enter each row in a new line"
    print "e.g: "
    print "XOX"
    print "OXO"
    print "OXO\n"
    for i in range(3):
        position.append(list(raw_input().upper()))
    #validate input
    if not clean_input(position):
        print "Invalid input.."
        return
    winner = detect_winner(position)
    starter = detect_starter(position)
    print 'Player',starter,'started the game.',
    if winner:
        print 'Player',winner,'has won.'
    else:
        print 'The game is a draw.'
    
    
if __name__ == '__main__':
    main()
