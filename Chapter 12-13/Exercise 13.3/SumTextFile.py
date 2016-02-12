def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    # Open files for input 
    infile = open(f1, "r")
    
    s = infile.read() # Read all from the file
    numbers = [eval(x) for x in s.split()]
    print("There are", len(numbers), "scores")
    print("The total is", sum(numbers))
    print("The average is", sum(numbers)/len(numbers))

             
    infile.close() # Close the output file

main()
