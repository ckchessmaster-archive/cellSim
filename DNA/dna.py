# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class DNABase(ABC):
    @abstractmethod
    def buildCell(self, cell):
        pass