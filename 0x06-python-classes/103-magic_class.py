#!/usr/bin/python3
"""Python class that imitates a Python bytecode"""
import math
"""imported module"""


class MagicClass:
    """Created class"""
    def __init__(self, radius=0):
        """Initialised object class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise (TypeError("radius must be a number"))
        self._MagicClass__radius = radius

    def area(self):
        """Retrieves the area"""
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self):
        """Retrieves the circumference"""
        return (2 * math.pi * self._MagicClass__radius)

if __name__ == "__main__":
    import dis
    dis.dis(MagicClass)
