from math import sqrt
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self,length,width):
        A = length * width
        return A
    def perimeter(self,length,width):
        P = 2 * (length + width)
        return P
    def diadonal_length(self,length,width):
        d_length = sqrt((length **2) + (width **2))
        return d_length


plot = Rectangle(40, 30)


        