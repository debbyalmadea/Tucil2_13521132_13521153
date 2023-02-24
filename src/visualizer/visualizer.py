import points.points as p
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


def changeToNumpy(points):
    toArray = [[0 for j in range(3)] for i in range(points.get_point_count())]
    for i in range(0, points.get_point_count()-1):
        for j in range(0,3):
            toArray[i][j] = points.get_point(i).get(j)
    
    npArray = np.array(toArray)
    
    return npArray

def visualize(array, p1, p2): #ambah param point1, point2
    
    #Plotting points
    ax = plt.figure().add_subplot(111, projection='3d')
    x = array[:,0]
    y = array[:,1]
    z = array[:,2]
    
    #Setting biar point terdekat warnanya beda
    arrlen = array.shape[0]
    for i in range(arrlen):
        if ( (x[i] == p1.get(0) and y[i] == p1.get(1) and z[i] == p1.get(2)) or (x[i] == p2.get(0) and y[i] == p2.get(1) and z[i] == p2.get(2)) ):
            ax.scatter(x[i], y[i], z[i], color = "red")
        else:
            ax.scatter(x[i], y[i], z[i], color = "black")
    
    #Modify Graph
    plt.xlabel("x")
    plt.ylabel("y")
    plt.clabel("z")
    #ax.xaxis.label.set_color('red')
    #ax.yaxis.label.set_color('blue')
    #ax.w_xaxis.line.set_color("red")
    #ax.w_yaxis.line.set_color("blue")
    #ax.w_zaxis.line.set_color("green")
    #Show
    plt.show()