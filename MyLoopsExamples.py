allAges = [25, 66, 44, 23, 67]

print("All")
for arg in allAges:
    print(arg)

print("Partial")
for arg in allAges[2:5]:
    print(arg)

print("Up to 10")
for i in range(10):
    print(i)

# This good if you don't want 0...n-1
print("10 to 50")
for i in range(10,50,10) :
    print(i)

