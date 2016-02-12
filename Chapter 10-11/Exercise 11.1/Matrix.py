def main():
    matrix = []
    
    for i in range(3):
        s = input("Enter a 3-by-4 matrix row for row " + str(i) + ": ") 
        items = s.split() # Extracts items from the string
        list = [ eval(x) for x in items ] # Convert items to numbers   
        matrix.append(list)
    print(matrix)        
    for column in range(0,4):
        print ("sum of the elements for column " ,column ,"is", sum(row[column] for row in matrix))
       
main()
