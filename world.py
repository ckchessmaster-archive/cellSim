# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:58:30 2019

@author: ckche
"""

from cell import Cell
import numpy as np

class World:
    def __init__(self, maxWorldSize = 100):
        if maxWorldSize <= 0:
            raise ValueError("Max world size must be greater than 0!")
        
        self.maxWorldSize = maxWorldSize
        
        # Create the first cell and initialize cell list
        self.cells = np.array([Cell(0,0)])
        
    # End __init__()
        
        
    def tick(self):
        for cell in self.cells:
            cell.tick()
    # End tick()
# End World