import points.point as point
import lib.linalg as la


class Points:
    def __init__(self, dimension, points=[]):
        self.__dimension = dimension
        self.__points = points
        self.__point_count = 0

    # getter
    def get_points(self):
        """
            Return array of point
        """
        return self.__points

    def get_point(self, id):
        return self.__points[id]

    def get_points_within_id(self, start_id, end_id):
        return self.__points[start_id:end_id + 1]

    def get_dimension(self):
        return self.__dimension

    def get_point_count(self):
        return self.__point_count

    # setter
    def set_points(self, points):
        self.__points = points
        self.__point_count = len(points)
    

    def set_empty(self):
        self.__points = []
        self.__point_count = 0

    # other function

    def generate_random(self, point_count, constraint):
        self.set_empty()
        _points = []
        for i in range(point_count):
            _point = point.Point(self.get_dimension())
            _point.generate_random(constraint)
            _points.append(_point)
        self.set_points(_points)

        # self.sort()

    def add(self, point):
        self.__points.append(point)
        self.__point_count += 1
        
    def partition(self, axis, lowIdx, highIdx):
        #get 1-3
        pivot = self.get_point(highIdx).get(axis) #Pivot x terakhir
        i = lowIdx - 1
        for k in range(lowIdx, highIdx):
            if self.get_point(k).get(axis) <= pivot:
                i += 1
                self.__points[i], self.__points[k] = self.__points[k], self.__points[i]
        
        self.__points[i+1], self.__points[highIdx] = self.__points[highIdx], self.__points[i+1] 
        return i+1
        
    def sort(self, axis, lowId, highIdx):
        i = lowId
        j = highIdx
        if i < j:
            partitionId = self.partition(axis, lowId, highIdx)
            self.sort(axis, i, partitionId-1)
            self.sort(axis, partitionId+1, j)

    def search(self, values, axes):
        pass

    def left_points(self, value, range=-1, axis=0):
        pass

    def right_points(self, value, range=-1, axis=0):
        pass

    def pseudo_line(self, axis=0):
        pass

    def divide(self):
        pass

    def __find_closest_pair_dnc(self):
        pass

    def __find_closest_pair_bf(self):
        """
            Finding closest pair of points using brute force algorithm
        """
        _min = 99999999
        _min_id = [-1, -1]
        for i in range(self.__point_count):
            for j in range(i + 1, self.__point_count):
                _norm = la.norm(self.get_point(i), self.get_point(j))
                if (_norm < _min):
                    _min = _norm
                    _min_id = [i, j]

        return _min, self.get_point(_min_id[0]), self.get_point(_min_id[1])

    def find_closest_pair(self, kind="dnc"):
        if kind == "bf":
            return self.__find_closest_pair_bf()
        pass

    def view(self):
        for i in range(self.__point_count):
            print(self.get_point(i).coordinate)
