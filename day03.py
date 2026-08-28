production = int(input("Please enter the number of products produced in the shift: "))

target = int(input("Please enter the target production for the shift: "))

failure_rate = float(input("Please enter the failure rate (as a percentage) for the shift: "))

machine_status = input("Is the machine operational? (True/False): ")

if production >= target and failure_rate < 3:

    print("Machine performing well")

elif failure_rate > 5 or machine_status == "False":

    print("Process needs immediate attention")

else:

    print("Process is acceptable")
