import points.points as ps
import platform
import points.point as p
import lib.linalg as la
import visualizer.visualizer as vs
import time
import sys
import colorama
import os

def printWelcome():
        print("""
                   __        __       .__
          /  \    /  \ ____ |  |   ____  ____   _____   ____
          \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ /
           \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/
            \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
                \/       \/          \/            \/     \/
              """)
        
def printPlatform():
    print("""
            Here is your computer specification:
            'platform': {},
            'platform-release': {},
            'platform-version': {},
            'architecture': {},
            'processor': {},
            """.format(platform.system(), platform.release(), platform.version(), platform.machine(), platform.processor()))

def printPlatformToFile():
    print("Here is your computer specification:")
    print("'platform': {}.format(plattform.system())")
    print("'platform-release': {}".format(platform.release()))
    print("'architecture': {}".format(platform.machine()))
    print("'processor': {}".format(platform.processor()))
    print("")

def printMenu():
    print("------------------------------------------Menu-------------------------------------------------")
    print("|1. Randomize Points                                                                          |")
    print("|2. Input File                                                                                |")
    print("|3. Exit                                                                                      |")
    print("-----------------------------------------------------------------------------------------------")
    print("")

def printDash():
    print("-----------------------------------------------------------------------------------------------")
    
    
def result(r_n, countPoint):
    CONSTRAINT = 1e9
    ps1 = ps.Points(int(r_n))
    ps1.generate_random(int(countPoint), CONSTRAINT)

    startTimeDNC = time.perf_counter()
    _minDNC, resultDNC = ps1.find_closest_pair()
    endTimeDNC = time.perf_counter()
    calledDNC = la.func_called
    finalTimeDNC = endTimeDNC - startTimeDNC
    
    la.func_called = 0
    startTimeBF = time.perf_counter()
    _minBF, resultBF = ps1.find_closest_pair(kind="bf")
    endTimeBF = time.perf_counter()
    calledBF = la.func_called
    finalTimeBF = endTimeBF - startTimeBF
    
    return _minDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF 

def printToTerminal(_minDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF):
    print("-----------------------------------------------------------------------------------------------")
    print("|  Algorithm  |     Minimum Distance       |      Time       |      Function Norm Called      |")
    print("-----------------------------------------------------------------------------------------------")   
    print("|    DNC      |         {:.2f}      |     {:.2f} ms       |             {:.2f}             |".format(_minDNC, finalTimeDNC, calledDNC))
    print("-----------------------------------------------------------------------------------------------")
    print("|    BF       |         {:.2f}      |     {:.2f} ms       |             {:.2f}             |".format(_minBF, finalTimeBF, calledBF))
    print("-----------------------------------------------------------------------------------------------")


def inputFile():
    pass

    
def outputToFile(fileName, dimension, pointCount, _minDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF):
    original_stdout = sys.stdout
    #path = sys.path[0]
    #joinPath = path.replace("src", "tc")
    #savePath = joinPath + fileName +".txt"
    with open(fileName+".txt", 'w') as f:
        sys.stdout = f 
        printPlatformToFile()
        print("Dimension: {}".format(dimension))
        print("n: {}".format(pointCount))
        printToTerminal(_minDNC, calledDNC, finalTimeDNC, _minBF, calledBF, finalTimeBF)
        
        sys.stdout = original_stdout 

def printGoodbye():
    print("""
             ________                  .______.                 
            /  _____/  ____   ____   __| _/\_ |__ ___.__. ____  
            /   \  ___ /  _ \ /  _ \ / __ |  | __ <   |  |/ __ \ 
            \    \_\  (  <_> |  <_> ) /_/ |  | \_\ \___  \  ___/ 
            \______  /\____/ \____/\____ |  |___  / ____|\___  >
                    \/                   \/      \/\/         \/ 
              """)