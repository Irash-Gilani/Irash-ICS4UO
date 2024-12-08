
# poly.py starts here
class point:
    def __init__(self, x: float = None, y: float = None):
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
        self.__head = point()  # a null point with a null Next field

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


        self.__linkedliststr = "" # initialzes a string to store the linked list items to be printed

        self.__V = self.__head.next # sets the list traverser to the first item in the linked list

        while self.__V != None: # loop continues until the pointer leads to a null value
            self.__linkedliststr += (str(self.__V)) # adds the current item to linkedliststr
            if self.__V.next != None: # adds an arrow to be printed if the next item is not null
                self.__linkedliststr += (" --> ")
            self.__V = self.__V.next # moves to the next item

        return self.__linkedliststr # returns the linked list as a string

#poly.py ends here

# driver starts here

from poly import *

# Irash Gilani
# 846852
# Driver for polygon program

# variable dictionary;
# S - The string fed into GetNumeric to return an x and y coordinate
# x - The x coordinate taken from splitting S, and the x coordinate taken from splitting p
# y - The y coordinate taken from splitting S, and the y coordinate taken from splitting p
# polydata - The first line of text from a2, containing all of the coordinates
# ptarr - an array containing all of the point objects made from processing polydata
# p - a coordinate in polydata that has had its brackets removed
# pt - a point object created from the x and y values taken from p
# poly - a polygon object
# pair - a pair of x and y coordinate in tuple form taken from processing a point through getNumeric

# a function that takes in a coordinate in string format and outputs a tuple containing an x and y coordinate
def getNumeric(S: str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float

    S = S.strip("()") # removes the brackets in the string

    (x, y) = S.split(", ") # gets the x any y coordinates by splitting them up between the comma

    # code below attempts to convert the x and y values gathered from a coordinate string to an int or float
    try:
        x = int(x)
    except:
        x = float(x)

    try:
        y = int(y)
    except:
        y = float(y)

    return (x, y)


fh = open("a2.txt", "r")  # this is the name of the data file to open

polydata = fh.readline().strip() # removes the brackets

polydata = polydata.split(", ") # makes an array made up of the coordinates as individual items, split up by the commas


# make an array of points (str)

ptarr = []

for coord in polydata: # goes through each coordinate item in the polydata array
    p = coord.strip("()") # removes the brackets and assigns the item to p

    [x, y] = p.split(",") # gets the x and y values from p by splitting it by the comma

    pt = point(x, y).__str__() # creates a point object made up of the x and y value and assigns it to pt

    ptarr.append(pt) # appends pt to ptarr

# declare a polygon

Poly = Polygon()

# loop through the points array and turn them into numbers for the polynomial object
for pt in ptarr:
    # generate an x, y pair (numerical not str) from getNumeric
    pair = getNumeric(pt)
    # add to the polynomial (call add_point())
    Poly.add_point(pair[0], pair[1])

print(Poly)  # this should print the entire linked list of points as string

# driver ends here

# separate poly.py and driver into separate files when done
