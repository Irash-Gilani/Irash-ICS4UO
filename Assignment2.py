import math
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getPoint(self):
        return ({0}, {1}).format(self.__x, self.__y)
   
    def distance(self, p2):
        return math.sqrt((self.__x-p2.x)**2 + (self.__y-p2.y)**2)
    
class Polygon(Point):
    
    def add_point(self, x, y):
        vertex = Point(x, y)
        

print(Polygon.add_point(5, 3))
        
        
#unfinsihed 

