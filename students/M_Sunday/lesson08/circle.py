#!/usr/bin/python
from math import pi


class Circle(object):

    @staticmethod
    def entry_check(the__radius):
        if isinstance(the__radius, (str, list, tuple, dict)):
            raise TypeError("Radius entry must be a single, positive, and "
                            "non-string value")
        else:
            if the__radius < 0:
                raise ValueError("Radius must be greater than 0")
            else:
                return the__radius

    def __init__(self, the_radius):
        self._radius = self.entry_check(the_radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, the_radius):
        self._radius = self.entry_check(the_radius)

    @property
    def diameter(self):
        return self._radius * 2.0

    @diameter.setter
    def diameter(self, diam):
        self._radius = diam / 2.0

    @property
    def area(self):
        return pi * self._radius**2

    @classmethod
    def from_diameter(cls, dia):
        return cls(dia / 2.0)
