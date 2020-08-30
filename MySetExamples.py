drinks = { "coffee", "tea", "juice" }

if "tea" in drinks:
    print("In")
else:
    print("Out")


food_map = {
    "pizza" : 20,
    "burger" : 30}

print(food_map)
print(food_map["burger"])

for i in food_map:
    print(i, " = ", food_map[i])