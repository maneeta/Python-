print("Feet           Meters      |     Meters          Feet" )
print("------------------------------------------------------------")

def footToMeter(foot):
    return foot * 0.305

for foot in range(1,11):
        print(foot, "\t", format(footToMeter(foot), "10.2f"),"\t   |")
   
print()
def meterToFoot(meter):
    return meter / 0.305

for meter in range(20,66,5):
        print("\t\t\t\t", meter, "\t", format(meterToFoot(meter), "10.2f"))
