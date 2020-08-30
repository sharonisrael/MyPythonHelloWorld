
def first_func(my_num = 999):
    my_local_num = my_num * 2
    print("Hellow world", my_local_num)
    print("Hellow world2")

def second_func(my_str, my_int):
    print("Hello " + my_str)
    print(my_int ** 2)
    print("You " + my_str + ":", my_int)

def third_func(my_int):
    return my_int ** 2


def forth_func(my_list):
    print("Printing list")
    for i in my_list:
        print(i)

# The * next to args means "take the rest of the parameters given and put them in a list called args".
def fifth_func(*args):
    print("Printing args")
    for i in args:
        print(i)

first_func()
second_func("Sharon", 5)
print ("Third function ", third_func(5))

ages = [25,66,44,23,67]
forth_func(ages)

food = [2,4,6]
fifth_func(*food)