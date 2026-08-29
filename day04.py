productions = [950 , 1100, 980, 1200, 1050]
for production in productions:
    if production < 1000:
        print(production)

shifts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for shift in range(2, 11, 2):
    print("Shift", shift, "is being analyzed")

production = 0

while production < 10:
    production += 1
    print("Production:",production)

current_production = 0

while current_production < 100:
    current_production += 10
    print("Current production:", current_production)


target_production = 0

while target_production < 1000:
    target_production += 100
    if target_production == 500:
        print("Halfway to target production!")
    elif target_production == 1000:
        print("Target production reached!")
    print("Target production:", target_production)

prdctn = 0
while prdctn < 1000:
    user_input_production = int(input("Enter a production value: "))
    prdctn += user_input_production
    print("Current production:", prdctn)
    if prdctn >= 1000:
        print("Target production reached!")
