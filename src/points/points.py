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
        """
            return array of points from start_id to end_id (inclusive)
        """
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

    def __search_fo(self, low, high, value, axis):
        """
            prereq: points are sorted ascending by axis

            return index of first occurence of value in axis using binary search.
        """

        if (high >= low):
            mid = low + (high - low) // 2
            if self.get_point(mid).get(axis) == value:
                if mid == 0 or self.get_point(mid - 1).get(axis) != value:
                    return mid
                else:
                    return self.__search_fo(low, high - 1, value, axis)
            else:
                if value < self.get_point(mid).get(axis):
                    return self.__search_fo(low, mid - 1, value, axis)
                else:
                    return self.__search_fo(mid + 1, high, value, axis)
        return low

    def __search_lo(self, low, high, value, axis):
        """
            prereq: points are sorted ascending by axis

            return index of last occurence of value in axis using binary search.
        """
        if (high >= low):
            mid = low + (high - low) // 2
            if self.get_point(mid).get(axis) == value:
                if mid == self.get_point_count() - 1 or self.get_point(mid + 1).get(axis) != value:
                    return mid
                else:
                    return self.__search_lo(low, high + 1, value, axis)
            else:
                if value < self.get_point(mid).get(axis):
                    return self.__search_lo(low, mid - 1, value, axis)
                else:
                    return self.__search_lo(mid + 1, high, value, axis)

        return high

    def search(self, value, kind="first", axis=0):
        """
            prereq: points are sorted ascending by axis
        """
        if kind == "first":
            return self.__search_fo(0, self.get_point_count() - 1, value, axis)
        else:
            return self.__search_lo(0, self.get_point_count() - 1, value, axis)

    def divide(self):
        """
            return two Points: first half of array of point and last half of array of point
        """
        left = Points(self.__dimension)
        right = Points(self.__dimension)
        left.set_points(
            self.get_points_within_id(0, self.__point_count // 2 - 1))
        right.set_points(
            self.get_points_within_id(self.__point_count // 2, self.__point_count - 1))
        return left, right

    def __find_closest_pair_with(self, other, distance, axis=0):
        pass

    def __find_closest_pair_dnc(self):
        """
            finding closest pair of points using divide and conquer algorithm
        """
        if self.get_point_count() == 2:
            return la.norm(self.get_point(0), self.get_point(1)), self.get_point(0), self.get_point(1)
        else:
            _min = 0
            _min_p1 = point.Point(self.__dimension)
            _min_p2 = point.Point(self.__dimension)

            left, right = self.divide()
            left_min, left_p1, left_p2 = left.__find_closest_pair_dnc()
            right_min, right_p1, right_p2 = right.__find_closest_pair_dnc()

            left_closest = left.get_point(left.get_point_count() - 1)
            right_closest = right.get_point(0)
            pseudo_line = left_closest.get_value_between(right_closest)

            if (left_min < right_min):
                _min = left_min
                _min_p1 = left_p1
                _min_p2 = left_p2
            else:
                _min = right_min
                _min_p1 = right_p1
                _min_p2 = right_p2

            # closest pair in grey area
            gfl_id = left.search(pseudo_line - _min, kind="first")
            gfr_id = right.search(pseudo_line - _min, kind="last")

            grey_l = Points(self.__dimension)
            grey_l.set_points(left.get_points_within_id(
                gfl_id, left.get_point_count() - 1))

            grey_r = Points(self.__dimension)
            grey_r.set_points(right.get_points_within_id(
                gfr_id, right.get_point_count() - 1))

            grey_l.__find_closest_pair_with(grey_r, _min)

            # print("left")
            # left.view()
            # print("right")
            # right.view()

            # print(pseudo_line)
            return _min, _min_p1, _min_p2

    def __find_closest_pair_bf(self):
        """
            finding closest pair of points using brute force algorithm
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
        """
            finding closest pair of points. parameter kind is the algorithm used. 
            default is "dnc" for divide and conquer, another one is "bf" for brute force
        """
        if kind == "bf":
            return self.__find_closest_pair_bf()
        elif kind == "dnc":
            return self.__find_closest_pair_dnc()

    def view(self):
        for i in range(self.__point_count):
            print(self.get_point(i).coordinate)
