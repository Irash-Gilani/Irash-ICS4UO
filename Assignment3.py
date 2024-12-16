# poly.py starts here
# TODO: Make a header for poly.py

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
        # a boolean for checking if a polygon is regular or not regular
        # will return false if any of the angles or side lengths are unequal with the one that came
        # before them 
        self.__isregular = True
        self.__distsum = 0 # the sum of all side lengths

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

    # returns the amount of sides in the polygon    
    def getSides(self):
        return(self.__sides)
    
    # a function for getting the dot product between two vectors in radians 
    def dotprod(self, vecA, vecB):
      self.__product = 0
      for count in range(len(vecA)):
        self.__product += vecA[count] * vecB[count]
      return self.__product
    
    # a function for getting the magnitude of a vector
    def magnitude(self, matrix):
      self.__mag = 0
      for val in matrix:
        self.__mag += math.pow(val, 2)
      
      self.__mag = math.sqrt(self.__mag)
      
      return self.__mag
    
    def area(self):
        self.__area = 0
        
        self.__V = self.__head.next # sets the list traverser to the first item in the linked list
        # traverses the linked list to gather the sum of all distances
        while self.__V != None: # loop continues until the pointer leads to a null value
            self.__currpoint = self.__V
            if self.__V.next != None: # performs below code if the next item is not null
                self.__nextpoint = self.__V.next
                
                self.__dist = self.nextpoint.distance(self.__currpoint) # calculates the distance between the
                                                                        # current and next point
            
                self.__distsum += self.__dist # adds the distance to distsum
                                                                            
                # gets the dot product of the next and current point
                self.__dotp = self.dotprod((self.nextpoint.getX, self.nextpoint.getY), (self.currpoint.getX, self.currpoint.getY))
                # gets the magnitude of the next and current point
                self.__mag = self.magnitude((self.nextpoint.getX, self.nextpoint.getY), (self.currpoint.getX, self.currpoint.getY))
                
                # obtains the angle between the two points by running cosine inverse of the dot product
                # of the two vectors divided by the magnitude of the two vectors
                self.__angle = math.acos(self.__dotp / self.__mag)
                                                                      
            if self.__V.next == None: # if the traverser is on the last item
                self.__distsum += self.__V.distance(self.__head.next) # adds the distance between the last
                                                                      # and the first point to distsum
                                                                      
            # initializes prevdist and prevangle before first check on first point to prevent an error                                                          
            if self.__V == self.__head.next:
                self.__prevdist = self.__dist
                self.__prevangle = self.__angle
                
            if self.__prevdist != self.__dist or self.__prevangle != self.__angle:
                self.__isregular = False
                
            self.__V = self.__V.next # moves to the next item
            
            
        # below code makes a calculation for area depending on whether or not the polygon is regular
        # if the polygon is regular, the area is found using the formula below
        if self.__isregular == True:
            self.__area = ((self.__dist**2)*(self.__sides)) / (4)*(math.tan(180/self.__sides))
            
            return self.__area
        # if the polygon is irregular, the area is found using the process below
        else:
            self.__prod1 = 0
            self.__prod2 = 0
            #traverse the linked list
            self.__V = self.__head.next # sets the list traverser to the first item in the linked list
            
            while self.__V != None: # loop continues until the pointer leads to a null value
                self.__vert1 = (self.__V.getX, self.__V.getY) # the current coordinate
                self.__vert2 = (self.__V.next.getX, self.__V.next.getY) # the coordinate after the current coordinate
                
                # multiplies the x value of the current point by the y value of the next coordinate
                # and adds it to the first sum of the products
                self.__prod1 += vert1[0]*vert2[1]
                
                # multiplies the y value of the current point by the x value of the next coordinate
                # and adds it to the second sum of the products
                self.__prod2 += vert1[1]*vert2[0]
                
                if self.__V.next == None:
                    # when the traverser is on the last coordinate, perform the algorithim
                    # above using the last and first coordinates as the current and next coordinates
                    self.__vert1 = (self.__V.getX, self.__V.getY)
                    self.__vert2 = (self.__head.next.getX, self.__head.next.getY)
                
                    self.__prod1 += vert1[0]*vert2[1]
                    self.__prod2 += vert1[1]*vert2[0]
                
                self.__V = self.__V.next # moves to the next item
                
            self.__area = (self.__prod1 - self.__prod2) / 2
            
            return self.__area
            
    def perimeter(self):
        self.__perimeter = 0
          
        self.__V = self.__head.next # sets the list traverser to the first item in the linked list
        
        # traverses the linked list to gather the sum of all distances
        while self.__V != None: # loop continues until the pointer leads to a null value
            self.__currpoint = self.__V
            if self.__V.next != None: # performs below code if the next item is not null
                self.__nextpoint = self.__V.next
                    
                self.__dist = self.nextpoint.distance(self.__currpoint) # calculates the distance between the
                                                                        # current and next point
                
                self.__distsum += self.__dist # adds the distance to distsum
                                                                                
                # gets the dot product of the next and current point
                self.__dotp = self.dotprod((self.nextpoint.getX, self.nextpoint.getY), (self.currpoint.getX, self.currpoint.getY))
                # gets the magnitude of the next and current point
                self.__mag = self.magnitude((self.nextpoint.getX, self.nextpoint.getY), (self.currpoint.getX, self.currpoint.getY))
                    
                # obtains the angle between the two points by running cosine inverse of the dot product
                # of the two vectors divided by the magnitude of the two vectors
                self.__angle = math.acos(self.__dotp / self.__mag)
                                                                          
            if self.__V.next == None: # if the traverser is on the last item
                self.__distsum += self.__V.distance(self.__head.next) # adds the distance between the last
                                                                      # and the first point to distsum
                                                                          
            # initializes prevdist and prevangle before first check on first point to prevent an error                                                          
            if self.__V == self.__head.next:
                self.__prevdist = self.__dist
                self.__prevangle = self.__angle
                    
            if self.__prevdist != self.__dist or self.__prevangle != self.__angle:
                self.__isregular = False
                    
            self.__V = self.__V.next # moves to the next item
            
        # if the polygon is regular, the perimeter is found by multiplying the distance of one
        # side by the amount of sides
        if self.__isregular == True:
            self.__perimeter = self.__dist*self.__sides
            return self.__perimeter
        # if the polygon is irregular, the perimeter is found by taking the sum
        # of all of the distances
        else:
            self.__perimeter = self.__distsum
            return self.__perimeter
            

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
import turtle

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

    (x, y) = S.split(", ") # gets the x and y coordinates by splitting them up between the comma

    # code below attempts to convert the x and y values gathered from a coordinate string to an int or float
    try:
        x = int(x)
    except:
        x = float(x)

    try:
        y = int(y)
    except:
        y = float(y)
    
    # returns x and y in a tuple
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
# will return false if any of the angles or side lengths are unequal with the one that came
# before them 
isregular = True

