#prompt

subtotal =eval(input("Enter subtotal : "))
gratuityRate = eval(input("Enter gratuity rate : "))

#compute
gratuity = (subtotal*gratuityRate)/100.0
total = subtotal + gratuity

print("The gratuity is", int(gratuity*100)/100.0, "and the total is", int(total*100)/100.0)
