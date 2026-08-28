age = int(input("Please enter your age: "))
if age >= 18:
    print("You are a adult.")
else:
    print("You are a minor.") 

number = int(input("Please enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

productionperday = int(input("Please enter the number of products produced in a day: "))
targetproduction = int(input("Please enter the target production: "))
if productionperday >targetproduction:
    print("You have exceeded the target production.")
elif productionperday == targetproduction:
    print("You havemet the target production.")
else:
    print("You have not met the target production.")

failrate = float(input("Please enter the failure rate (as a percentage): "))
if failrate 0 <= failrate < 2:
    print("The failure rate is good.")
elif failrate 2 <= failrate < 5:
    print("The failure rate is acceptable.")
elif failrate >= 5:
    print("The failure rate needs improvement.")
