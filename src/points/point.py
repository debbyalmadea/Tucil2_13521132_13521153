class Point:
    def __init__(self, dimension, coordinate):
        self.dimension = dimension
        self.coordinate = coordinate

    def get(self, axis):
        return self.coordinate[axis]

    def set(self, axis, value):
        self.coordinate[axis] = value

    pass
