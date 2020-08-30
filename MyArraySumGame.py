
my_list = []

user_input = 0

while (user_input != -1):
    print("Please enter number")
    user_input_str = input()

    try:
        user_input = int(user_input_str)
    except ValueError:
        print("Illegal value. Try again")
        continue

    if user_input != -1:
        my_list.append(user_input)


list_total = 0
for i in my_list:
    list_total += i

my_sum = sum(my_list)

print(my_list)
# fstring formatting in python 3.7
print(f'sum is {list_total} for the list {my_list} and sum is also {my_sum}')
