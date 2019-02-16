# -*- coding: utf-8 -*-

from DNA.dnaPhotoSimple import DNAPhotoSimple as DNA
from graphics import Point
from graphics import Circle
from graphics import color_rgb

class Cell:
    def __init__(self, x, y, energy, world):
        self.location = {'x':x, 'y':y}
        self.world = world
        self.energy = energy
        self.dna = DNA()
        self.components = []
        self.dna.buildCell(self)
        
        # Draw ourself to the screen
        pt = Point(self.location['x'], self.location['y'])
        cir = Circle(pt, 5)
        cir.setOutline('black')
        
        # Set the color based on remaining energy
        colorValue = 255
        if self.energy <= (2550):
            colorValue = round(self.energy / 10)
        
        cir.setFill(color_rgb(colorValue, 0, 0))
        cir.draw(self.world.window)
        self.sprite = cir
    #end __init__()
    
    def tick(self):
        if self.energy <= 0:
            self.die()
            return 1

        for component in self.components:
            component.tick()
        
        self.energy -= 1
        
        # Set the color based on remaining energy
        colorValue = 255
        if self.energy <= (2550):
            colorValue = round(self.energy / 10)
        self.sprite.setFill(color_rgb(colorValue, 0, 0))
        
        return 0
    #end tick()
    
    def die(self):
        self.sprite.undraw()
#End Cell