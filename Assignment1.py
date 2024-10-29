# Irash Gilani
# 846852
# Assignment 1: Random Magic Squares

# Global Variable Dictionary
# primenumbers - an array made up of every prime number between 5 and 19
# inputprime - a boolean that returns true if the user inputs a value that is found in primenumbers
# N - the value that the user inputs
# squarearr1 - the first array, made up of values ranging from 1 to N
# squarearr2 - the second array, made up of values ranging from 0*N to (N-1)*N
# shiftmat1 - a matrix of dimensions NxN made up of squarearr1 with its values shifted by three left every row
# shiftmat2 - a matrix of dimensions NxN made up of squarearr2 with its values shifted by two left
# matsum - a 2D matrix made up of the sums of the values in shiftmat1 and shiftmat2
# rownum - the amount of rows in a matrix
# colnum - the amount of columns in a matrix

# a function that takes a 1D matrix of length N and makes a 2D array of
# dimensions N by N with every row shifted by a defined value
def matshift(matrix, shiftval):
  shiftmat = []
  shiftby = 0
  
  for rownum in range(len(matrix)):
    shiftedvalarr = []
    for val in range(len(matrix)):
      shiftedval = 0
      shift = (val + shiftby) % (len(matrix))
      shiftedval = matrix[shift]
      shiftedvalarr.append(shiftedval)
    shiftmat.append(shiftedvalarr)
      
    shiftby += shiftval
    
  return shiftmat
  
# a function that takes in two 2D matrixes of the same dimensions 
# and returns a matrix made up of the sums of their values
def addM(M1, M2):
    sumarr = []
    for rownum in range(len(M1)):
      sumarr.append([0] * len(M1[0]))
    
    for rownum in range(len(M1)):
      for columnnum in range(len(M1[0])):
        sumarr[rownum][columnnum] = (M1[rownum][columnnum] + M2[rownum][columnnum])
    
    return sumarr
    
# compares the sums of rows, columns and both diagonals of a 2D array to see 
# if it is magic
def isMagic(squarearr):
    
      squareismagic = True
      sum = 0
      tempsum = 0
      
      # checking rows
      for rownum in range(len(squarearr)):
        
        tempsum = 0
        
        for columnnum in range(len(squarearr[0])):
          if rownum == 0:
            sum += squarearr[rownum][columnnum]
          tempsum += squarearr[rownum][columnnum]
        
        if tempsum != sum:
          squareismagic = False
        
      #checking columns
      sum = 0
      
      for columnnum in range(len(squarearr[0])):
        
        tempsum = 0
        
        for rownum in range(len(squarearr)):
          if columnnum == 0:
            sum += squarearr[rownum][columnnum]
          tempsum += squarearr[rownum][columnnum]
          
        if tempsum != sum:
          squareismagic = False
          
      # checking diagonals
      
      LtoRsum = 0
      RtoLsum = 0
      
      # retrieves diagonal count from left to right
      for diagcount in range(len(squarearr)):
        
        LtoRsum += squarearr[diagcount][diagcount]
        
      # retrieves diagonal count from right to left, then compares with first count
      for diagcount in range(len(squarearr) - 1, -1, -1):
        RtoLsum += squarearr[diagcount][diagcount]
        
      if LtoRsum != RtoLsum:
        squareismagic = False
        
      if squareismagic == True:
        return ("The square is magic, with a magic number of %d." % sum)
      else:
        return "square is not magic"

primenumbers = [5, 7, 11, 13, 17, 19]
inputprime = False
N = 0

# check if input is a prime number between or equal to 5 and 19
while not inputprime:
  N = int(input("Input a prime number between 5 and 19: "))
  if N in primenumbers:
    inputprime = True
  else:
    print("Input is outside of range")

# creates a square matrix with a length of N
squarearr1 = [0] * N

# goes through every value in squarearr1 and replaces them with values ranging from 1 to N
for i in range(len(squarearr1)):
  squarearr1[i] = i + 1
  
#creates a second square matrix with a length of N
squarearr2 = [0] * N

# goes through every value in squarearr2 and replaces them with values ranging from (0)(N) to (N-1)(N)
for i in range(len(squarearr2)):
  squarearr2[i] = i*N

# creates a 2D matrix out of the first array with each row shifted by 3
shiftmat1 = matshift(squarearr1, 3)
# creates a 2D matrix out of the second array with each row shifted by 3
shiftmat2 = matshift(squarearr2, 2)


matsum = addM(shiftmat1, shiftmat2)
print("The magic square is:")
for rownum in range(len(matsum)):
  for colnum in range(len(matsum[0])):
    print("%-3d" % matsum[rownum][colnum], end=" ")
  print()
  
print()

print(isMagic(matsum))
