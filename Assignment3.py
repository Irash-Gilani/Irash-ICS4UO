# poly.py starts here

# Irash Gilani
# 846852
# Polygon Object for Assignment 3

# Variable Dictionary:
# self.__x - the x coordinate of a point object, in float form
# self.__y - the y coordinate of a point object, in float form
# self.__next - the pointer on a point object
# self.__sides - the amount of sides in the polygon
# self.__vertices - the amount of vertices in the polygon
# self.__head - a point with null value, which is meant to point at the first point in a polygon
# self.__isregular - a boolean that indicates whether or not a polygon is regular
# self.__distsum - the sum of all side lengths in a polygon
# V - a global point object that is used for adding a point to the linked list of points
# vecA - one of the two vectors used in the algorithm for getting the dot product between two vectors
# vecB - the other of the two vectors used in the algorithm for getting the dot product between two vectors
# self.__product - the dot product of two vectors
# matrix - a matrix that is inputted into the function for getting the magnitude of a matrix
# self.__mag - the magnitude of a matrix
# val - an item in a matrix
# self.__area - the area of the polygon
# self.__currpoint - the point that the list traverser is currently on
# self.__nextpoint - the point after the current point the list traverser is on
# self.__dist - the distance between two points
# self.__dotp - the dot product of two coordinates
# self.__mag2p - the product of two coordinates' magnitudes multiplied together
# self.__angle - the internal angle between two points
# self.__vert1 - a coordinate used in the algorithm for calculating the area of an irregular polygon
# self.__vert2 - a coordinate that comes after vert1, used for calculating the area of an irregular polygon
# self.__prod1 - the sum of the products of x coordinates multiplied by the next y coordinates
# self.__prod2 - the sum of the products of y coordinates multiplied by the next x coordinates
# self.__perimeter - the perimeter of the polygon
# self.__t - a variable used for calling Turtle
# self.__mult - a value that the x and y coordinates of two points on Turtle are multiplied by to make the shape larger and easier to see
# self.__pt1 - a point on the Turtle display that the drawer moves from
# self.__pt2 - a point on the Turtle display that the drawer moves towards
# self.__linkedliststr - a string that contains all of the coordinates in the linked list separated by arrows


