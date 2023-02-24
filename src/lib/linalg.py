import points.point as p
import math

func_called = 0


def norm(point1, point2):
    global func_called
    func_called += 1

    _norm = 0
    for i in range(point1.dimension):
        _norm += math.pow(point1.get(i) - point2.get(i), 2)

    return math.sqrt(_norm)
