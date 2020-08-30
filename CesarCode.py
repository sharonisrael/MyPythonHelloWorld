
my_numbers = [1,2,3,4,5,6]

my_numbers_list = list(my_numbers)

print(my_numbers)
print(my_numbers_list)

my_zip = zip(my_numbers, my_numbers)


a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Vicky"]

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

my_list = list(zip(a,b))
print(my_list)

my_dict = dict(zip(a,b))
print(my_dict)

