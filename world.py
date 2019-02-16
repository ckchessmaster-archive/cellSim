# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:58:30 2019

@author: ckche
"""

from cell import Cell

class World:
    def __init__(self, maxWorldSize = 100):
        if maxWorldSize <= 0:
            raise ValueError("Max world size must be greater than 0!")
        
        self.maxWorldSize = maxWorldSize
        
        # Create the first cell and initialize cell list
        self.cells = [Cell(100,100, 10000000, self)]
        
    # End __init__()
        
        
    def tick(self):
        for i, cell in enumerate(self.cells):
            result = cell.tick()
            if result == 1:
                del self.cells[i]
        #end for cell in cells
    # End tick()
# End World