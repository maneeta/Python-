from TriangleFromGeometricObject import Triangle

def main():
    side1, side2, side3 = eval(input("Enter three sides : "))
    triangle = Triangle(side1, side2, side3);

    color = input("Enter color : ")
    triangle.setColor(color);

    filled = eval(input("Enter 1/0 for filled (1: true, 0: false) : "))

    isFilled = (filled == 1)
    triangle.setFilled(isFilled);

    print("The area is", triangle.getArea())
    print("The perimeter is", triangle.getPerimeter())
    print("Color is", color)
    print("Filled is", triangle.isFilled())

main() # Call the main function
