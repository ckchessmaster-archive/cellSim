# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:30:41 2019

@author: ckche
"""

from components.component import Component
import random

class BinaryFissionBehaviour(Component):
    def __init__(self, cell, energyThreshold):
        self.cell = cell
        self.energyThreshold = energyThreshold
        
    def tick(self):
        if self.canSplit():
            self.split()
            
    def canSplit(self):
        self.splitLocation = self.findSplitLocation()
        
        if (self.cell.energy >= self.energyThreshold 
            and (self.cell.location['x'] is not self.splitLocation['x'] or self.cell.location['y'] is not self.splitLocation['y'])):
            return True
        else:
            return False
    #end canSplit
            
    def findSplitLocation(self):
        # This needs to be refactored at some point
        potentialLocations = [
                {'x':(self.cell.location['x'] + 10), 'y':self.cell.location['y']},
                {'x':(self.cell.location['x'] - 10), 'y':self.cell.location['y']},
                {'x':self.cell.location['x'], 'y':(self.cell.location['y'] + 10)},
                {'x':self.cell.location['x'], 'y':(self.cell.location['y'] - 10)}]
        
        usedLocations = []
        for cell in self.cell.world.cells:
            usedLocations.append(cell.location)
        
        possibleLocations = []
        for plocation in potentialLocations:
            if plocation not in usedLocations:
                possibleLocations.append(plocation)
                
        if len(possibleLocations) > 0:
            return possibleLocations[0]
        
        # return our location to signify there is no spawn place
        return self.cell.location
        
    def split(self):
        self.cell.world.createNewCell(self.splitLocation, self.cell.energy / 2)        
        self.cell.energy = self.cell.energy / 2
    #end split()
#end BinaryFissionBehaviour
        