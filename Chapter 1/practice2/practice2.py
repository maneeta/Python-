
name = input("Enter employee's name : ")
hoursWorked = eval(input("Enter number of hours worked in a week : "))
ratePerHour = eval(input("Enter hourly pay rate : "))
federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate : "))
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate : "))

#compute
grossPay = hoursWorked * ratePerHour
federalTax = grossPay * federalTaxWithholdingRate
stateTax = grossPay * stateTaxWithholdingRate
totalDeduction = federalTax + stateTax
netPay = grossPay - totalDeduction

#print
print("Employee Name : "+ name + "\n\n")
print("Hours Worked : " + str(hoursWorked) + '\n')
print("Pay Rate : $" + str(ratePerHour) + '\n')
print("Gross Pay : $" + str(grossPay ) + '\n')
print("Deductions : \n ")
print("\tFederal Withholding (" + str(federalTaxWithholdingRate * 100) + "%) : $" + str(int(federalTax *100)/100.0) + '\n')
print("\tState Withholding (" + str(stateTaxWithholdingRate * 100) + "%) : $" + str(int(stateTax * 100)/100.0) + '\n')
print("\tTotal Deduction : $" + str((int(totalDeduction * 100)/100.0)) + '\n')
print("Net Pay:$" + str(int(netPay * 100)/100.0) + '\n')
