# poly.py starts here

import math

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
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self, p2):
        return math.sqrt((float(self.__x)-float(p2.getX()))**2 + (float(self.__y)-float(p2.getY()))**2)

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
            if self.__head.next != None:
                self.__sides += 1
        else:
            self.__V.next = V
            self.__vertices += 1

            self.__sides += 1
            self.__V = self.__V.next

        
            
    def getSides(self):
        return(self.__sides)

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

# poly.py ends here

# driver starts here

# driver for the polygon class
#from poly import *

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
# isregular - a boolean that indicates whether or not a polygon is regular
# pair - a pair of x and y coordinates in tuple form taken from processing a point through getNumeric
# ptnum - the index value of items in the ptarr array, serves as a counter in a for loop
# pt2num - an index value that is one less that ptnum
# pair1 - a pair of x and y coordinates in tuple form that correspond to ptnum in ptarr
# pair2 - a pair of x and y coordinates in tuple form that correspond to pt2num in ptarr
# pt1 - pair1 converted to point
# pt2 - pair2 converted to point
# dist - the distance between pt1 and pt2
# dotp - the dot product of pair1 and pair2
# magp - the product of the magnitudes of pair1 and pair2
# angle - the angle between pair1 and pair2's points, calculated by getting the inverse of cosine of dotp / magp
# prevdist - the value of dist that comes before the current value of dist, meant to be compared to the current
# distance value to determine whether or not a polygon is regular
# prevangle - the measure of angle that comes before the current angle value, meant to be compared to the
# current angle value to determine whether or not a polygon is regular
# perimeter - the perimeter of the polygon
# sides - the amount of sides in the polygon 
# area - the area of the polygon
# prod1 - the sum of the products of the x coordinate multiplied by the next y coordinate, taken when calculating the
# area of an irregular polygon
# prod2 - the sum of the products of the y coordinate multiplied by the next x coordinate, taken when calculating the
# area of an irregular polygon
# vert1 - the current vertex, used when calculating prod1 and prod2 for the area of an irregular polygon
# vert2 - the vertex after vert1, used when calculating prod1 and 



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


# a function for getting the dot product between two vectors in radians 
def dotprod(vecA, vecB):
  product = 0
  for count in range(len(vecA)):
    product += vecA[count] * vecB[count]
  return product

# a function for getting the magnitude of a vector
def magnitude(matrix):
  mag = 0
  for val in matrix:
    mag += math.pow(val, 2)
  
  mag = math.sqrt(mag)
  
  return mag


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

#print("sides:", Poly.getSides())

# a boolean for checking if a polygon is regular or not regular
# will return false if all of the angles or side lengths are not equal 
isregular = True

# an array to be made up of the distances between each successive pair of points, to be used in
# permimeter calculations if the polygon is not regular
distarr = []

# below is a for loop that goes through all points in the polygon
# starts at the second item
for ptnum in range(1, len(ptarr)):
    # initializes variable for the previous item
    pt2num = ptnum - 1
    
    # pair1 is current point, pair2 is last point 
    pair1 = getNumeric(ptarr[ptnum])
    pair2 = getNumeric(ptarr[pt2num])
    
    # below is pair1 and pair2 converted to point objects
    pt1 = point(pair1[0], pair1[1])
    pt2 = point(pair2[0], pair2[1])
    
    dist = pt1.distance(pt2)
    distarr.append(dist)
    #print("distance:", dist)
    dotp = dotprod(pair1, pair2)
    #print("dot product:", dotp)
    mag2p = magnitude(pair1)*magnitude(pair2)
    #print("magnitude of both points:", mag2p)
    
    # to get an angle between two points,
    # run cosine inverse of the dotproduct of two vectors divided by the magnitude of two vectors
    angle = math.acos(dotp / mag2p)
    #print("angle in rads:", angle)
    
    # initializes prevdist and prevangle before first check on first point to prevent error
    if ptnum == 1:
        prevdist = dist
        prevangle = angle
        
    # check if distances or angles are unequal
    if ptnum > 1:
        if prevdist != dist or prevangle != angle:
            isregular = False
            
            
    # update prevdist and prevangle before moving on to new points 
    prevdist = dist
    prevangle = angle
    
# below code checks for a regular polygon by comparing the last coordinate in ptarr with the first coordinate in ptarr
# same processes taking place as the code above
if ptnum == len(ptarr) - 1:
    pair1 = getNumeric(ptarr[ptnum])
    pair2 = getNumeric(ptarr[0])
    
    pt1 = point(pair1[0], pair1[1])
    pt2 = point(pair2[0], pair2[1])

    dist = pt1.distance(pt2)
    distarr.append(dist)
    dotp = dotprod(pair1, pair2)
    mag2p = magnitude(pair1)*magnitude(pair2)
    angle = math.acos(dotp / mag2p)
    
    if prevdist != dist or prevangle != angle:
        isregular = False





#print(isregular)
    
perimeter = 0

sides = Poly.getSides()

# if the polygon is regular, the perimeter is found by multiplying the distance of one
# side by the amount of sides 
if isregular == True:
    perimeter = dist*sides
# if the polygon is irregular, the perimeter is found by adding up all of the
# distance values 
else:
    for distval in distarr:
        perimeter += distval
        
#print(perimeter)
    
area = 0

# if the polygon is regular, the area is found using the formula below 
if isregular == True:
    area = ((dist**2)(sides)) / (4)(math.tan(180/sides))
else:
    prod1 = 0
    prod2 = 0
    
    for ptnum in range(len(ptarr)):
        if ptnum != len(ptarr) - 1:
            vert1 = getNumeric(ptarr[ptnum])
            vert2 = getNumeric(ptarr[ptnum + 1])
            
            prod1 += vert1[0]*vert2[1]
            prod2 += vert1[1]*vert2[0]
        else:
             vert1 = getNumeric(ptarr[ptnum])
             vert2 = getNumeric(ptarr[0])
             
             prod1 += vert1[0]*vert2[1]
             prod2 += vert1[1]*vert2[0]
    area = (prod1 - prod2) / 2
    
#print(area)
            
        
    
# driver ends here
