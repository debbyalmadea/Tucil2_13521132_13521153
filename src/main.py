import points.points as ps
import platform
import points.point as p
if __name__ == "__main__":
    ps1 = ps.Points(3)
    p1 = p.Point(3, [-6, 5, 2])
    p2 = p.Point(3, [-4, -4, -5])
    p3 = p.Point(3, [-2, 5, -2])
    p4 = p.Point(3, [-2, -5, -4])
    # ps1.generate_random(5, 5)
    ps1.add(p1)
    ps1.add(p2)
    ps1.add(p3)
    ps1.add(p4)

    ps1.view()
    _min, p1, p2 = ps1.find_closest_pair(kind="bf")
    print(_min)
    print(p1.coordinate)
    print(p2.coordinate)
    # print("----------------------")
    # print(ps1.get_point(4).get(2))
    # ps1.sort(2, 0, ps1.get_point_count()-1)
    # ps1.view()
    # Make throw exception

    ps1.find_closest_pair()
