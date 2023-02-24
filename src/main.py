import points.points as ps

if __name__ == "__main__":
    ps1 = ps.Points(3)
    ps1.generate_random(5, 5)
    ps1.view()
    _min, p1, p2 = ps1.find_closest_pair(kind="bf")
    print(_min)
    print(p1.coordinate)
    print(p2.coordinate)
