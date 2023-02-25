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
        if start_id <= end_id:
            return self.__points[start_id:end_id + 1]
        else:
            return []

    def get_dimension(self):
        return self.__dimension

    def get_point_count(self):
        return self.__point_count

    # setter
    def set_points(self, points):
        """
            set points (array)
        """
        self.__points = points
        self.__point_count = len(points)

    def set_empty(self):
        """
            set points to empty
        """
        self.__points = []
        self.__point_count = 0

    # other function

    def generate_random(self, point_count, constraint):
        """
            generate random points
        """
        self.set_empty()
        _points = []
        for i in range(point_count):
            _point = point.Point(self.get_dimension())
            _point.generate_random(constraint)
            _points.append(_point)
        self.set_points(_points)

        # self.sort()

    def add(self, point):
        """
            add point to points
        """
        self.__points.append(point)
        self.__point_count += 1

    def __partition(self, lowIdx, highIdx, axis):
        """
            partition used for quick sort
        """
        # get 1-3
        pivot = self.get_point(highIdx).get(axis)  # Pivot x terakhir
        i = lowIdx - 1
        for k in range(lowIdx, highIdx):
            if self.get_point(k).get(axis) <= pivot:
                i += 1
                self.__points[i], self.__points[k] = self.__points[k], self.__points[i]

        self.__points[i+1], self.__points[highIdx] = self.__points[highIdx], self.__points[i+1]
        return i+1

    def sort(self, lowId, highIdx, axis=0):
        """
            sort points by axis using quick sort
        """
        i = lowId
        j = highIdx
        if i < j:
            partitionId = self.__partition(lowId, highIdx, axis)
            self.sort(i, partitionId-1, axis)
            self.sort(partitionId+1, j, axis)

    def __search_fo(self, low, high, value, axis):
        """
            prereq: points are sorted ascending by axis

            return index of first occurence of value in axis using binary search.
            if there is no value, return first occurence of element more than value
        """

        if (high >= low and low < self.__point_count):
            mid = low + (high - low) // 2
            if self.get_point(mid).get(axis) == value:
                if mid == 0 or self.get_point(mid - 1).get(axis) < value:
                    return mid
                else:
                    return self.__search_fo(low, high - 1, value, axis)
            else:
                if value < self.get_point(mid).get(axis):
                    return self.__search_fo(low, mid - 1, value, axis)
                else:
                    return self.__search_fo(mid + 1, high, value, axis)
        # print("===========FO NOT FOUND", low, high, "VALUE:", value)
        # self.view()

        return low

    def __search_lo(self, low, high, value, axis):
        """
            prereq: points are sorted ascending by axis

            return index of last occurence of value in axis using binary search.
            if there is no value, return last occurence of element less than value
        """
        if (high >= low and high < self.__point_count):
            mid = low + (high - low) // 2
            # print(self.__point_count, mid)
            if self.get_point(mid).get(axis) == value:
                if mid == self.get_point_count() - 1 or self.get_point(mid + 1).get(axis) > value:
                    return mid
                else:
                    return self.__search_lo(low, high + 1, value, axis)
            else:
                if value < self.get_point(mid).get(axis):
                    return self.__search_lo(low, mid - 1, value, axis)
                else:
                    return self.__search_lo(mid + 1, high, value, axis)

        # print("===========LO NOT FOUND", low, high, "VALUE:", value)
        # self.view()
        return high

    def search(self, value, kind="first", axis=0):
        """
            prereq: points are sorted ascending by axis
        """
        if kind == "first":
            return self.__search_fo(0, self.get_point_count() - 1, value, axis)
        elif kind == "last":
            return self.__search_lo(0, self.get_point_count() - 1, value, axis)

    def divide(self):
        """
            return tuple
            1. array of integer size two representing start and end index of
               the first half of array points
            2. array of integer size two representing start and end index of
               the second half of array points
        """
        # left = Points(self.__dimension)
        # right = Points(self.__dimension)
        # left.set_points(
        #     self.get_points_within_id(0, self.__point_count // 2 - 1))
        # right.set_points(
        #     self.get_points_within_id(self.__point_count // 2, self.__point_count - 1))
        left_sid = 0
        left_eid = self.__point_count // 2 - 1
        right_sid = self.__point_count // 2
        right_eid = self.__point_count - 1

        return [left_sid, left_eid], [right_sid, right_eid]

    def __find_closest_pair_grey(self, distance, left_id, right_id, axis=0):
        """
            return closest pair of point in grey area, an area +- distance
            from pseudo line from all axes
        """
        _min = distance
        min_p1 = point.Point(self.__dimension)
        min_p2 = point.Point(self.__dimension)

        left_closest = self.get_point(left_id[1])
        right_closest = self.get_point(right_id[0])
        # pseudo_line = left_closest.get(
        #     axis) + abs(left_closest.get_value_between(right_closest))

        # print("LEFT CLOSEST", left_closest.coordinate)
        # print("RIGHT CLOSEST", right_closest.coordinate)
        # print("PSEUDO LINE:", pseudo_line)

        gfl_id = self.search(
            int(right_closest.get(0) - distance), kind="first")
        # gfr_id = self.search(int(left_closest.get(0) + distance), kind="last")

        grey_l = Points(self.__dimension)
        grey_l.set_points(self.get_points_within_id(gfl_id, left_id[1]))

        # grey_r = Points(self.__dimension)
        # grey_r.set_points(self.get_points_within_id(right_id[0], gfr_id))

        # print("=========GREY L")
        # grey_l.view()
        # print("GREY R")
        # grey_r.view()
        # print("DISTANCE")
        # print(distance)
        for _point in grey_l.__points:
            # print("===================POINT")
            # print(_point.coordinate)
            grey_r_id = self.search(
                int(_point.get(0) + _min), kind="last")
            grey_r = Points(self.__dimension)
            grey_r.set_points(self.get_points_within_id(
                right_id[0],  grey_r_id))
            # print("TARGET END", grey_r_id)
            # print("==========================TARGET")
            for i in range(grey_r.__point_count):
                if not grey_r.__points[i].is_diff_within_distance(_point, _min):
                    continue
                _norm = la.norm(_point, grey_r.__points[i])
                # print(grey_r.__points[i].coordinate)
                # print("NORM", _norm)
                # print("MIN", _min)
                if _norm < _min:
                    _min = _norm
                    min_p1 = grey_r.__points[i]
                    min_p2 = _point
            # _min_temp, min_p1_temp, min_p2_temp = grey_r.__find_closest_pair_with(
            #     _point, _min)
            # if _min_temp < _min:
            #     _min = _min_temp
            #     min_p1 = min_p1_temp
            #     min_p2 = min_p2_temp

        return _min, min_p1, min_p2

    def __find_closest_pair_dnc(self):
        """
            finding closest pair of points using divide and conquer algorithm
        """

        if self.get_point_count() == 2:
            # print("NORM")

            return la.norm(self.get_point(0), self.get_point(1)), self.get_point(0), self.get_point(1)
        else:
            _min = 0
            _min_p1 = point.Point(self.__dimension)
            _min_p2 = point.Point(self.__dimension)

            left_id, right_id = self.divide()
            left = Points(self.__dimension)
            left.set_points(self.get_points_within_id(left_id[0], left_id[1]))

            right = Points(self.__dimension)
            right.set_points(self.get_points_within_id(
                right_id[0], right_id[1]))
            # print("divided")
            # print("left")
            # left.view()
            # print("right")
            # right.view()

            left_min, left_p1, left_p2 = left.__find_closest_pair_dnc()
            right_min, right_p1, right_p2 = right.__find_closest_pair_dnc()

            # print("left min", left_min)
            # print(left_p1.coordinate, left_p2.coordinate)

            # print("right min", right_min)
            # print(right_p1.coordinate, right_p2.coordinate)

            if (left_min < right_min):
                _min = left_min
                _min_p1 = left_p1
                _min_p2 = left_p2
            else:
                _min = right_min
                _min_p1 = right_p1
                _min_p2 = right_p2

            _min_grey, min_p1_grey, min_p2_grey = self.__find_closest_pair_grey(
                _min, left_id, right_id)

            # print("grey min", _min_grey)

            if _min_grey < _min:
                _min = _min_grey
                _min_p1 = min_p1_grey
                _min_p2 = min_p2_grey

            return _min, _min_p1, _min_p2

    def __find_closest_pair_bf(self):
        """
            finding closest pair of points using brute force algorithm
        """
        _min = 1000000000
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
            self.sort(0, self.get_point_count() - 1)
            # print("sorted")
            # self.view()
            return self.__find_closest_pair_dnc()

    def view(self):
        for i in range(self.__point_count):
            print(self.get_point(i).coordinate)
