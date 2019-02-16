# -*- coding: utf-8 -*-

from DNA.dna import DNABase
from components.photoModule import PhotoModule
from components.binaryFissionBehaviour import BinaryFissionBehaviour

class DNAPhotoSimple(DNABase):
    def buildCell(self, cell):
        cell.components.append(PhotoModule(cell))
        cell.components.append(BinaryFissionBehaviour(cell, 500))