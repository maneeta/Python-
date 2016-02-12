count = 0
isLeapYear = False
for year in range(2001,2100):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        isLeapYear = True
        count  += 1
        print(year, end=' ')
        if count%10==0:
            print()
        
year += 1
