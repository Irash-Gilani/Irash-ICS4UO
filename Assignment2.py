
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
    
        V = point(x, y)
        
        if self.__vertices == 0:
            self.__V = V 
            self.__head.next = self.__V
            
            self.__vertices += 1
        else:
            self.__V.next = V
            self.__vertices += 1
            
            if self.__vertices % 2 == 0:
                self.__sides += 1
            self.__V = self.__V.next
            
    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as string
        # You need to use point's __str__ function to help you.
        
        linkedliststr = ""
        
        self.__V = self.__head.next
        
        while self.__V != None:
            linkedliststr += (str(self.__V))
            if self.__V.next != None:
                linkedliststr += ("-->")
            self.__V = self.__V.next
            
        return linkedliststr
    

#poly.py ends here

# driver starts here

# driver for the polygon class
#from poly import *

def getNumeric(S : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    
    S = S.strip("()")
    
    (x, y) = S.split(", ")
    
    try:
        x = int(x)
    except:
        x = float(x)
    
    try:
        y = int(y)
    except:
        y = float(y)

    return (x, y)

fh = open("a2.txt", "r") # this is the name of the data file to open

polydata = fh.readline().strip()

polydata = polydata.split(", ")

# make an array of points (str)

ptarr = []

for coord in polydata:
    
    p = coord.strip("()")
    
    [x, y] = p.split(",")

    pt = point(x, y).__str__()
    
    ptarr.append(pt)


# declare a polygon

Poly = Polygon()

# loop through the points array and turn them into numbers for the polynomial object
for pt in ptarr:
    # generate an x, y pair (numerical not str) from getNumeric
    pair = getNumeric(pt)
    # add to the polynomial (call add_point())
    Poly.add_point(pair[0], pair[1])

print(Poly) # this should print the entire linked list of points as string

# driver ends here

# separate poly.py and driver into separate files when done
