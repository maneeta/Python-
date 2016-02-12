import random

def printMatrix(n):
   matrix = []
   rows = columns = n
   if rows == 1 and columns == 1:
      print(random.randint(0,1)) 
   elif rows == 2 and columns == 2:
      print(random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1))  
   elif rows == 3 and columns == 3:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1))
   elif rows == 4 and columns == 4:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
   elif rows == 5 and columns == 5:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
   elif rows == 6 and columns == 6:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
   elif rows == 7 and columns == 7:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
   elif rows == 8 and columns == 8:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))

   elif rows == 9 and columns == 9:
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
      print(random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
   else:
      print("Enter single digit number")
       
   return matrix
def main():
    n = eval(input("Enter n : "))
    printMatrix(n)
main()
