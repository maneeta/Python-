from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3)/2
        return (s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3))**0.5
  
    def getPerimeter(self):
        return (self.__side1 + self.__side2 + self.__side3)

    def printTriangle(self):
        print(self.__str__() + " side1: " + str(self.__side1))
        print(self.__str__() + " side2: " + str(self.__side2))
        print(self.__str__() + " side3: " + str(self.__side3))

