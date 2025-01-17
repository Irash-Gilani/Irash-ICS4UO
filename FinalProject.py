# polynomial.py starts here

# Irash Gilani
# 846852
# Polynomial Object for the Final Project

# Variable Dictionary:
# self.__coeffs - an array consisting of the coefficients of a polynomial, with the leading
# zeroes removed
# self.__pastleading zeroes - a boolean that checks for whether or not the leading zeroes
# have been passed while a loop goes through an inputted array to append coefficents to
# self.__coeffs 
# idx - a step value for going through the inputted array in a loop
# exp - a step value for going backwards through self.__coeffs, representing
# the value of the current exponent
# self.__y - a float value returned from calculating f(x)
# self.__exponent - an integer that is increased by one on every step of the loop
# going through self.__coeffs during the calculation of f(x), whenever the step
# is not on the second last value of self.__coeffs
# self.__index - an integer that is increased by one along with exp during the
# filling of self.__polystring
# self.__polystring - a string that contains the polynomial consisting of its
# coefficients and exponent values in proper format to be printed


class Polynomial:
    def __init__(self, coefficients):
        # the input variable "coefficients" is an array
        # the coefficients are assumed to be in standard form 
        self.__coeffs = []
        
        # the code below is for ignoring the leading zeroes in the input list,
        # then appending the rest of the numbers to self.__coeffs
        self.__pastleadingzeroes = False
        
        for idx in range(len(coefficients)):
            if coefficients[idx] != 0:
                self.__pastleadingzeroes = True
            if self.__pastleadingzeroes == True:
                self.__coeffs.append(coefficients[idx])
                
    def get_order(self):
    # a function for getting the order of the polynomial
        
        if (len(self.__coeffs) - 1) == -1:
            # if the length of the coefficients array minus 1 is -1, than there
            # are no coefficients or exponents, leading to an order of 0
            return 0
            
        for exp in range(len(self.__coeffs) - 1, -1, -1):
        # goes backwards through self.__coeffs to find the exponent of the first variable
            if exp == len(self.__coeffs) - 1:
                return exp
            
        
    def f(self, x):
    # a function for getting the value of y using the polynomial and an
    # inputted x value 
        self.__y = 0
        self.__exponent = 0
        
        for idx in range(len(self.__coeffs) - 1, -1, -1):
            # a for loop that goes from the last coefficient in self.__coeffs
            # to the first coefficient
            
            if idx == len(self.__coeffs) - 1:
                # if the loop is on the second last coefficient in self.__coeffs,
                # add the coefficient times x without an exponent
                self.__y += self.__coeffs[idx] * x
            else:
                # if the loop is on any other number, the exponent is increased by one
                # with every step, and is 
                self.__exponent += 1
                self.__y += (self.__coeffs[idx]) * x**self.__exponent
        
        return self.__y
                
                
    
    def __str__(self):
        # a function for printing the polynomial including its exponents
        self.__polystring = ""
        self.__index = 0
        
        for exp in range(len(self.__coeffs) - 1, -1, -1):
            # goes backwards through self.__coeffs, using the step value as the exponent and increasing
            # self.__index by one with each step, and adding each value in the polynomial according to
            # their exponent and index values
            
            self.__polystring += str(self.__coeffs[self.__index])
            self.__polystring += "x^"
            self.__polystring += str(exp)
            # adds "(coefficient)x^(exponent)" to self.__polystring
            
            self.__index += 1
            
            
            if exp != 0:
                self.__polystring += " + "
                # adds a plus sign if the loop is not on the last value in self.__coeffs
        
        if self.__polystring == "":
            self.__polystring = "0"
        
        return self.__polystring
                
                
            
        
# polynomial.py ends here

# IVT.py starts here

# Irash Gilani
# 846852
# IVT Object for the Final Project

# Variable Dictionary:
# self.__poly - A Polynomial object that is inputted when
# the IVT object is called
# self.__x1 - the first x value as an inputted float or integer that supposedly has
# the zero in between it and x2
# self.__x2 - the second x value as an inputted float or integer that supposedly has
# the zero in between it and x1
# self.__zerofound - a boolean that is always False until the IVT algorithm returns an
# x intercept or a string informing the user that there is no zero between the inputted
# x values

