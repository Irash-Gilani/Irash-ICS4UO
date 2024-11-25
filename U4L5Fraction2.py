from Fraction import Fraction

class Fraction2(Fraction):
  def __init__(self, num, den):
    Fraction.__init__(self, num, den)
  
  def check(self):
    if self.getDen() == 0:
      return ("Error: The denominator is zero.")
    else:
      return ("Valid: The denominator is not zero.")
      
  def unreduce(self, unint):
    multnum = self.getNum() * unint
    multden = self.getDen() * unint
    
    self.__n = multnum
    self.__d = multden
    
    return "{0}/{1}".format(self.__n, self.__d)
    
  def mult(self, g):
      f3num = self.getNum() * g.getNum()
      f3den = self.getDen() * g.getDen()
      
      result = "{0}/{1}".format(f3num, f3den)
      
      return result
  
  def sum(self, g):
    f1 = Fraction2(self.getNum(), self.getDen())
    f2 = Fraction2(g.getNum(), g.getDen())
    
    f3num = (f1.getNum() * f2.getDen()) + (f2.getNum() * f1.getDen())
    f3den = (f1.getDen() * f2.getDen())
    
    return Fraction2(f3num, f3den)
