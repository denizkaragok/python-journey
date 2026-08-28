age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an adult.")
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
    print("You have met the target production.")
else:
    print("You have not met the target production.")

failrate = float(input("Please enter the failure rate (as a percentage): "))
if failrate >= 0 and failrate < 2:
    print("The failure rate is good.")
elif failrate >= 2 and failrate < 5:
    print("The failure rate is acceptable.")
elif failrate >= 5:
    print("The failure rate needs improvement.")

shift_number = int(input("Please enter the shift number (1, 2, or 3): "))
if shift_number == 1:
    print("You are on the morning shift.")
    production = int(input("Please enter the number of products produced in the morning shift: "))
    target = int(input("Please enter the target production for the morning shift: "))
    if production > target:
        print("You have exceeded the target production for the morning shift.")
    elif production == target:
        print("You have met the target production for the morning shift.")
    else:
        print("You have not met the target production for the morning shift.")
elif shift_number == 2:
    print("You are on the evening shift.")
    production = int(input("Please enter the number of products produced in the evening shift: "))
    target = int(input("Please enter the target production for the evening shift: "))
    if production > target:
        print("You have exceeded the target production for the evening shift.")
    elif production == target:
        print("You have met the target production for the evening shift.")
    else:
        print("You have not met the target production for the evening shift.")
elif shift_number == 3:
    print("You are on the night shift.")
    production = int(input("Please enter the number of products produced in the night shift: "))
    target = int(input("Please enter the target production for the night shift: "))
    if production > target:
        print("You have exceeded the target production for the night shift.")
    elif production == target:
        print("You have met the target production for the night shift.")
    else:
        print("You have not met the target production for the night shift.")
else:
    print("Invalid shift number. Please enter 1, 2, or 3.")
