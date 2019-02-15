# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:40:47 2019

@author: chris kingdon
"""

import time
from world import World

def main():
    world = World()
    
    while True:
        start = time.time()
        world.tick()
        end = time.time()
        diff = end - start
        
        # Force each tick to take no less than 1/20th of a second
        if diff < 0.05:
            time.sleep(0.05 - diff)
            
    # End while True
# end main()
          
main()