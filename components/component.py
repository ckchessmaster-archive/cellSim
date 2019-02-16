# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def tick(self):
        pass