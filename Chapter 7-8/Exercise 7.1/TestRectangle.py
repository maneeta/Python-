from Rectangle import Rectangle

def main():
    # Create a rectangle with width = 1 height = 2
    rectangle1 = Rectangle()
    print("The area of the rectangle of width", rectangle1.getWidth(), "and height", rectangle1.getHeight(), "is", rectangle1.getArea())
    print("The perimeter of the rectangle of width", rectangle1.getWidth(), "and height", rectangle1.getHeight(), "is", rectangle1.getPerimeter())
        
    # Create a rectangle with width = 4 and height = 40
    rectangle2 = Rectangle(4, 40)
    print("The area of the rectangle of width", rectangle2.getWidth(), "and height", rectangle2.getHeight(), "is", rectangle2.getArea())
    print("The perimeter of the rectangle of width", rectangle2.getWidth(), "and height", rectangle2.getHeight(), "is", rectangle2.getPerimeter())
        
    # Create a rectangle with width = 3.5 and height = 35.7
    rectangle3 = Rectangle(3.5, 35.7)
    print("The area of the rectangle of width", rectangle3.getWidth(), "and height", rectangle3.getHeight(), "is", rectangle3.getArea())
    print("The perimeter of the rectangle of width", rectangle3.getWidth(), "and height", rectangle3.getHeight(), "is", rectangle3.getPerimeter())

   
main() # Call the main function
