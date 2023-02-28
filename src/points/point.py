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
        """
        menghasilkan koordinat secara random (double)
        """
        for i in range(self.dimension):
            self.set(i, random.uniform(-constraint, constraint))

    def is_diff_within_distance(self, other, distance):
        """
        return true jika selisih self dan other
        pada setiap sumbu kurang dari sama dengan distance
        """
        for i in range(self.dimension):
            if abs(self.get(i) - other.get(i)) > distance:
                return False

        return True

    def greater_than_eq(self, other, axis=0):
        """
        return true jika self lebih besar sama dengan other
        dengan prioritas utama sumbu axis
        """
        if self.get(axis) > other.get(axis):
            return True
        elif self.get(axis) < other.get(axis):
            return False

        for i in range(self.dimension):
            if axis == i:
                continue
            if self.get(i) > other.get(i):
                return True
            elif self.get(i) < other.get(i):
                return False

        return True

    def less_than_eq(self, other, axis=0):
        """
        return true jika self lebih kecil sama dengan other
        dengan prioritas utama sumbu axis
        """
        if self.get(axis) < other.get(axis):
            return True
        elif self.get(axis) > other.get(axis):
            return False

        for i in range(self.dimension):
            if axis == i:
                continue
            if self.get(i) < other.get(i):
                return True
            elif self.get(i) > other.get(i):
                return False

        return True
    
    def is_equal(self, other):
        for i in range(self.dimension):
            if self.get(i) != other.get(i):
                return False
        
        return True
