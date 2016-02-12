#prompt
number = eval(input("Enter an integer : "))

num1 = number % 10
number = number // 10

num2 = number % 10
number = number // 10

num3 = number % 10
number = number // 10

num4 = number % 10
number = number // 10

print("The reversed number is " + str(num1) + str(num2) + str(num3) + str(num4))