# between self.__x1 and self.__x2 and returns True if both checks are successful,
# letting the IVT algorithm commence
# self.__y1 - a float representing f(self.__x1)
# self.__y2 - a float representing f(self.__x2)
# self.__x0 - the average of self.__x1 and self.__x2, which is to be checked
# if it is sufficiently close to zero


#from polynomial import Polynomial

class IVT():
# an object for approximating the zeroes of a polynomial using
# two x values and a Polynomial object


    def __init__(self, Poly):
        # Poly is a Polynomial object
        
        self.__poly = Poly
        
    def findZero(self, x1, x2):
        
        
        self.__x1 = x1
        self.__x2 = x2
        self.__zerofound = False
        self.__xunequal = False
        self.__xopposite = False
        self.__prevx0 = 0
    
        while self.__zerofound == False:
            # a while loop that will always run until a value is returned
            
            # below code is for checking if the preconditions are met
            if self.__x1 == self.__x2:
            # x1 and x2 are equal, only check if f(x1) = 0 to find
            # a zero
                if Polynomial.f(self.__poly, self.__x1) == 0:
                    return self.__x1
            
            elif self.__x1 != self.__x2:
                #print("unequal")
                self.__xunequal = True
            # first precondition is whether or not x1 is unequal to x2
            # if the first precondition is true, move on to the next precondition
            
                self.__y1 = Polynomial.f(self.__poly, self.__x1)
                self.__y2 = Polynomial.f(self.__poly, self.__x2)
                # the values of f(x1) and f(x2) are initialized
                
                if ((self.__y1 > 0 and self.__y2 < 0) or (self.__y1 < 0 and self.__y2 > 0)):
                    #print("opposite")
                # second precondition is whether or not the sign of f(x1) is the opposite of the sign of f(x2),
                # this is checked by looking at whether or not one variable is smaller than zero while the
                # other is bigger than zero
                    self.__xopposite = True

                    
            self.__x0 = (self.__x1 + self.__x2) / 2
            print("(%f + %f) / 2 = %f" % (self.__x1, self.__x2, self.__x0))
            print("x0 =", self.__x0, "x1 =", self.__x1, "x2 =", self.__x2)
                    
            if self.__xopposite and self.__xunequal == False:
                # if neither of the preconditions are not met, it is assumed that no solution exists
                return ("There is no solution between %.2f and %.2f" % (self.__x1, self.__x2))
            elif self.__xopposite == False and self.__xunequal == True:
                # if the two x values are unequal but with the same sign in y,
                # the line of the graph could be bouncing off of the x axis to form a zero,
                # instead of passing through
                
                print(self.__prevx0, self.__x0)
                
                # TODO fix how the value of prevx0 is always eventaully many more decimal places than x0,
                # despite pretty much being the same number, when x1 and x2 average into a max/min
                
                if self.__x0 == self.__prevx0:
                    # if the current value of x0 is the same as the previous value of x0, then
                    # the algorithim is looping infinitely, meaning that there is no x intercept
                    return ("There is no solution between %.2f and %.2f" % (self.__x1, self.__x2))
                
                while (self.__x1 < self.__x0 < self.__x2):
                    if round(Polynomial.f(self.__poly, self.__x0), 3) == 0.000:
                            # if f(x0) is sufficiently close enough to zero, to the point where it 
                            # can be rounded down to 0.000, than x0 will be returned
                            return self.__x0
                    elif self.__x0 > 0:
                        # if f(x0) does not sufficiently round to zero, and is larger than 0, it
                        # is assumed that the zero is inbetween x1 and x0
                        self.__prevx0 = self.__x0
                        self.__x2 = self.__x0
                        #print("x2 = x0")
                        # the value of x0 is assigned to x2, breaking the inner while loop above
                    elif self.__x0 < 0:
                        # if f(x0) does not sufficiently round to zero, and is smaller than 0, it
                        # is assumed that the zero is inbetween x0 and x2
                        self.__prevx0 = self.__x0
                        self.__x1 = self.__x0
                        #print("x1 = x0")
                        # the value of x1 is assigned to x0, breaking the inner while loop above
                        # and restarting the algorithm with a new x1 value
            
                    
            else:
                # if both of the preconditions are met, the average of x1 and x2 is found
                #self.__x0 = (self.__x1 + self.__x2) / 2
                
                
                if Polynomial.f(self.__poly, self.__x1) < Polynomial.f(self.__poly, self.__x2):
                    while (self.__x1 < self.__x0 < self.__x2):
                        #print("f(x0) =", Polynomial.f(self.__poly, self.__x0))
                        #print("rounded", round(Polynomial.f(self.__poly, self.__x0), 3))
                        if round(Polynomial.f(self.__poly, self.__x0), 3) == 0.000:
                            # if f(x0) is sufficiently close enough to zero, to the point where it 
                            # can be rounded down to 0.000, than x0 will be returned
                            return self.__x0
                        elif Polynomial.f(self.__poly, self.__x0) < 0:
                            # if f(x0) does not sufficiently round to zero, and is smaller than 0, it
                            # is assumed that the zero is inbetween x0 and x2
                            self.__x1 = self.__x0
                            #print("x1 = x0")
                            # the value of x1 is assigned to x0, breaking the inner while loop above
                            # and restarting the algorithm with a new x1 value
                        elif Polynomial.f(self.__poly, self.__x0) > 0:
                            # if f(x0) does not sufficiently round to zero, and is larger than 0, it
                            # is assumed that the zero is inbetween x1 and x0
                            self.__x2 = self.__x0
                            #print("x2 = x0")
                            # the value of x0 is assigned to x2, breaking the inner while loop above
                else:
                # if f(x1) is bigger than f(x2), perform the same operation as above but with all of the
                # < and > checks reversed
                    while (self.__x1 < self.__x0 < self.__x2):
                        if round(Polynomial.f(self.__poly, self.__x0), 3) == 0.000:
                            # if f(x0) is sufficiently close enough to zero, to the point where it 
                            # can be rounded down to 0.000, than x0 will be returned
                            return self.__x0
                        elif Polynomial.f(self.__poly, self.__x0) > 0:
                            # if f(x0) does not sufficiently round to zero, and is larger than 0, it
                            # is assumed that the zero is inbetween x0 and x2
                            self.__x1 = self.__x0
                            #print("x1 = x0")
                            # the value of x1 is assigned to x0, breaking the inner while loop above
                            # and restarting the algorithm with a new x1 value
                        elif Polynomial.f(self.__poly, self.__x0) < 0:
                            # if f(x0) does not sufficiently round to zero, and is smaller than 0, it
                            # is assumed that the zero is inbetween x1 and x0
                            self.__x2 = self.__x0
                            #print("x2 = x0")
                            # the value of x0 is assigned to x2, breaking the inner while loop above
                    
                
                
                
                
                    
    
                    

        

