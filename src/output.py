import points.points as ps
import platform
import points.point as p
import lib.linalg as la
import visualizer.visualizer as vs
import time
import sys
import colorama
from colorama import Fore, Back, Style
import psutil

# To reset color
colorama.init(autoreset=True)


def printWelcome():
    print(Fore.YELLOW + """
                   __        __       .__
          /  \    /  \ ____ |  |   ____  ____   _____   ____
          \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ /
           \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/
            \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
                \/       \/          \/            \/     \/
              """)
    print()


def printPlatform():
    print("""
            Here is your computer specification:
            'platform': {},
            'platform-release': {},
            'platform-version': {},
            'architecture': {},
            'processor': {},
            'ram': {} GB
            """.format(platform.system(), platform.release(), platform.version(), platform.machine(), platform.processor(), (psutil.virtual_memory()[0]/1000000000)))


def printPlatformToFile():
    print("Here is your computer specification:")
    print("'platform': {}.format(plattform.system())")
    print("'platform-release': {}".format(platform.release()))
    print("'architecture': {}".format(platform.machine()))
    print("'processor': {}".format(platform.processor()))
    print("'ram': {} GB".format(psutil.virtual_memory()[0]/1000000000))
    print("")


def printMenu():
    print("")
    print(Fore.LIGHTGREEN_EX +
          "------------------------------------------Menu-------------------------------------------------")
    print(Fore.LIGHTGREEN_EX +
          "|1. Randomize Points                                                                          |")
    print(Fore.LIGHTGREEN_EX +
          "|2. Input File                                                                                |")
    print(Fore.LIGHTGREEN_EX +
          "|3. Exit                                                                                      |")
    print(Fore.LIGHTGREEN_EX +
          "-----------------------------------------------------------------------------------------------")
    print("")


def printDash():
    print(Fore.RED + "-----------------------------------------------------------------------------------------------")


def result(_points):
    _minDNC, resultDNC, finalTimeDNC = _points.find_closest_pair()
    calledDNC = la.func_called

    la.func_called = 0
    _minBF, resultBF, finalTimeBF = _points.find_closest_pair(kind="bf")
    calledBF = la.func_called

    return _points, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF


def printToTerminal(_minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF):
    print("")
    print(Fore.GREEN + "-----------------------------------------------------------------------------------------------")
    print(Fore.GREEN + "|  Algorithm  |     Minimum Distance       |      Time       |      Function Norm Called      |")
    print(Fore.GREEN + "-----------------------------------------------------------------------------------------------")
    print(Fore.GREEN + "|    DNC      |         {:.2f}      |     {:.4f} ms       |             {}             |".format(
        _minDNC, finalTimeDNC, calledDNC))
    print(Fore.GREEN + "-----------------------------------------------------------------------------------------------")
    print(Fore.GREEN + "|    BF       |         {:.2f}      |     {:.4f} ms       |             {}             |".format(
        _minBF, finalTimeBF, calledBF))
    print(Fore.GREEN + "-----------------------------------------------------------------------------------------------")
    print("")

    print("")
    for i in range(len(resultDNC)):
        print(Fore.CYAN + "-----------------------------------------------------------------------------------------------")
        print(Fore.CYAN + "|                                         Closest Pair {}                                      |".format(i+1))
        print(Fore.CYAN + "-----------------------------------------------------------------------------------------------")
        for j in range(len(resultDNC[i])):
            print(Fore.CYAN + "-----------------------------------------------------------------------------------------------")
            print(Fore.CYAN + "|{}|".format(resultDNC[i][j].coordinate))
            print(Fore.CYAN + "-----------------------------------------------------------------------------------------------")
    print("")


def printToFile(_minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF):
    print("")
    print("-----------------------------------------------------------------------------------------------")
    print("|  Algorithm  |     Minimum Distance       |      Time       |      Function Norm Called      |")
    print("-----------------------------------------------------------------------------------------------")
    print("|    DNC      |         {:.2f}      |     {:.4f} ms       |             {}             |".format(
        _minDNC, finalTimeDNC, calledDNC))
    print("-----------------------------------------------------------------------------------------------")
    print("|    BF       |         {:.2f}      |     {:.4f} ms       |             {}             |".format(
        _minBF, finalTimeBF, calledBF))
    print("-----------------------------------------------------------------------------------------------")
    print("")

    print("")
    for i in range(len(resultDNC)):
        print("-----------------------------------------------------------------------------------------------")
        print("|                                         Closest Pair {}                                      |".format(i+1))
        print("-----------------------------------------------------------------------------------------------")
        for j in range(len(resultDNC[i])):
            print("-----------------------------------------------------------------------------------------------")
            print("|{}|".format(resultDNC[i][j].coordinate))
            print("-----------------------------------------------------------------------------------------------")
    print("")


def inputFile(inputFileName):

    f = open("../input/" + inputFileName + ".txt", "r")
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


def outputToFile(outputFileName, dimension, pointCount, _minDNC, resultDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF):
    original_stdout = sys.stdout
    #path = sys.path[0]
    #joinPath = path.replace("src", "tc")
    #savePath = joinPath + fileName +".txt"
    with open("../output/" + outputFileName+".txt", 'w') as f:
        sys.stdout = f
        printPlatformToFile()
        print("Dimension: {}".format(dimension))
        print("n: {}".format(pointCount))
        printToFile(_minDNC, resultDNC, calledDNC,
                    finalTimeDNC, _minBF, calledBF, finalTimeBF)

        sys.stdout = original_stdout

        f.close()


def printGoodbye():
    print(Fore.YELLOW + """
             ________                  .______.                 
            /  _____/  ____   ____   __| _/\_ |__ ___.__. ____  
            /   \  ___ /  _ \ /  _ \ / __ |  | __ <   |  |/ __ \ 
            \    \_\  (  <_> |  <_> ) /_/ |  | \_\ \___  \  ___/ 
            \______  /\____/ \____/\____ |  |___  / ____|\___  >
                    \/                   \/      \/\/         \/ 
              """)
