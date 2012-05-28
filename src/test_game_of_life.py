'''
Created on May 14, 2012

@author: MUNEER
'''
import unittest
from game_of_life import LifeGrid

class Test(unittest.TestCase):

    def setUp(self):
        '''sets up few initial test grids'''
        self.static_grid = [
                       [True,True],
                       [True,True]
                       ]
        
        self.oscillator_grid = [
                           [False, False, False],
                           [True,True,True],
                           [False,False,False]
                           ]
        
        self.boat_grid = [
                     [True, True, False],
                     [True, False, True],
                     [False, True, False],
                     ]
        
        self.toad_grid = [
                     [False, True, True, True],
                     [True, True, True, False],
                     ]

        self.mygrid = LifeGrid()

    def tearDown(self):
        '''deletes the test grids'''
        del(self.static_grid)
        del(self.oscillator_grid)
        del(self.boat_grid)
        del(self.toad_grid)


    def testEnvelope(self):
        '''test for LifeGrid.envelope method'''
        enveloped_static_grid =  self.mygrid.envelope(self.static_grid)
        expected_result = [
                         [False, False, False, False],
                         [False, True, True, False],
                         [False, True, True, False],
                         [False, False, False, False],
                         ]
        assert enveloped_static_grid == expected_result
        
    def testDeEnvelope(self):
        '''test for LifeGrid.de_envelope method'''
        sample_input_grid = [
                         [False, False, False, False],
                         [False, True, True, False],
                         [False, True, True, False],
                         [False, False, False, False],
                         ]
        sample_output_grid = [
                              [True, True],
                              [True, True]
                              ]
        de_enveloped_static_grid =  self.mygrid.de_envelope(sample_input_grid)
        assert de_enveloped_static_grid == sample_output_grid

    def testStrip(self):
        '''test for LifeGrid.strip_grid method'''
        
        sample_input_grid = [
                         [False, False, False, False],
                         [False, True, True, False],
                         [False, True, True, False],
                         [False, False, False, False],
                         ]
        sample_output_grid = [
                              [True, True],
                              [True, True]
                              ]
        stripped_static_grid =  self.mygrid.strip_grid(sample_input_grid)
        assert stripped_static_grid == sample_output_grid
        
    def testNextState(self):
        '''test for LifeGrid.get_next_state method'''
        sample_grid = self.oscillator_grid
        output_grid = self.mygrid.get_next_state(sample_grid)
        expected_output = [
                           [False, True, False],
                           [False,True,False],
                           [False,True,False]
                           ]
        assert output_grid == expected_output
        
    def testGetLiveNeighbours(self):
        '''test for LifeGrid.strip_grid method'''
        sample_grid = self.oscillator_grid
        output_grid = self.mygrid.get_live_neighbours((1,1), sample_grid)
        expected_output = [
                           [1,0],        [1,2],
                           ]
        assert output_grid == expected_output
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()