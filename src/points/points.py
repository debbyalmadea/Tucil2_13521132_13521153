import point
import lib.linalg as la


class Points:
    def __init__(self, dimension, points=[]):
        self.__dimension = dimension
        self.__points = points
        self.__point_count = 0
        self.sort()

    # getter
    def get_points(self):
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
        self.__dimension = len(points[0])
        self.sort()

    def set_points_random(self):
        pass

    # other function
    def add(self, point):
        self.__points.append(point)
        self.__point_count += 1

    def sort(self, axis=0):
        pass

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
        pass

    def find_closest_pair(self, kind="dnc"):
        pass
