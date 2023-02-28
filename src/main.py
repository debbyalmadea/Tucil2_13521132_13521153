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

                if (r_n.isdigit() and int(r_n) > 0 and int(r_n) <= 100):
                    countPoint = input("Input n points: ")
                    if (countPoint.isdigit() and int(countPoint) > 1 and int(countPoint) <= 10000):
                        CONSTRAINT = 1e9
                        _points = ps.Points(int(r_n))
                        _points.generate_random(int(countPoint), CONSTRAINT)
                        _points, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF = op.result(
                            _points)
                        op.printToTerminal(
                            _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                        toFile = input("Print to File? y/n ")

                        while toFile != "y" and toFile != "Y" and toFile != "n" and toFile != "N":
                            print("Please input between y or n")
                            print(
                                "--------------------------------------")
                            toFile = input("Print to File? y/n ")

                        if (toFile == "y" or toFile == "Y"):
                            fileName = input("File Name: ")
                            op.outputToFile(fileName, r_n, countPoint, _minDNC, resultDNC,
                                            calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                        elif (toFile == "n" or toFile == "N"):
                            findFile = False

                        if(int(r_n) == 3):
                            print("Do you want to visualize the data? y/n")
                            inputVisualize = input("Choice: ")
                            while inputVisualize != "y" and inputVisualize != "Y" and inputVisualize != "n" and inputVisualize != "N":
                                print("Please input between y or n")
                                print(
                                    "--------------------------------------")
                                inputVisualize = input("Choice: ")

                            if (inputVisualize == "y" or inputVisualize == "Y"):
                                fileName = input("Figure Name: ")
                                print("Visualizing...")
                                vs.visualize(_points, resultDNC, fileName)
                            elif (inputVisualize == "n" or inputVisualize != "N"):
                                print("Back to previous menu...")
                                print(
                                    "--------------------------------------")
                    elif (countPoint.isdigit() and int(countPoint) > 10000):
                        print("Too many points. Maximum points are 10000")
                    elif (countPoint.isdigit() and int(countPoint) <= 1):
                        print("Please input more than one points")
                    elif (not countPoint.isdigit()):
                        print("Please input positive integer only")

                elif (not r_n.isdigit() and r_n != "e"):
                    print("Please input positive integer only")

                elif (r_n != "e" and int(r_n) > 100):
                    print("Too many dimension. Keep it under 100")
                elif (r_n.isdigit() and int(r_n) <= 0):
                    print("Please input positive integer only")
                elif (r_n == "e"):
                    startPoint = False

                print("")
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

                            while toFile != "y" and toFile != "Y" and toFile != "n" and toFile != "N":
                                print("Please input between y or n")
                                print(
                                    "--------------------------------------")
                                toFile = input("Print to File? y/n ")
                            if (toFile == "y" or toFile == "Y"):
                                fileName = input("File Name: ")
                                op.outputToFile(fileName, dimension, numberOfPoints, _minDNC,
                                                resultDNC, calledDNC, finalTimeDNC, _minBF, resultBF, calledBF, finalTimeBF)

                            elif (toFile == "n" or toFile == "N"):
                                findFile = False

                            if(dimension == 3):
                                print("Do you want to visualize the data? y/n")
                                inputVisualize = input("Choice: ")
                                while inputVisualize != "y" and inputVisualize != "Y" and inputVisualize != "n" and inputVisualize != "N":
                                    print("Please input between y or n")
                                    print(
                                        "--------------------------------------")
                                    inputVisualize = input("Choice: ")
                                if (inputVisualize == "y" or inputVisualize == "Y"):
                                    fileName = input("Figure Name: ")
                                    print("Visualizing...")
                                    vs.visualize(_points, resultDNC, fileName)
                                elif (inputVisualize == "n" or inputVisualize == "N"):
                                    print("Back to previous menu...")
                                    print(
                                        "--------------------------------------")
                        except Exception as err:
                            print(err)
                            print("")
                        except:
                            print("Incorrect File configuration")

                except FileNotFoundError:
                    print("File not found")

        elif (inputMenu == "3"):
            op.printGoodbye()
            start = False
        else:
            print("The option is between 1 or 2")