# IVT.py ends here

# polynomial driver starts here

# Irash Gilani
# 846852
# Driver Code for the Polynomial Object in the Final Project

# Variable Dictionary:
# P - A Polynomial object


#from polynomial import Polynomial

# P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([0, 0, 0, 0, 0, 0, 0, 0])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([9, 9, 9, 9, 9, 9, 9, 9])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([0, 1, 2, 3, 4, 5, 6, 7])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([-8, -7, -6, -5, -4, -3, -2, -1])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([8.57, 6.65, 5.5, 4.65, 3.65, 2.65, -1.54, 0.5426])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())
# 
# P = Polynomial([3, 2, 1])
# print(P)
# for i in range(10):
#  print(i, P.f(i))
# print("The order is", P.get_order())




# polynomial driver ends here

# ivtdriver.py starts here


# Irash Gilani
# 846852
# Driver Code for the IVT Object in the Final Project

# Variable Dictionary:
# P - A Polynomial object
# zero - an IVT object, for getting the x intercept
# of the Polynomial object


#from IVT import IVT

P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])

#P = Polynomial([-5, 1, 0, 7, 0, 5, 2, 2])

#P = Polynomial([0, 1, 0, 2, 3, 0, 0, 0])

#P = Polynomial([-5, 0, 2, 1, 0, 0])

#P = Polynomial([2, 0, 5, 2, 0, 0,])

print(P)

zero = IVT(P)

print(zero.findZero(-2.2, -1))
#print(zero.findZero(0, 0))
#print(zero.findZero(-999999999999999, 99999999999999999999))

# ivtdriver.py ends here
