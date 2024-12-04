
# poly.py starts here

class point:
    def __init__(self, x: float=None, y: float=None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None


    def valid(self):
        # A validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.
        val = True
        
        if val == None:
            val = False
        
        if val != int or val != float:
            val = False
    
        return val
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __str__(self):
        # point (x, y) expressed this way as string
        # as in: (4, 5)
        
        return "({0}, {1})".format(self.__x, self.__y)

class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = point() # a null point with a null Next field
        
    def add_point(self, x: float, y: float):
        # initialize a point object V
        # if it is the first point, create the object with variable V make head.next point to V
        # if it is any other point, V.next points to it, and V traverses to that point
        # count the vertices as you go
        
        self.__x = x
        self.__y = y
        
        if self.vertices == 0:
            V = point(self.__x, self.__y)
            self.__head.next = V
            self.__vertices += 1
        else:
            V.next = V
            self.__vertices += 1
            V = V.next
            self.__sides += 1
            
    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as string
        # You need to use point's __str__ function to help you.
        
        V = self.__head
        
        while V.next != None:
            V.next = V
            print(V, "-->", end="")
            V = V.next
    

#poly.py ends here

# driver starts here

# driver for the polygon class
#from poly import *

def getNumeric(S : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    
    S = point(S)
    
    x = point.getX(S)
    y = point.getY(S)

    return (x, y)

fh = open("a2.txt", "r") # this is the name of the data file to open

polydata = fh.readline().strip()

polydata = polydata.split(", ")

# make an array of points (str)
# do this as a linked list

ptarr = []

for coord in polydata:
    
    p = coord.strip("()")
    
    [x, y] = p.split(",")
    
    try:
        x = int(x)
    except:
        x = float(x)
    
    try:
        y = int(y)
    except:
        y = float(y)
        
    print(x, y)
    print(point(x, y))
    
    # use getNumeric instead
    pt = point(x, y).__str__()
    
    ptarr.append(pt)
    
print(ptarr)

# declare a polygon

Poly = Polygon(ptarr)

# loop through the points array and turn them into numbers for the polynomial object
    # generate an x, y pair (numerical not str) from getNumeric
    # add to the polynomial (call add_point())

print(Poly) # this should print the entire linked list of points as string

# driver ends here

# separate poly.py and driver into separate files when done
