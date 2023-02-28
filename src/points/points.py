import points.point as point
import lib.linalg as la
import math
import time


class Points:
    def __init__(self, dimension, points=[]):
        self.__dimension = dimension
        self.__points = points
        self.__point_count = 0

    # getter
    def get_points(self):
        """
            return points
        """
        return self.__points

    def get_point(self, id):
        return self.__points[id]

    def get_points_within_id(self, start_id, end_id):
        """
            return points dari start_id s.d. end_id
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
        self.__points = points
        self.__point_count = len(points)

    def set_empty(self):
        self.__points = []
        self.__point_count = 0

    # other function

    def generate_random(self, point_count, constraint):
        """
            menghasilkan points secara random
        """
        self.set_empty()
        _points = []
        for i in range(point_count):
            _point = point.Point(self.get_dimension())
            _point.generate_random(constraint)
            _points.append(_point)
        self.set_points(_points)

    def add(self, point):
        """
            tambahkan point ke dalam points
        """
        self.__points.append(point)
        self.__point_count += 1

    def __partition(self, lowIdx, highIdx, axis):
        """
            partisi untuk quicksort
        """
        # get 1-3
        pivot = self.get_point(highIdx)  # Pivot x terakhir
        i = lowIdx - 1
        for k in range(lowIdx, highIdx):
            if self.get_point(k).less_than_eq(pivot, axis):
                i += 1
                self.__points[i], self.__points[k] = self.__points[k], self.__points[i]

        self.__points[i+1], self.__points[highIdx] = self.__points[highIdx], self.__points[i+1]
        return i+1

    def sort(self, lowId, highIdx, axis=0):
        """
            mengurutkan points berdasarkan axis
        """
        i = lowId
        j = highIdx
        if i < j:
            partitionId = self.__partition(lowId, highIdx, axis)
            self.sort(i, partitionId-1, axis)
            self.sort(partitionId+1, j, axis)

    def __search_fo(self, low, high, value, axis):
        """
            prereq: points terurut membesar berdasarkan axis

            return indeks dari kejadian pertama ditemukan nilai dari axis
            sebesar value dengan menggunakan binary search
            jika tidak ada nilai dari axis yang bernilai value, maka
            return indeks kejadian pertama ditemukannya nilai dari axis
            lebih besar dari value
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

        return low

    def __search_lo(self, low, high, value, axis):
        """
            prereq: points terurut membesar berdasarkan axis

            return indeks dari kejadian terakhir ditemukan nilai dari axis
            sebesar value dengan menggunakan binary search
            jika tidak ada nilai dari axis yang bernilai value, maka
            return indeks kejadian terakhir ditemukannya nilai dari axis
            lebih kecil dari value
        """
        if (high >= low and high < self.__point_count):
            mid = low + (high - low) // 2
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

        return high

    def __search(self, value, kind="first", axis=0):
        """
            prereq: points terurut membesar berdasarkan axis
        """
        if kind == "first":
            return self.__search_fo(0, self.get_point_count() - 1, value, axis)
        elif kind == "last":
            return self.__search_lo(0, self.get_point_count() - 1, value, axis)

    def divide(self):
        """
            return tuple
            1. array of integer dengan dua elemen merepresentasikan indeks awal 
               dan indeks akhir dari setengah bagian awal points
            2. array of integer dengan dua elemen merepresentasikan indeks awal 
               dan indeks akhir dari setengah bagian akhir points
        """
        left_sid = 0
        left_eid = self.__point_count // 2 - 1
        right_sid = self.__point_count // 2
        right_eid = self.__point_count - 1

        return [left_sid, left_eid], [right_sid, right_eid]

    def __find_closest_pair_grey(self, distance, left_id, right_id, axis=0):
        """
            return pasangan point di dalam grey area 
        """
        _min = distance
        result = []

        left_closest = self.get_point(left_id[1])
        right_closest = self.get_point(right_id[0])

        # grey area farthest left id
        gfl_id = self.__search(
            right_closest.get(axis) - distance, kind="first")

        grey_l = Points(self.__dimension)
        grey_l.set_points(self.get_points_within_id(gfl_id, left_id[1]))

        if grey_l.get_point_count() > 0:
            # grey area farthest right id
            gfr_id = self.__search(left_closest.get(
                axis) + distance, kind="last")
            grey_r = Points(self.__dimension)
            grey_r.set_points(self.get_points_within_id(right_id[0],  gfr_id))

            for i in range(grey_l.__point_count):
                p1 = grey_l.get_point(grey_l.get_point_count() - i - 1)
                for i in range(grey_r.__point_count):
                    p2 = grey_r.__points[i]

                    if not p2.is_diff_within_distance(p1, _min):
                        continue
                    _norm = la.norm(p1, p2)
                    if _norm < _min:
                        _min = _norm
                        result = [[p1, p2]]
                    elif _norm == _min:
                        result += [[p1, p2]]

        if len(result) > 0:
            return _min, result
        else:
            return math.inf, []

    def __find_closest_pair_dnc(self):
        """
            mencari closest pair of points dengan algoritma divide and conquer 
        """
        if self.get_point_count() == 1:
            return math.inf, []
        elif self.get_point_count() == 2:
            norm = la.norm(self.get_point(0), self.get_point(1))
            return norm, [[self.get_point(0), self.get_point(1)]]
        else:
            _min = 0
            result = []

            left_id, right_id = self.divide()
            left = Points(self.__dimension)
            left.set_points(self.get_points_within_id(left_id[0], left_id[1]))

            right = Points(self.__dimension)
            right.set_points(self.get_points_within_id(
                right_id[0], right_id[1]))

            left_min, left_result = left.__find_closest_pair_dnc()
            right_min, right_result = right.__find_closest_pair_dnc()

            if (left_min < right_min):
                _min = left_min
                result = left_result
            elif (left_min > right_min):
                _min = right_min
                result = right_result
            else:
                _min = left_min
                result = left_result + right_result

            _min_grey, grey_result = self.__find_closest_pair_grey(
                _min, left_id, right_id)

            if _min_grey < _min:
                _min = _min_grey
                result = grey_result
            elif _min_grey == _min:
                result += grey_result

            return _min, result

    def __find_closest_pair_bf(self):
        """
            mencari closest pair of points dengan algoritma brute force
        """
        _min = math.inf
        result = []
        for i in range(self.__point_count):
            for j in range(i + 1, self.__point_count):
                _norm = la.norm(self.get_point(i), self.get_point(j))
                if (_norm < _min):
                    _min = _norm
                    result = [[self.get_point(i), self.get_point(j)]]
                elif (_norm == _min):
                    result += [[self.get_point(i), self.get_point(j)]]

        return _min, result

    def find_closest_pair(self, kind="dnc"):
        """
            mencari closest pair of points.

            kind: algoritma yang digunakan, dapat berupa "dnc" atau "bf"
        """
        if kind == "bf":
            start = time.perf_counter()
            _min, result = self.__find_closest_pair_bf()
            end = time.perf_counter()
            return _min, result, end - start
        elif kind == "dnc":
            self.sort(0, self.get_point_count() - 1)
            start = time.perf_counter()
            _min, result = self.__find_closest_pair_dnc()
            end = time.perf_counter()
            return _min, result, end - start

    def view(self):
        """
            mencetak semua point dalam points
        """
        for i in range(self.__point_count):
            print(self.get_point(i).coordinate)
