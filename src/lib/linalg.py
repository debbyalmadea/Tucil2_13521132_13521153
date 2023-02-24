import points.point as p
import math


def norm(point1, point2):
    _norm = 0
    for i in range(point1.dimension):
        _norm += math.pow(point1.get(i) - point2.get(i), 2)

    return math.sqrt(_norm)
