import points.points as ps
import points.point as p


def inputFile(inputFileName):

    f = open("input/" + inputFileName + ".txt", "r")
    readText = []
    readText = f.read()
    splitText = readText.splitlines()

    dimension = int(splitText[0])
    numberOfPoints = int(splitText[1])

    count = len(splitText) - 2

    if count != numberOfPoints:
        raise Exception("Jumlah poin salah. Jumlah yang diharapkan:",
                        numberOfPoints, "Jumlah yang diperoleh:", count)

    # for i in range(2, len(splitText)):
    for i in range(2, len(splitText)):
        for j in range(dimension):
            split = splitText[i].split()
            if (len(split) != dimension):
                raise Exception("Dimensi salah pada poin di line", i + 1)

    f.close()
    return splitText, dimension, numberOfPoints


def processPoints(splitText, dimension, numberOfPoints):
    hasil = [0 for i in range(numberOfPoints)]
    for i in range(2, numberOfPoints+2):
        hasil[i-2] = splitText[i].split()

    for i in range(numberOfPoints):
        for j in range(dimension):
            hasil[i][j] = float(hasil[i][j])

    ps1 = ps.Points(dimension)
    for i in range(numberOfPoints-2):
        ps1.add(p.Point(dimension, hasil[i]))
    return ps1
