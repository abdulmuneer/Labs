'''
Created on Mar 26, 2012

@author: abdul
'''

import time
from pprint import pprint

def can_you_split(choco_matrix,choco_sizes):
    num_of_pieces = len(choco_sizes)
    num_of_cuts = num_of_pieces - 1
    pprint (blocks_after_a_cut(choco_matrix))
    new_blocks = []
    #for each_block in new_block_sets:
        #[([1, 3], [3, 3]), ([1, 4], [2, 4]), ([2, 3], [2, 3])]
        #([1, 3], [3, 3])
   # new_blocks.append(object)
    
    
def blocks_after_a_cut(block_size):
    '''
    >>> blocks_after_a_cut((3,4))
    (((3,1),(3,3)), ((3,2),(3,2)), ((1,4),(2,4)) )
    '''
    rows,columns = block_size
    new_pieces = []
    if [rows, columns] == [1,1]:
        return None
    for i in range(1,(columns/2)+1 ):
        new_pieces.append([sorted((rows,i)), sorted((rows,columns-i)) ])
    for i in range(1,(rows/2)+1):
        new_pieces.append([sorted((i,columns)), sorted((rows-i,columns)) ])
    return sorted(new_pieces)
    #print size_combinations(new_pieces)
    
def size_combinations(piece_combinations):
    sizes = []
    for each_combination in piece_combinations:
        #([2, 3], [2, 3]) - a typical each_combination
        sizes.append(sorted([block[0]*block[1] for block in each_combination]))
    return sorted(sizes)

def main():
    '''
    try:
        number_of_pieces = int(raw_input("Enter the number of pieces"))
    except:
        print "invalid input.."
        return quit_program()
    else:
        if number_of_pieces == 0:
            return quit_program()
    '''
    '''
    try:
        matrix = raw_input("Enter the chocolate matrix separated by space").split()
        choco_matrix = [int(x) for x in matrix]
    except:
        print "Invalid input"
        return quit_program()
    else:
        if choco_matrix[0] == 0:
            return quit_program()
    
    try:
        sizes = raw_input("Enter the size of the chocolate pieces separated by space").split()
        choco_sizes = [int(x) for x in matrix]
    except:
        print "Invalid input"
        return quit_program()
    else:
        if choco_sizes[0] == 0:
            return quit_program()
    '''
    choco_matrix = (3,4)
    choco_sizes = (6,6)
    can_you_split(choco_matrix,choco_sizes)

def quit_program():
    print "quitting..."
    time.sleep(3)
    return 0
if __name__ == '__main__':
    main()