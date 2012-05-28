'''
Created on May 14, 2012

@author: MUNEER
'''
"""
class Cell():
    '''
    defines a cell object with its cordinates and state
    '''
    def __init__(self, is_alive=False):
        self.is_alive = is_alive
    def toggle_state(self):
        self.is_alive = not self.is_alive
"""

class LifeGrid():
    '''
    Defines a grid of cells with its state (True or False)
    Defines methods to get next state and print the grid
    '''
    def __init__(self):
        self.grid = []
        
    def get_grid(self):
        #print "inside get_grid"
        state = {'-':False, 'X':True, 'x':True}
        row_entry, row = raw_input(), 0
        row_length = None #to compare each entry to previous ones
        
        #keep taking input till user enters a blank line
        while(row_entry):
            try:
                cell_rows = [state[cells] for cells in row_entry]
            except:
                print "Invalid input"
                return None
            
            #this will help validate all rows are of same length.
            if not row_length:
                row_length = len(cell_rows)
            if row_length != len(cell_rows):
                print "Invalid entry"
                return None
            
            self.grid.append(cell_rows)
            row_entry, row = raw_input(), row+1
            
        return self.grid
    
    def get_next_state(self,grid=None):
        '''
        Returns the next state of the input grid
        '''
        my_grid = grid or self.grid
        if not my_grid:
            return None
        
        #expand the grid by enveloping empty cells on all four borders
        #apply next state calculation on this new grid
        #this is done to accommodate growing and moving patterns
        enveloped_grid = self.envelope(my_grid)
        
        #create a new grid to store the next state
        new_grid = [[False for j in enveloped_grid[0]] for i in enveloped_grid]
        for row_count, row_contents  in enumerate(enveloped_grid):
            for col_count, cells in enumerate(row_contents):
                
                cordinates = (row_count,col_count)
                num_live_neighbours = len(
                        self.get_live_neighbours(cordinates,enveloped_grid))
                if num_live_neighbours == 3:
                    new_cell = True
                elif num_live_neighbours == 2 and cells:
                    new_cell = True
                else:
                    new_cell = False
                new_grid[row_count][col_count] = new_cell
                
        #remove envelop if there is no new cell in any border
        self.grid = self.de_envelope(new_grid)
        return self.grid
            
    def get_live_neighbours(self, cordinates, grid):
        '''returns the cordinates of all live neighbors'''
        neighbor_positions = [(-1,-1),(-1,0),(-1,1),
                              (0,-1),       (0,1),
                              (1,-1),(1,0),(1,1)
                              ]
        neighbours = [ [sum(a) for a in zip(cordinates,distance)] 
                      for distance in neighbor_positions ]
        
        live_neighbours = [cells for cells in neighbours if 
                    self.is_valid(cells,grid) and self.is_alive(cells,grid)]
        return live_neighbours
    
    def envelope(self, grid):
        '''
        Adds empty cells on all four borders of the current grid.
        This is done to allow growing and moving patterns
        '''
        if not grid:
            return None
        rows, columns = len(grid), len(grid[0])
        new_grid = [[False for x in range(columns+2)]]
        for rows in grid:
            new_rows = [False]+ rows+[False]
            new_grid.append(new_rows)
        new_grid.append([False for x in range(columns+2)])
        return new_grid
    
    def de_envelope(self, grid):
        '''
        Removes the envelop created by self.envelop method \
        if they are not occupied
        '''
        if not grid:
            return None
        
        #removing top
        if not any([cells for cells in grid[0]]):
            del grid[0]
        
        #removing bottom
        if not any([cells for cells in grid[-1]]):
            del grid[-1]
        
        #removing left column
        if not any([rows[0] for rows in grid]):
            for rows in grid:
                del rows[0]
                
        #removing right column
        if not any([rows[-1] for rows in grid]):
            for rows in grid:
                rows.pop()
        
        return grid
    
    def strip_grid(self,grid):
        '''
        strips the grid to remove all empty borders.
        '''
        if not grid:
            return None
        #stripping top and bottom rows:
        while not any([cells for cells in grid[0]]):
            del(grid[0])
        while not any([cells for cells in grid[-1]]):
            del(grid[-1])
        #stripping left and right columns 
        while not any(rows[0] for rows in grid):
            for rows in grid:
                del(rows[0])
        while not any(rows[-1] for rows in grid):
            for rows in grid:
                del(rows[-1]) 
        return grid
    
    def is_valid(self,cordinate,grid):
        '''
        checks if a given cordinate is a valid cell inside the grid
        yatin, mishra, rohit.
        '''
        #print "inside is_valid"
        return 0<=cordinate[0]<len(grid) and \
            0<=cordinate[1]<len(grid[0])
    
    def is_alive(self, cordinates, grid):
        '''
        checks if a given cordinate is a live cell
        '''
        return grid[cordinates[0]][cordinates[1]]
    
    def __get_cell(self,cordinate,grid):
        if not grid:
            return
        #print "inside __get_cell"
        return grid[cordinate[0]][cordinate[1]]
    
    def print_grid(self, grid=None):
        if not grid:
            grid = self.grid
        #print "inside print_grid"
        out = {True:'X', False:'-'}
        for rows in grid:
            print '\n'
            for cells in rows:
                print out[cells],
    
if __name__ == '__main__':
    mygrid = LifeGrid()
    print "\nEnter the grid:\n"
    original_grid = mygrid.get_grid()
    while original_grid:
        mygrid.get_next_state()
        mygrid.print_grid()
        x = raw_input("\nHit Enter for the next state")
                    