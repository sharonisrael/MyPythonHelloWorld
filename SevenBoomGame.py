
max_num = int(input("Please enter max number: "))

for i in range(1,max_num+1):
    # Can also do "7" in list(str(i))
    if i % 7 == 0 or "7" in str(i):
        print("Boom")
    else:
        print(f'Number is {i}')



