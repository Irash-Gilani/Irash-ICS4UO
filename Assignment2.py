import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getPoint(self):
        return "({0}, {1})".format(self.__x, self.__y)
   
    def distance(self, p2):
        return math.sqrt((self.__x-p2.x)**2 + (self.__y-p2.y)**2)
    
class Polygon(Point):
    
    # creates a vertex
    def add_point(x, y):
        return Point(x, y).getPoint()
    

try:
    fh = open("a2.txt", "r")
    
    # read the line of coordinates, split them up and
    # process them through a linked list
    
    fh.close()

except OSError as err:
    print("File not found", err)
except EOFError as err2:
    print("End of file exceeded", err2)
    fh.close()
  
  
  
#unfinished

