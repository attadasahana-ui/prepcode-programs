amount = float(input("enter order amount = "))
premium = input("premium membership ? ")

if amount>= 1000 and premium == "yes" :
    print("Free delivery")
else :
    print("No free delivery")