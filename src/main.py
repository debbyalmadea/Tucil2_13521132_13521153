import visualizer.visualizer as vs
import utils.output as op
import utils.input as ip
import points.points as ps
if __name__ == "__main__":
    start = True
    while (start):
        op.printWelcome()
        op.printPlatform()
        op.printMenu()
        inputMenu = input("Choice: ")
        op.printDash()

        if (inputMenu == "1"):

            startPoint = True

            while (startPoint):

                print("Input dimension or type 'e' to go back to menu")
                r_n = input("Dimension size: ")

                if (r_n.isdigit()):
                    countPoint = input("Input n points: ")

                    if (countPoint.isdigit() and int(countPoint) > 1):
                        CONSTRAINT = 1e9
                        _points = ps.Points(int(r_n))
                        _points.generate_random(int(countPoint), CONSTRAINT)
                        _points, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF = op.result(
                            _points)
                        op.printToTerminal(
                            _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                        toFile = input("Print to File? y/n ")

                        if (toFile == "y"):
                            fileName = input("File Name: ")
                            op.outputToFile(fileName, r_n, countPoint, _minDNC, resultDNC,
                                            calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                        elif (toFile == "n"):
                            startPoint = False

                        if(int(r_n) == 3):
                            print("Do you want to visualize the data? y/n")
                            inputVisualize = input("Choice: ")
                            if (inputVisualize == "y"):
                                print("Visualizing...")
                                vs.visualize(_points, resultDNC)
                            elif (inputVisualize == "n"):
                                print("Back to previous menu...")
                                print("--------------------------------------")
                            else:
                                print("Please input between y or n")
                                print("--------------------------------------")
                    elif (countPoint.isdigit() and countPoint == "1"):
                        print("Please input more than one points")

                elif (not r_n.isdigit() and r_n != "e"):
                    print("Please input double only")

                elif (r_n == "e"):
                    startPoint = False
        elif (inputMenu == "2"):
            findFile = True
            while (findFile):
                try:
                    inputFileName = input(
                        "Please input filename or type 'e' to return to previous menu: ")
                    if (inputFileName == "e"):
                        findFile = False
                    else:
                        try:
                            splitText, dimension, numberOfPoints = ip.inputFile(
                                inputFileName)
                            _points = ip.processPoints(
                                splitText, dimension, numberOfPoints)
                            _points, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF = op.result(
                                _points)
                            op.printToTerminal(
                                _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)
                            toFile = input("Print to File? y/n ")

                            if (toFile == "y"):
                                fileName = input("File Name: ")
                                op.outputToFile(fileName, dimension, numberOfPoints, _minDNC,
                                                resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                            elif (toFile == "n"):
                                findFile = False

                            if(dimension == 3):
                                print("Do you want to visualize the data? y/n")
                                inputVisualize = input("Choice: ")
                                if (inputVisualize == "y"):
                                    print("Visualizing...")
                                    vs.visualize(_points, resultDNC)
                                elif (inputVisualize == "n"):
                                    print("Back to previous menu...")
                                    print(
                                        "--------------------------------------")
                                else:
                                    print("Please input between y or n")
                                    print(
                                        "--------------------------------------")
                        except Exception as err:
                            print(err.args)

                except FileNotFoundError:
                    print("File not found")

        elif (inputMenu == "3"):
            op.printGoodbye()
            start = False
        else:
            print("The option is between 1 or 2")

    #CONSTRAINT = 1e9
    #ps1 = ps.Points(3)

    # jangan dihapus buat debugging :333333
    # p1 = p.Point(3, [0,0,1])
    # p2 = p.Point(3, [0,0,4])
    # p3 = p.Point(3, [0,0,2])
    # p4 = p.Point(3, [0,0,3])
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

    #ps1.generate_random(128, CONSTRAINT)
    # print("----------------------")
    # print(ps1.get_point(4).get(2))
    # ps1.sort(0, ps1.get_point_count()-1)
    # Make throw exception
    # start = time.perf_counter()
    #_min,resultDNC = ps1.find_closest_pair()
    # end = time.perf_counter()
    # print("==============BY DNC")
    # print(_min)
    # print(p1.coordinate)
    # print(p2.coordinate)
    # print("FUNC NORM CALLED:", la.func_called)
    # print("TIME", end - start)

    # la.func_called = 0
    # print("==============BY BF")
    # start = time.perf_counter()
    # _min, p1, p2 = ps1.find_closest_pair(kind="bf")
    # end = time.perf_counter()
    # print(_min)
    # print(p1.coordinate)
    # print(p2.coordinate)
    # print("FUNC NORM CALLED:", la.func_called)
    # print("TIME", end - start)

    # for i in range(len(result)):
    #    for j in range(len(result[i])):
    #        print(result[i][j].get(j))

    # if (ps1.get_dimension() == 3):
    #    vs.visualize(ps1, resultDNC)
