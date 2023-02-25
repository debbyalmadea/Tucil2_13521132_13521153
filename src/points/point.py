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
            self.set(i, random.uniform(-constraint, constraint))

    def is_diff_within_distance(self, other, distance):
        for i in range(self.dimension):
            if abs(self.get(i) - other.get(i)) > distance:
                return False

        return True
