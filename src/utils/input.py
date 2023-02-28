import points.points as ps
import points.point as p


def inputFile(inputFileName):
    """
    membaca input dari file
    """
    f = open("input/" + inputFileName + ".txt", "r")
    readText = []
    readText = f.read()
    f.close()
    splitText = readText.splitlines()

    if len(splitText) < 2:
        raise Exception("Incorrect File configuration")

    dimension = int(splitText[0])
    if dimension <= 0:
        raise Exception(
            "Incorrect File configuration: Dimension must be at least 1")
    if dimension > 100:
        raise Exception(
            "Incorrect File configuration: Dimension greater than 100. Too big")

    numberOfPoints = int(splitText[1])
    if numberOfPoints < 2:
        raise Exception(
            "Incorrect File configuration: Number of points are less than 2")

    if numberOfPoints > 10000:
        raise Exception(
            "Incorrect File configuration: Maximum number of points are 10000")
    count = len(splitText) - 2

    if count != numberOfPoints:
        raise Exception("Incorrect File configuration: Unmatched number of points. Expected: " +
                        str(numberOfPoints) + ". Obtained: " + str(count))

    for i in range(2, len(splitText)):
        for j in range(dimension):
            split = splitText[i].split()
            if (len(split) != dimension):
                raise Exception(
                    "Incorrect File configuration: Incorrect dimension for point in line " + str(i + 1))

    return splitText, dimension, numberOfPoints


def processPoints(splitText, dimension, numberOfPoints):
    """
    mengubah input array of integer menjadi points
    """
    hasil = [0 for i in range(numberOfPoints)]
    for i in range(2, numberOfPoints+2):
        hasil[i-2] = splitText[i].split()

    for i in range(numberOfPoints):
        for j in range(dimension):
            hasil[i][j] = float(hasil[i][j])
            if hasil[i][j] > 1e9:
                raise Exception(
                    "Incorrect File configuration: There is a point with more than 1e9 value")
            if hasil[i][j] < -1e9:
                raise Exception(
                    "Incorrect File configuration: There is a point with less than -1e9 value")

    ps1 = ps.Points(dimension)
    for i in range(numberOfPoints-2):
        ps1.add(p.Point(dimension, hasil[i]))
    return ps1
