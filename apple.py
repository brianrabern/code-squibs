def apple_sum_total(input):
    tot = 0
    for item in input:
        tot += item["total"]*item["cost"]
    return tot




# Has an output of 0
apples1 = []

# Has an output of 1
apples2 = [
    {"total": 1, "cost": 1}
]

# Has an output of 7.35
apples3 = [
    {"total": 10.5, "cost": .70}
]

# Has an output of 24.05
apples4 = [
    {"total": 22, "cost": .15},
    {"total": 0, "cost": 8},
    {"total": 50, "cost": .25},
    {"total": 15, "cost": .55}
]

print(apple_sum_total(apples1))
print(apple_sum_total(apples2))
print(apple_sum_total(apples3))
print(apple_sum_total(apples4))
