def computeCommission(salesAmount):
    if salesAmount <= 5000:
        commission =  salesAmount * 0.08
    elif (salesAmount >= 5000) or (salesAmount <= 10000):
        commission = (5000 * 0.08)+((salesAmount - 5000)*0.10)
    elif salesAmount > 10000:
        commission = (5000 * 0.08)+ (10000 * 0.10) + (salesAmount * 0.12)

    return commission

def main():
    print("salesAmount\t    Commmission")
    for  salesAmount in range(10000,101000,5000):
        print(salesAmount, "\t\t",format(computeCommission(salesAmount),"10.2f"))
        
main()
