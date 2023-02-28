import points.points as ps
import points.point as p


def inputFile(inputFileName):

    f = open("input/" + inputFileName + ".txt", "r")
    readText = []
    readText = f.read()
    splitText = readText.splitlines()

    if len(splitText) < 2:
        raise Exception("Konfigurasi file salah")

    dimension = int(splitText[0])
    if dimension > 100:
        raise Exception(
            "Konfigurasi file salah: Dimensi di atas 100, terlalu besar")

    numberOfPoints = int(splitText[1])
    if numberOfPoints < 2:
        raise Exception("Konfigurasi file salah: Jumlah titik kurang dari 2")

    count = len(splitText) - 2

    if count != numberOfPoints:
        raise Exception("Konfigurasi file salah: Jumlah titik salah. Jumlah yang diharapkan: " +
                        str(numberOfPoints) + ". Jumlah yang diperoleh: " + str(count))

    # for i in range(2, len(splitText)):
    for i in range(2, len(splitText)):
        for j in range(dimension):
            split = splitText[i].split()
            if (len(split) != dimension):
                raise Exception(
                    "Konfigurasi file salah: Dimensi salah pada titik di line " + str(i + 1))

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
