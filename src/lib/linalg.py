import math

# menghitung pemanggilan fungsi norm
func_called = 0


def norm(point1, point2):
    """
    mengembalikan jarak euclidean 
    dari point1 dan point2
    """
    global func_called
    func_called += 1

    norm = 0
    for i in range(point1.dimension):
        norm += math.pow(point1.get(i) - point2.get(i), 2)

    return math.sqrt(norm)
