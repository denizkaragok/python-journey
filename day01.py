production = 800
workingtime = 8
workers = 4
print("Production:", production)
print("Working time:", workingtime)
print("Workers:",workers)
productionperhour = production / workingtime
print(productionperhour)
productionperworker = production / workers
print(productionperworker)
onehourproductionforperworker = production / (workers * workingtime)
print("1 işçi 1 saatte bunu üretebiliyor:",onehourproductionforperworker)

                                             