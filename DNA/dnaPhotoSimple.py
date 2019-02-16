# -*- coding: utf-8 -*-

from DNA.dna import DNABase
from components.photoModule import PhotoModule

class DNAPhotoSimple(DNABase):
    def buildCell(self, cell):
        cell.components.append(PhotoModule())