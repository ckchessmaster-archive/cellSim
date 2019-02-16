# -*- coding: utf-8 -*-

from components.component import Component

class PhotoModule(Component):
    def __init__(self, cell):
        self.cell = cell
        
    def tick(self):
        sunLevel = self.cell.world.getSunLevelAtCoordinates(self.cell.location)
        self.cell.energy += (sunLevel / 100)
        