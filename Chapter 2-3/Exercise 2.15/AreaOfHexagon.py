#Enter the length of the side of hexagon
s = eval(input("Enter the legth of the side : "))

#Compute the area of hexagon
area = 3 * (3 ** 0.5)/2 * s * s
print("The area of the hexagon is", int(area * 100)/100.0)