import math
import turtle

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
    
    # a function for getting the boolean value of whether or not the polygon is regular
    # if getRegular returns True, then the polygon is regular
    # if it returns False, the polygon is irregular
    def getRegular(self):
        self.__distsum = 0
        self.__V = self.__head.next # sets the list traverser to the first item in the linked list
        # traverses the linked list to gather the sum of all distances
        while self.__V != None: # loop continues until the pointer leads to a null value
            self.__currpoint = self.__V
            if self.__V.next != None: # performs below code if the next item is not null
                self.__nextpoint = self.__V.next
                
                self.__dist = self.__nextpoint.distance(self.__currpoint) # calculates the distance between the
                                                                          # current and next point
            
                self.__distsum += self.__dist # adds the distance to distsum
                                                                            
                                                                            
                # gets the dot product of the next and current point
                self.__dotp = self.dotprod((self.__nextpoint.getX(), self.__nextpoint.getY()), (self.__currpoint.getX(), self.__currpoint.getY()))
                # gets the magnitude of the next and current point
                self.__mag2p = self.magnitude((self.__nextpoint.getX(), self.__nextpoint.getY())) * self.magnitude((self.__currpoint.getX(), self.__currpoint.getY()))
                
                # obtains the angle between the two points by running cosine inverse of the dot product
                # of the two vectors divided by the magnitude of the two vectors
                if self.__dotp and self.__mag2p != 0:
                    self.__angle = math.acos(self.__dotp / self.__mag2p)
                else:
                    self.__angle = 90
                                                                      
            if self.__V.next == None: # if the traverser is on the last item
                self.__distsum += self.__V.distance(self.__head.next) # adds the distance between the last
                                                                      # and the first point to distsum
                                                                      
            # initializes prevdist and prevangle before the check on first point to prevent an error                                                          
            if self.__V == self.__head.next:
                self.__prevdist = self.__dist
                self.__prevangle = self.__angle
            
            # if any of the angles or side lengths are unequal with each other, the polygon is irregular
            if self.__prevdist != self.__dist or self.__prevangle != self.__angle:
                self.__isregular = False
                
            self.__V = self.__V.next # moves to the next item
            
        return self.__isregular
    
    def area(self):
        self.__area = 0
        
        # below code makes a calculation for area depending on whether or not the polygon is regular
        # if the polygon is regular, the area is found using the formula below
        
        if self.getRegular() == True:
            self.__area = ((self.__dist**2)*(self.__sides)) / (4)*(math.tan(180/self.__sides))
            
            return self.__area
        # if the polygon is irregular, the area is found using the process below
        else:
            self.__prod1 = 0
            self.__prod2 = 0
            #traverse the linked list
            self.__V = self.__head.next # sets the list traverser to the first item in the linked list
            
            
            while self.__V.next != None: # loop continues until the pointer leads to a null value
                self.__vert1 = (self.__V.getX(), self.__V.getY()) # the current coordinate
                self.__vert2 = (self.__V.next.getX(), self.__V.next.getY()) # the coordinate after the current coordinate
                
                # multiplies the x value of the current point by the y value of the next coordinate
                # and adds it to the first sum of the products
                self.__prod1 += self.__vert1[0]*self.__vert2[1]
                
                # multiplies the y value of the current point by the x value of the next coordinate
                # and adds it to the second sum of the products
                self.__prod2 += self.__vert1[1]*self.__vert2[0]
                
                self.__V = self.__V.next # moves to the next item
                
            if self.__V.next == None:
                # when the traverser is on the last coordinate, perform the algorithim
                # above using the last and first coordinates as the current and next coordinates
                self.__vert1 = (self.__V.getX(), self.__V.getY())
                self.__vert2 = (self.__head.next.getX(), self.__head.next.getY())
                
                self.__prod1 += self.__vert1[0]*self.__vert2[1]
                self.__prod2 += self.__vert1[1]*self.__vert2[0]
                 
            self.__area = (self.__prod1 - self.__prod2) / 2
            
            return self.__area
            
    def perimeter(self):
        self.__perimeter = 0
          
        # if the polygon is regular, the perimeter is found by multiplying the distance of one
        # side by the amount of sides
        if self.getRegular() == True:
            self.__perimeter = self.__dist*self.__sides
            return self.__perimeter
        # if the polygon is irregular, the perimeter is found by taking the sum
        # of all of the distances
        else:
            self.__perimeter = self.__distsum
            return self.__perimeter
            
            
    def draw(self):
        self.__t = turtle.Turtle()
        turtle.bgcolor("white")
        turtle.tracer(0, 0)
        self.__mult = 20

        self.__t.penup()
        
        self.__V = self.__head.next # sets the list traverser to the first item in the linked list
        
        while self.__V != None:
            # if the last point has not been reached, perform the below code
            if self.__V.next != None:
                #point one
                self.__pt1 = (self.__V.getX(), self.__V.getY())
                #point two
                self.__pt2 = (self.__V.next.getX(), self.__V.next.getY())
                
                # move plotter to the first point
                self.__t.goto(self.__pt1[0]*self.__mult, self.__pt1[1]*self.__mult)
                # draws a line from the first point to the second point
                self.__t.pendown()
                self.__t.goto(self.__pt2[0]*self.__mult, self.__pt2[1]*self.__mult)
                
                
                self.__V = self.__V.next
            else:
                # if the last point has been reached, draw a line from the
                # last coordinate to the first coordinate using the
                # same process as above
                
                #point one
                self.__pt1 = (self.__V.getX(), self.__V.getY())
                #point two
                self.__pt2 = (self.__head.next.getX(), self.__head.next.getY())
                
                # move plotter to the first point
                self.__t.goto(self.__pt1[0]*self.__mult, self.__pt1[1]*self.__mult)
                # draws a line from the first point to the second point
                self.__t.pendown()
                self.__t.goto(self.__pt2[0]*self.__mult, self.__pt2[1]*self.__mult)

                self.__t.penup() # stops drawing
                
                self.__V = self.__V.next # ends the while loop
        turtle.update()
        

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
# Driver for the Polygon Program

# Variable Dictionary;
# S - The string fed into GetNumeric to return an x and y coordinate
# x - The x coordinate taken from splitting S, and the x coordinate taken from splitting p
# y - The y coordinate taken from splitting S, and the y coordinate taken from splitting p
# polydata - The first line of text from a2, containing all of the coordinates
# ptarr - an array containing all of the point objects made from processing polydata
# p - a coordinate in polydata that has had its brackets removed
# pt - a point object created from the x and y values taken from p
# poly - a polygon object
# pair - a pair of x and y coordinates in tuple form taken from processing a point through getNumeric



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

if Poly.getRegular() == True:
    print("Polygon is regular.")
else:
    print("Polgon is irregular.")

print("Perimeter = %.2f" % Poly.perimeter()) # prints the perimeter
           
print("Area = %.2f" % Poly.area()) # prints the area

Poly.draw() # displays the polygon on Turtle
    
# driver ends here
