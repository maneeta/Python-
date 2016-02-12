def main():
    # Read numbers as a string from the console
    s = input("Enter scores : ")
    items = s.split() # Extract items from the string
    score = [eval(x) for x in items] # Convert items to numbers
    best = max(score)
    #print(best)
    
    for i in range(0,len(score)):
        #print(score[i])
        if score[i] >= (best-10):
            print("Student", i, "score is ", score[i], "and grade is A")
        elif score[i] >= (best-20):
            print("Student", i, "score is ", score[i], "and grade is B")
        elif score[i] >= (best-30):
            print("Student", i, "score is ", score[i], "and grade is C")
        elif score[i] >= (best-40):
            print("Student", i, "score is ", score[i], "and grade is D")
        else:
            print("invalid")  
main()  
