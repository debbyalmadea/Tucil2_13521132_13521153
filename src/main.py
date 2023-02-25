import points.points as ps
import platform
import points.point as p
import lib.linalg as la
import visualizer.visualizer as vs
import time

if __name__ == "__main__":
    ps1 = ps.Points(3)

    # jangan dihapus buat debugging :333333
    # p1 = p.Point(3, [-10, 8, 8])
    # p2 = p.Point(3, [-5, -9, 4])
    # p3 = p.Point(3, [-4, -3, 1])
    # p4 = p.Point(3, [3, 6, -2])
    # p5 = p.Point(3, [5, 9, 0])
    # p6 = p.Point(3, [6, -6, -2])
    # p7 = p.Point(3, [6, 3, 4])
    # p8 = p.Point(3, [7, 4, -2])
    # ps1.add(p1)
    # ps1.add(p2)
    # ps1.add(p3)
    # ps1.add(p4)
    # ps1.add(p5)
    # ps1.add(p6)
    # ps1.add(p7)
    # ps1.add(p8)

    ps1.generate_random(256, 1000000)
    # print("----------------------")
    # print(ps1.get_point(4).get(2))
    # ps1.sort(0, ps1.get_point_count()-1)
    # Make throw exception

    start = time.perf_counter()
    _min, p1, p2 = ps1.find_closest_pair()
    end = time.perf_counter()
    print("==============BY DNC")
    print(_min)
    print(p1.coordinate)
    print(p2.coordinate)
    print("FUNC NORM CALLED:", la.func_called)
    print("TIME", end - start)

    print("==============BY BF")
    start = time.perf_counter()
    _min, p1, p2 = ps1.find_closest_pair(kind="bf")
    end = time.perf_counter()
    print(_min)
    print(p1.coordinate)
    print(p2.coordinate)
    print("TIME", end - start)

    pointArray = vs.changeToNumpy(ps1)
    vs.visualize(pointArray, p1, p2)
