print("Kilograms\t", "Pounds")
print("--------------------------------")
for number in range(1, 200, 2):
    print(format(number, "<10d"),                 format((number*2.2),"10.2f"))
