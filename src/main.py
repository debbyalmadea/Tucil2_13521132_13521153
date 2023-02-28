import points.points as ps
import platform
import points.point as p
import lib.linalg as la
import visualizer.visualizer as vs
import time
import colorama
import output as op

if __name__ == "__main__":

    start = True
    while (start):
        op.printWelcome()
        op.printPlatform()
        op.printMenu()
        inputMenu = int(input("Choice: "))
        op.printDash()

        if (inputMenu == 1):
            
            startPoint = True
            
            while (startPoint):
                
                print("Input dimension or type 'e' to go back to menu")
                r_n = input("Dimension size: ")
                
                if (r_n.isdigit()):
                    countPoint = input("Input n points: ")

                    if (countPoint.isdigit()):
                        _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF = op.result(r_n, countPoint)
                        op.printToTerminal(_minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF)
                        
                        toFile = input("Print to File? y/n ")
                        
                        if (toFile == "y"):
                            fileName = input("File Name: ")
                            op.outputToFile(fileName,r_n, countPoint, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF)
                        
                        elif (toFile == "n"):
                            startPoint = False
                            
                        """if(int(r_n) == 3):
                            print("Do you want to visualize the data? y/n")
                            inputVisualize = input("Choice: ")
                            if (inputVisualize == "y"):
                                print("Visualizing...")
                            elif (inputVisualize == "n"):
                                print("Back to previous menu...")
                                print("--------------------------------------")
                            else:
                                print("Please input between y or n")
                                print("--------------------------------------")"""

                elif (not r_n.isdigit() and r_n != "e"):
                    print("Please input double only")
                
                elif (r_n == "e"):
                    startPoint = False
        elif (inputMenu == 2):
            findFile = True
            while (findFile):
                try:
                    inputFileName = input("Please input filename or type 'e' to return to previous menu: ")
                    if (inputFileName == "e"):
                        findFile = False
                    else:
                        dimension, numberofPoint, parts = op.inputFile(inputFileName)
                        _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF = op.resultFromInputFile(dimension, numberofPoint, parts)
                        op.printToTerminal(_minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF)
                        toFile = input("Print to File? y/n ")
                        
                        if (toFile == "y"):
                            fileName = input("File Name: ")
                            op.outputToFile(fileName, dimension, numberofPoint, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF)
                        
                        elif (toFile == "n"):
                            findFile = False
                
                except FileNotFoundError:
                    print("File not found")
            
    
        elif (inputMenu == 3):
            op.printGoodbye()
            start = False
        else:
            print("The option is between 1 or 2")
            
            
    # CONSTRAINT = 1e9
    # ps1 = ps.Points(3)

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

    # ps1.generate_random(1000, CONSTRAINT)
    # print("----------------------")
    # print(ps1.get_point(4).get(2))
    # ps1.sort(0, ps1.get_point_count()-1)
    # Make throw exception
    # start = time.perf_counter()
    # _min, p1, p2 = ps1.find_closest_pair()
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
    
    #for i in range(len(result)):
    #    for j in range(len(result[i])):
    #        print(result[i][j].get(j))

    # if (ps1.get_dimension() == 3):
    #    pointArray = vs.changeToNumpy(ps1)
    #    vs.visualize(pointArray, p1, p2)