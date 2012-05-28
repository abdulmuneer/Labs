'''
solves the problem listed below..
Created on May 25, 2012
@author: MUNEER

#=============================================================================
# Problem: 
# There are 100 Doors - All of them CLOSED initially.
# You do 100 iterations and visit doors as below.  
# During every visit, you toggle the status of the door  
# [If it is CLOSED, you OPEN it. If it is OPEN, you CLOSE it.] 
#  
#    Iteration 1 : Start from door number 1,
          visit each of the 100 doors and toggle status of visited door. 
#    Iteration 2 : Start from door number 2,
          visit 4, 6, 8, 10, ...100. Toggle status of visited door.
          visit 4, 6, 8, 10, 12, ...100. Toggle status of visited door. 
#    Iteration 3 : Start from door number 3,
          visit 6, 9, 12, 15, 18, ...99. Toggle status of visited door. 
#    Iteration 4 : Start from door number 4,
          visit 8, 12, 16, 20, ...100. Toggle status of visited door. 
#    ... 
#    ...
#    So on. 
# At the end of 100th iteration, print the door numbers  
# which are in OPEN state. 
#=============================================================================
'''

def open_doors(doors=100):
    '''
    returns the list of open doors.
    '''
    opened_doors = [i for i in xrange(1,doors+1) if is_door_open(i)]
    return opened_doors
    
    
def is_door_open(i):
    '''
    returns boolean to show if i-th door is open after all the operations.
    '''
    
    #NOTE: It turns out that i-th door will be visited\
    # for all numbers that are factors of i
    number_of_operations = num_factors(i)
    
    #Since initially the doors are closed, every even number of operations\
    #will keep the door closed.
    is_open = True if number_of_operations%2 else False
    return is_open 

def num_factors(num):
    '''
    returns the count of all factors of the number including 1 and itself
    '''
    count = 0
    for i in xrange(1,num+1):
        count = count+1 if not num%i else count
    return count

if __name__ == '__main__':
    print 'Open doors: ', open_doors()