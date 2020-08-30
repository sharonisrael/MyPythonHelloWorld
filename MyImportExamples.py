import random
import MyFuncExamples
import this


MyFuncExamples.first_func()

print("random")
x = random.randrange(1, 1000)
print(x)

names = ["sharon", "tali", "Shahar", "Dana"]

random_name = names[random.randint(0, len(names) - 1)]
print(f"Selected name is {random_name}")

print("Selected name : %s" % random_name)