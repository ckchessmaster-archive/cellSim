# -*- coding: utf-8 -*-

from DNA.dnaPhotoSimple import DNAPhotoSimple as DNA

class Cell:
    def __init__(self, x, y, energy, world):
        self.location = {'x':x, 'y':y}
        self.world = world
        self.energy = energy
        self.dna = DNA()
        self.components = []
        self.dna.buildCell(self)
        
    #end __init__()
    
    def tick(self):
        if self.energy <= 0:
            return 1

        for component in self.components:
            component.tick()
        
        self.energy -= 1
        return 0
    #end tick()
#End Cell