# an array to be made up of the distances between each successive pair of points 
# to be used in permimeter calculations if the polygon is not regular
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
    
    # distance between current and previous point is obtained and appended to distarr
    dist = pt1.distance(pt2)
    distarr.append(dist)
    
    # obtains the dot product of the current and previous point
    #print("distance:", dist)
    dotp = dotprod(pair1, pair2)
    #print("dot product:", dotp)
    # obtains the magnitude of the current and previous point
    mag2p = magnitude(pair1)*magnitude(pair2)
    #print("magnitude of both points:", mag2p)
    
    # obtains the angle between the two points by running cosine inverse of the dot product
    # of the two vectors divided by the magnitude of the two vectors
    angle = math.acos(dotp / mag2p)
    #print("angle in rads:", angle)
    
    # initializes prevdist and prevangle before first check on first point to prevent an error
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
    area = ((dist**2)*(sides)) / (4)*(math.tan(180/sides))
# if the polygon is irregular, the area is found using the process below
else:
    prod1 = 0
    prod2 = 0
    
    for ptnum in range(len(ptarr)): # goes through every coordinate in ptarr
        if ptnum != len(ptarr) - 1:
            vert1 = getNumeric(ptarr[ptnum]) # the current coordinate
            vert2 = getNumeric(ptarr[ptnum + 1]) # the coordinate after the current coordinate
            
            # multiplies the x value of the current point by the y value of the next coordinate
            # and adds it to the first sum of the products
            prod1 += vert1[0]*vert2[1]
            # multiplies the y value of the current point by the x value of the next coordinate
            # and adds it to the second sum of the products
            prod2 += vert1[1]*vert2[0]
        else:
            # when ptnum is on the last point, perform the algorithim above using the last and first
            # coordinates as the current and next coordinates
             vert1 = getNumeric(ptarr[ptnum])
             vert2 = getNumeric(ptarr[0])
             
             prod1 += vert1[0]*vert2[1]
             prod2 += vert1[1]*vert2[0]
             
    area = (prod1 - prod2) / 2
    
#print(area)
            
# below is code for displaying the polygon on Turtle     

# t = turtle.Turtle()
# turtle.bgcolor("white")
# turtle.tracer(0, 0)
# mult = 20
# 
# t.penup()
# 
# for ptnum in range(len(ptarr)):
#     # if the last point has not been reached, perform the below code
#     if ptnum != len(ptarr) - 1:
#         # first point corresponds to ptnum
#         pt1 = getNumeric(ptarr[ptnum])
#         # second point corresponds to ptnum + 1
#         pt2 = getNumeric(ptarr[ptnum + 1])
#         
#         # move plotter to the first point
#         t.goto(pt1[0]*mult, pt1[1]*mult)
#         # draws a line from the first point to the second point
#         t.pendown()
#         t.goto(pt2[0]*mult, pt2[1]*mult)
#     else:
#         # if the last point has been reached, draw a line from the
#         # last coordinate to the first coordinate
#         # same process as above
#         pt1 = getNumeric(ptarr[ptnum])
#         pt2 = getNumeric(ptarr[0])
#         
#         t.goto(pt1[0]*mult, pt1[1]*mult)
#         t.pendown()
#         t.goto(pt2[0]*mult, pt2[1]*mult)
#         # stops drawing
#         t.penup()
  
# TODO: Move algorithms for calculating area, calculating perimeter and turtle plotting to the Polygon object
# in progress
    
# driver ends here
