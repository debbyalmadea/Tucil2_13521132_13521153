import random


class Point:
    def __init__(self, dimension, coordinate=[]):
        self.dimension = dimension
        if (len(coordinate) == 0):
            coordinate = [0 for i in range(dimension)]
        self.coordinate = coordinate

    def get(self, axis):
        return self.coordinate[axis]

    def set(self, axis, value):
        self.coordinate[axis] = value

    def generate_random(self, constraint):
        for i in range(self.dimension):
            self.set(i, random.randint(-constraint, constraint))

    def get_value_between(self, other, axis=0):
        return (self.get(axis) - other.get(axis)) / 2
