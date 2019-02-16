# -*- coding: utf-8 -*-

from graphics import *

win = GraphWin('CellSim', 500, 500) 

def init():
       print('Initializing renderer...')
    
def end():
    win.close()
    
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    
def render(world):
    clear(win)
    
    for cell in world.cells:
        pt = Point(cell.location['x'], cell.location['y'])
        cir = Circle(pt, 5)
        cir.setOutline('black')
        cir.setFill('red')
        cir.draw(win)
    
    
'''Example:
win = GraphWin()
pt = Point(100, 50)
pt.draw(win)
cir = Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')
line = Line(pt, Point(150, 100))
line.draw(win)
rect = Rectangle(Point(20, 10), pt)
rect.draw(win)
line.move(10, 40)
win.close()'''