
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def isPointResult(point, result):
    for i in range(len(result)):
        if point.is_equal(result[i][0]) or point.is_equal(result[i][1]):
            return True
    
    return False

def visualize(points, pairedPoints, fileName): #ambah param point1, point2
    
    """
    Plotting points
    """
    colorArr = ["red", "blue", "green", "cyan", "yellow"]
    colorId = 0
    ax = plt.figure(figsize=(15,10)).add_subplot(111, projection='3d')

    """
    Setting biar point terdekat warnanya beda
    """
    # arrlen = points.shape[0]
    '''for i in range(arrlen):
        if ((x[i] == p1.get(0) and y[i] == p1.get(1) and z[i] == p1.get(2)) or (x[i] == p2.get(0) and y[i] == p2.get(1) and z[i] == p2.get(2)) ):
            ax.scatter(x[i], y[i], z[i], color = "red")
        else:
            ax.scatter(x[i], y[i], z[i], color = "gray")'''
    for i in range(points.get_point_count()):
        _point = points.get_point(i)
        if isPointResult(_point, pairedPoints):
            continue
        else:
            ax.scatter(_point.get(0), _point.get(1), _point.get(2), color = "gray")
            
    for i in range(len(pairedPoints)):
        ax.scatter(pairedPoints[i][0].get(0), pairedPoints[i][0].get(1), pairedPoints[i][0].get(2), color = colorArr[colorId])
        ax.scatter(pairedPoints[i][1].get(0), pairedPoints[i][1].get(1), pairedPoints[i][1].get(2), color = colorArr[colorId])
        if colorId == len(colorArr) - 1:
            colorId = 0
        else:
            colorId += 1
    """
    Modify Graph
    """
    plt.title("Find Closest Distance 3D")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.clabel("z")
    ax.xaxis.label.set_color('red')
    ax.yaxis.label.set_color('blue')
    ax.w_xaxis.line.set_color("red")
    ax.w_yaxis.line.set_color("blue")
    ax.w_zaxis.line.set_color("green")
    # ax.set_xlim3d([-1e9, 1e9])
    # ax.set_ylim3d([-1e9, 1e9])
    # ax.set_zlim3d([-1e9, 1e9])
    
    #Show
    plt.savefig('output/' + fileName)
    plt.show()