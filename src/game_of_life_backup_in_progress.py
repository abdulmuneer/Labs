'''
Created on May 14, 2012

@author: MUNEER
'''
from copy import copy
class Cell():
    '''
    defines a cell object with its cordinates and state
    '''
    def __init__(self,x,y, is_alive=False):
        self.cordinates = (x,y)
        self.is_alive = is_alive

    def toggle_state(self):
        self.is_alive = not self.is_alive

class LifeGrid():
    def __init__(self):
        self.grid = []
    def get_grid(self):
        #print "inside get_grid"
        state = {'-':False, 'X':True}
        row_entry, row = raw_input(), 0
        while(row_entry):
            try:
                cell_rows = [Cell(row, column, state[cells]) for column, cells
                             in enumerate(row_entry)]
            except:
                print "Invalid input"
                return None
            self.grid.append(cell_rows)
            row += 1
            row_entry = raw_input()
        #return self.grid
            
            
    def get_live_neighbours(self, cordinates):
        #print "inside get_live_neighbours"
        #we assume this grid is surrounded by infinite dead cells
        neighbor_positions = [(-1,-1),(-1,0),(-1,1),
                              (0,-1),(0,1),
                              (1,-1),(1,0),(1,1)
                              ]
        neighbours = [ [sum(a) for a in zip(cordinates,cells)] 
                      for cells in neighbor_positions ]
        #print "neighbours of (%s,%s): "%cordinates,neighbours
        live_neighbours = [cells for cells in neighbours if 
                            self.is_valid(cells) and self.is_alive(cells)]
        #print "live_neighbours of (%s,%s)"%cordinates,live_neighbours
        return live_neighbours
    
    def get_next_state(self):
        #print "inside get_next_state"
        new_grid = []
        for rows in self.grid:
            new_row = []
            for cells in rows:
                new_cells = copy(cells)
                num_live_neighbours = len(
                                self.get_live_neighbours(cells.cordinates))
                
                if num_live_neighbours == 3:
                    new_cells.is_alive = True
                elif num_live_neighbours == 2:
                    new_cells.is_alive = cells.is_alive
                else:
                    new_cells.is_alive = False
                new_row.append(new_cells)
            new_grid.append(new_row)
        self.grid = new_grid
        #self.new_grid = new_grid
        return new_grid
                    
                    
                        
    def print_grid(self):
        #print "inside print_grid"
        out = {True:'X', False:'-'}
        for rows in self.grid:
            print '\n'
            for cells in rows:
                print out[cells.is_alive],
                   
        
        
    def is_valid(self, cell):
        #print "inside is_valid"
        return 0<=cell[0]<len(self.grid[0]) and 0<=cell[1]<len(self.grid)
    
    def is_alive(self,cells):
        #print "inside is_alive"
        return self.grid[cells[0]][cells[1]].is_alive
    
    def __get_cell(self, grid, cordinate):
        #print "inside __get_cell"
        return grid[cordinate[0]][cordinate[1]]
    
    
if __name__ == '__main__':
    
    while True:
        mygrid = LifeGrid()
        print "\nEnter next grid:\n"
        mygrid.get_grid()
        mygrid.get_next_state()
        mygrid.print_grid()
        

                    