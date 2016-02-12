def eliminateDuplicates(lst):
    output = []
    seen = set()
    for value in lst:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
s = input("Enter ten numbers: ")
items = s.split() # Extracts items from the string
# Remove duplicates from this list.
lst = [ eval(x) for x in items ] # Convert items to numbers
result = eliminateDuplicates(lst)
print("The distinct numbers are : ", result)
