import functools
import string
import winsound
import itertools
from tkinter import *
import base64

from gtts import gTTS # Import the required module for text to speech conversion
import os # This module is imported so that we can play the converted audio
from PIL import Image, ImageDraw, ImageFont

# import module_name
# from module_name import object_name
# import module_name as new_module_name

DATA_FOLDER = "D:/My_Programming/Python/Data/"

def run_prep_exam():
    x = ['ab', 'cd']
    for i in x:
        x.append(i.upper())
        print(x)


def combine_coins(coins, numbers):
    # new_numbers = ""
    # for i in numbers:
    #     new_numbers += coins + str(i) + ", " if i < (len(numbers)-1) else coins + str(i)
    # return new_numbers

    # for num in numbers:
    #     output += coins + str(num) + ', '
    # # Ignore the last comma.
    # return output[:-2]

    # using list comprehension
    # return ''.join([coins + str(number) + ', ' for number in numbers])[:-2]
    # using map
    # return ''.join(list(map(lambda number: coins + str(number) + ', ', numbers)))[:-2]
    return ', '.join([coins + str(number) for number in numbers])


def run_combine_coins():
    print(combine_coins('$', range(5)))


def double_charachter_func(my_char):
    return my_char * 2


def double_letter(my_str):
    return ''.join(list(map(double_charachter_func, my_str)))


def run_double_letter():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
    # 'ppyytthhoonn'
    # 'wwee  aarree  tthhee  cchhaammppiioonnss!!'


def can_divide_by_four(number):
    return number % 4 == 0


def four_dividers(number):
    return list(filter(can_divide_by_four, range(1, number + 1)))


def run_four_dividers():
    print(four_dividers(9))
    print(four_dividers(3))
    # [4, 8]
    # []


# Very important - the first is the total and the second is current item
# total equals to first value or to default value
# def function(num, item): num is the total
# def concatenate(mlist, x): mlist is the total list
def process_digit(sum, digit):
    return sum + int(digit)


def sum_of_digits(number):
    # total equals to default value = 0
    # See below for more information
    return functools.reduce(process_digit, str(number), 0)


def run_sum_of_digits():
    print(sum_of_digits(104))
    # 5


def password_function(num, item):
    print("num is", num)
    return num + 1


# print((lambda x, y: x + y) (2, 5))
# print(functools.reduce(lambda x, y: x + y, shopping_list))
# print(sorted(list_of_tuples, key=lambda x: x[1])) # for tuple or list x=(1,2)
# calc_sqrt_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
def lambda_password_function_test():
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    print("lst is", lst)
    # total equals to first value because no default
    # first iteration is only take first value
    # password_function will run len(lst) - 1 times
    magic = functools.reduce(password_function, lst)
    # total equals to 0 because default
    # first iteration will do calculation
    # password_function will run len(lst) times
    # magic = functools.reduce(password_function, lst, 0)
    result = (lambda x: x % 4 == 0)(magic)
    if result:
        print("Correct password!")
    else:
        print("Wrong password.")


def run_get_bigger_items():
    # Return list of items in list greater than some value
    my_list = [1, 2, 3, 4, 5, 6]
    my_threshold = 3
    # output is [4, 5, 6]

    # using filter
    # bigger_list = list(filter(lambda x: x > my_threshold, my_list))
    # using list comprehension
    bigger_list = [x for x in my_list if x > my_threshold]
    # Just to play with list comprehension else - will create [-1, -1, -1, 4, 5, 6]
    # bigger_list = [x if x > my_threshold else -1 for x in my_list]
    print(bigger_list)

    l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
    # For numbers above 45 inclusive, I would like to add 1; and for numbers less than it, 5.
    manipulated_list = [x + 1 if x > 45 else x + 5 for x in l]
    print(manipulated_list)


def intersection(list_x, list_y):
    return set([x for x in list_x for y in list_y if x == y])


def run_intersection():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
    # [3]
    # [5, 6]


def is_prime(number):
    # list comprehensive
    return len([x for x in range(2, number) if number % x == 0]) == 0
    # filter
    # return len(list(filter(lambda x: number % x == 0, range(2, number)))) == 0
    # reduce
    # Very important - the first is the total and the second is current item.
    # total equals to first value or to default value
    # return functools.reduce(lambda all_fail, x: all_fail and (number % x != 0), range(2, number), True)


def run_is_prime():
    print(is_prime(42))
    print(is_prime(43))
    # False
    # True


def is_funny(string):
    # lambda with if inside
    return ''.join(list(map(lambda x: 'X' if x not in ('h', 'a') else '', string))) == ''
    # return functools.reduce(lambda all_ok, x: all_ok and x in ('h', 'a'), string, True)
    # return len(list(filter(lambda x: x in ('h', 'a'), string))) == len(string)
    # return len([char for char in string if char != 'h' and char != 'a']) == 0


def run_is_funny():
    print(is_funny("hahahahahaha"))
    print(is_funny("hahahahahsaha"))
    # True
    # False


def hijack_decrypt_password(string, dict):
    # <Add one line of code here>
    # Used the hint of jump 2 characters up: k --> m
    return ''.join(list(map(lambda x: chr(ord(x) + 2), string)))
    # return ''.join([chr(ord(x)+2) for x in string])
    # lambda with elif nested if
    # lambda x: x * 10 if x < 2 else (x ** 2 if x < 4 else x + 10)
    # return ''.join(list(map(lambda x: 'm' if x == 'k' else ('q' if x == 'o' else ('g' if x == 'e' else x)), string)))
    # return ''.join(list(map(lambda x: x if x not in dict.keys() else dict[x], string)))
    # decrypted_message = ""
    # for letter in string:
    #     if letter in dict:
    #         decrypted_message += dict[letter]
    #     else:
    #         decrypted_message += letter
    # return decrypted_message


def run_hijack_decrypt_password():
    password_message = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    password_dict = {'k': 'm', 'o': 'q', 'e': 'g'}
    print(hijack_decrypt_password(password_message, password_dict))
    # sljmai ugrf rfc ambc: lglc dmsp mlc rum


def print_names_file_1(file_path):
    """
    Print longest name
    :param str file_path: file with data location
    """
    with open(file_path, "r") as names_file:
        print(max(map(lambda x: (x.rstrip(), (len(x.rstrip()))), names_file))[0])
        # reduce
        # print(functools.reduce(lambda longest, name: name if len(name) > len(longest) else longest, names_file))
        # Valdimir


def print_names_file_2(file_path):
    """
    Print total names lengths
    :param str file_path: file with data location
    """
    with open(file_path, "r") as names_file:
        # remove the \n when counting. Notice in last line doesn't have \n so I use replace and not [:-1]
        print(sum(map(lambda x: len(x.replace('\n', '')), names_file)))
        # 38


def print_names_file_3(file_path):
    """
    Print shortest names in file
    :param str file_path: file with data location
    """
    with open(file_path, "r") as names_file:
        # clean \n with rstrip() rstrip will delete all trailing whitespace
        names_len_dict = dict(map(lambda x: (x.rstrip(), (len(x.rstrip()))), names_file))
        print('\n'.join(list(filter(lambda name: len(name) == min(names_len_dict.values()), names_len_dict.keys()))))
        # Option B using sorted and take all with same length as  first element length (shortest)
        # new_list = sorted(open("names.txt", "r").read().split(), key=len)
        # print("\n".join([word for word in new_list if len(new_list[0]) == len(str(word))]))
        # Ed
        # Jo


def print_names_file_4(file_path, file_out_path):
    """
    Export names lengths by same order to new file
    :param str file_path: file with data location
    :param str file_out_path: file export
    """
    with open(file_path, "r") as names_file:
        with open(file_out_path, "w") as names_len_file:
            names_len_file.write('\n'.join(list(map(lambda name: str(len(name.rstrip())), names_file))))
    # 4
    # 4
    # 8
    # 7
    # 2
    # 5
    # 6
    # 2


def print_names_file_5(file_path):
    """
    Print all names with given length in file
    :param str file_path: file with data location
    """
    user_len = int(input("Enter name length: "))
    with open(file_path, "r") as names_file:
        # filter
        print(''.join(list(filter(lambda name: len(name.rstrip()) == user_len, names_file))))
        # list comprehensive
        # print(''.join([name for name in names_file if len(name.rstrip()) == user_len]))
    # Enter name length: 4
    # Hans
    # Anna


def run_print_names_file():
    file_path = DATA_FOLDER + "names.txt"
    print_names_file_1(file_path)
    # print_names_file_2(file_path)
    # print_names_file_3(file_path)
    # file_out_path = DATA_FOLDER+"name_length.txt"
    # print_names_file_4(file_path, file_out_path)
    # print_names_file_5(file_path)


class UnderAgeException(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Provided age is not above 18: " + str(self._age) + "." \
                                                                   " You need to wait " + str(
            18 - self._age) + " more years."


def send_invitation(name, age):
    if int(age) < 18:
        # print("under age")
        raise UnderAgeException(age)
    else:
        print("You should send an invite to " + name)


def run_send_invitation():
    send_invitation("Sharon", 17)
    send_invitation("Sharon", 20)


class UsernameContainsIllegalCharacter(Exception):
    pass


class UsernameTooShort(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Username too short"


class UsernameTooLong(Exception):
    pass

class PasswordMissingCharacter(Exception):

    def __init__(self, password_missing_type = "Unknown"):
        self._password_missing_type = password_missing_type

    def __str__(self) -> str:
        return "The password is missing a character (" + self._password_missing_type + ")"

class PasswordMissingCharacterUppercase(PasswordMissingCharacter):

    def __init__(self):
        super().__init__("Upper")

class PasswordMissingCharacterLowercase(PasswordMissingCharacter):

    def __init__(self):
        super().__init__("Upper")

class PasswordMissingCharacterDigit(PasswordMissingCharacter):

    def __init__(self):
        super().__init__("Digit")

class PasswordMissingCharacterSpecial(PasswordMissingCharacter):

    def __init__(self):
        super().__init__("Special")



class PasswordTooShort(Exception):
    pass

class PasswordTooLong(Exception):
    pass


def username_validator(username):
    return functools.reduce(lambda all_legal, x: all_legal and (str(x).isalpha() or str(x).isdigit() or x == '_'),
                            username, True)

def password_validator(password):
    has_digit = password_part_validator(password, string.digits)
    has_lowercase = password_part_validator(password, string.ascii_lowercase)
    has_uppercase = password_part_validator(password, string.ascii_uppercase)
    has_special = password_part_validator(password, string.punctuation)
    return has_digit and has_lowercase and has_uppercase and has_special

def password_part_validator(password, part_list):
    return len(list(filter(lambda x: x in part_list, password))) > 0


def check_input(username, password):
    if not username_validator(username):
        raise UsernameContainsIllegalCharacter()
    elif len(username) < 3:
        raise UsernameTooShort()
    elif len(username) > 16:
        raise UsernameTooLong()
    elif len(password) < 8:
        raise PasswordTooShort()
    elif len(password) > 40:
        raise PasswordTooLong()
    elif not password_validator(password):
        raise_password_validator_exception(password)
    else:
        print('OK')


def raise_password_validator_exception(password):
    if not password_part_validator(password, string.digits):
        raise PasswordMissingCharacterDigit()
    if not password_part_validator(password, string.ascii_lowercase):
        raise PasswordMissingCharacterLowercase()
    if not password_part_validator(password, string.ascii_uppercase):
        raise PasswordMissingCharacterUppercase()
    if not password_part_validator(password, string.punctuation):
        raise PasswordMissingCharacterSpecial()

def run_check_input():
    # check_input("1", "2")
    # check_input("0123456789ABCDEFG", "2")
    # check_input("A_a1.", "12345678")
    # check_input("A_1", "2")
    # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    # check_input("A_1", "ABCDEFGHIJLKMNOP")
    # check_input("A_1", "ABCDEFGhijklmnop")
    # check_input("A_1", "4BCD3F6h1jk1mn0p")
    # check_input("A_1", "4BCD3F6.1jk1mn0p")

def run_check_input2():
    # Enter username: A
    # Enter password: A
    # Probolem with username and password: Username too short
    valid_user_and_password = False
    while (not valid_user_and_password):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            valid_user_and_password = True
        except Exception as e:
            print("Probolem with username and password: " + str(e))

def print_prime_numbers():
    prime_generator = (n for n in range(10 ** 100) if is_prime(n))
    print(next(prime_generator))
    print(next(prime_generator))


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    english_generator = (words[i] for i in sentence.split())
    return ' '.join([next(english_generator) for i in sentence.split()])

def run_translate():
    print(translate("el gato esta en la casa"))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    prime_generator = (n for n in range(n, n*2) if is_prime(n))
    return next(prime_generator)

def run_first_prime_over():
    print(first_prime_over(1000000))
    # 1000003


def parse_ranges(ranges_string):
    # my_ranges = (my_range for my_range in ranges_string.split(','))
    # int_list = []
    # for from_to in my_ranges:
    #     int_list += range(int(str(from_to).split('-')[0]), int(str(from_to).split('-')[1])+1)
    # return int_list
    my_ranges = (my_range for my_range in ranges_string.split(','))
    my_start_stops = ((int(str(my_start_stop).split('-')[0]), int(str(my_start_stop).split('-')[1])+1) for my_start_stop in my_ranges)
    my_int_ranges = (range(my_start_stop[0], my_start_stop[1]) for my_start_stop in my_start_stops)
    # my_ints = (x for x in my_int_ranges)
    my_ints = []
    for i in my_int_ranges:
        my_ints += i
    # print(my_int_ranges)
    # my_ints = [i for i in my_int_ranges]
    # return my_ints
    return my_ints
    # lst = []
    # # Generator1 - take a couple of start-stop
    # gen_couple = ((l.split("-") for l in ranges_string.split(",")))
    # # Generator2 - get all numbers between start and stop
    # ??? Hmm.. I didn't understand
    # # gen_num = (i for start, stop in gen_couple for i in range (int(start), int(stop) + 1))
    # # make a list of all the numbers
    # for num in gen_num:
    #     lst.append(num)
    # return lst


def run_parse_ranges():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))
    # [1, 2, 4, 8, 9, 10]
    # [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]

def get_fibo():
    first_value = 0
    second_value = 1

    yield first_value
    yield second_value

    while(True):
        sum_both = first_value + second_value
        # new first equals to previous second
        first_value = second_value
        # new second is sum
        second_value = sum_both
        # return next value which is new second_value
        yield second_value

def run_get_fibo():
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def gen_secs():
    for seconds in range(60):
        yield seconds

def gen_minutes():
    for minutes in range(60):
        yield minutes

def gen_hours():
    for hours in range(24):
        yield hours

def gen_time():
    for hours in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                # yield '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
                yield f'{hours:02d}:{minutes:02d}:{seconds:02d}'

def run_gen_time():
    for gt in gen_time():
        print(gt)
    # 00:00:00
    # 00:00:01
    # 00:00:02
    # 00:00:03
    # 00:00:04
    # 00:00:05
    # 00:00:06

def gen_years(start=2019):
    my_start = start
    while(True):
        yield my_start
        my_start += 1

def gen_months():
    for months in range(1,13):
        yield months
    # This is not good because iterations will never end so will continue to loop over months
    # my_month = 1
    # while(True):
    #     not good
    #     yield my_month
    #     my_month = my_month + 1 if my_month < 12 else 1

def gen_days(month, leap_year=True):
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month == 2 and leap_year:
        # actually it's stateless and I can put return.
        return 28
    else:
        # actually it's stateless and I can put return.
        return int(days_in_month[month])

def is_leap_year(years):
    # Leap Years are any year that can be exactly divided by 4 (such as 2016, 2020, 2024, etc)
    leap_year = (years % 4 == 0)
    # except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
    # except if it can be exactly divided by 400, then it is (such as 2000, 2400)
    if years % 100 == 0 and years % 400 != 0:
        leap_year = False
    return leap_year


def gen_date():
    for years in gen_years():
        for months in gen_months():
            # mm/yyyy
            # yield f'{months:02d}/{years:02d}'
            for days in range(1, gen_days(months, is_leap_year(years)) + 1):
                # dd/mm/yyyy
                # yield f'{days:02d}/{months:02d}/{years:02d}'
                for times in gen_time():
                    # dd/mm/yyyy hh:mm:ss
                    yield f'{days:02d}/{months:02d}:{years:02d} {times}'
                    # yield '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


def run_gen_date():
    date_generator = gen_date()
    for i in range(1000000):
        print(next(date_generator))

def run_play_yonatan():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }

    # note and time
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

    info = [note.split(',') for note in notes.split(',')]
    print(info)

    # create iter
    notes_iter = iter(notes.split('-'))
    print(type(notes_iter))

    # WIth for loop
    for note_and_duration_iter in notes_iter:
        note_and_duration = str(note_and_duration_iter)
        print(note_and_duration)
        # Do something with the element
        separator_index = note_and_duration.index(',')
        print(separator_index)
        note = note_and_duration[:separator_index]
        frequency = freqs[note]
        duration = int(note_and_duration[separator_index + 1:])
        winsound.Beep(frequency, duration)

    # Infinite loop
    notes_iter = iter(notes.split('-'))
    while True:
        try:
            # Get the next item
            note_and_duration = str(next(notes_iter))
            print(note_and_duration)
            # Do something with the element
            separator_index = note_and_duration.index(',')
            print(separator_index)
            note = note_and_duration[:separator_index]
            frequency = freqs[note]
            duration = int(note_and_duration[separator_index+1:])
            winsound.Beep(frequency, duration)
        except StopIteration:
            # If StopIteration is raised, break from loop
            break

def run_print_every_third_number():
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        print(i)
        try:
            next(numbers)
            next(numbers)
        except StopIteration:
            break

def run_all_ways_for_hundred():
    # You have 3 bills of 20, 5 bills of 10, 2 bills of 5, 5 bills of 1
    # value:bills so will be unique bill value
    bills_list = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    bills_total_hundred = []
    for number_of_bills in range(1, len(bills_list)+1):
        bills_combinations = set(itertools.combinations(bills_list, number_of_bills))
        for combination in bills_combinations:
            if sum(combination) == 100:
                bills_total_hundred += [combination]
    print(len(bills_total_hundred))
    print(bills_total_hundred)

class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
    def get_name(self):
        return self._name

class EmployeeManager:
    def __init__(self):
        self._employee_lst = []
        self.eml_index = -1
    def add_employee(self, new_empl):
        self._employee_lst.append(new_empl)
    def __iter__(self):
        return self
    def __next__(self):
        if self.eml_index >= len(self._employee_lst) -1:
            raise StopIteration()
        self.eml_index += 1
        print(f'eml_index {self.eml_index}')
        return self._employee_lst[self.eml_index].get_name()

def run_employees():
    manager = EmployeeManager()
    manager.add_employee(Employee("Lia Levi", 30, 5000))
    manager.add_employee(Employee("Yosef Cohen", 32, 4800))
    manager.add_employee(Employee("Oded Haim", 47, 5100))
    for emp_name in manager:
        print(emp_name)

class MusicNotes:
    """
    La 	55 	110 	220 	440 	880
    Si 	61.74 	123.48 	246.96 	493.92 	987.84
    Do 	65.41 	130.82 	261.64 	523.28 	1046.56
    Re 	73.42 	146.84 	293.68 	587.36 	1174.72
    Mi 	82.41 	164.82 	329.64 	659.28 	1318.56
    Fa 	87.31 	174.62 	349.24 	698.48 	1396.96
    Sol 	98 	196 	392 	784 	1568
    :return:
    """
    def __init__(self) -> None:
        self._basic_notes_freqs = {'La': 55, 'Si': 61.74, 'Do': 65.41, 'Re': 73.4, 'Mi': 82.41, 'Fa': 87.31, 'Sol': 98}
        self._max_notes_multiply = 5
        self._notes_index = 0
        self._freqs_multiplier = 0

    def __iter__(self):
        return self

    def __next__(self):
        # stop after all table complete - reached right most column
        if self._freqs_multiplier >= self._max_notes_multiply:
            raise StopIteration()
        # decide value (row = note, column = frequency)
        next_note = list(self._basic_notes_freqs.keys())[self._notes_index]
        next_note_frequency = self._basic_notes_freqs[next_note] * (2 ** self._freqs_multiplier)
        # promote note
        self._notes_index += 1
        # After all notes promote frequency
        if self._notes_index >= len(self._basic_notes_freqs.keys()):
            # back to first note
            self._notes_index = 0
            self._freqs_multiplier += 1
        # print(next_note_frequency, self._notes_index, self._freqs_multiplier)
        return next_note_frequency


def run_notes_iter():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


def run_show_ui_dialog():
    window = Tk()
    window.title("tk")
    lbl = Label(window, text="What's your favorite video?", font=("Arial Bold", 24))
    lbl.grid(column=0, row=0)

    def clicked():
        new_img = PhotoImage(file=DATA_FOLDER+"IMG_9924.GIF")
        # Need to update both so new image will be displayed
        image_label.image = new_img
        image_label.configure(image=new_img)
        btn.configure(text="Button was clicked !!")

    btn = Button(window, text="click to find out!", command=clicked)
    btn.grid(column=0, row=1)

    image_label = Label(window)
    image_label.grid(column=0, row=2)

    window.mainloop()

def run_decrypt_message():
    # Base64 encoding allows us to convert bytes containing binary or text data to ASCII characters.
    # By encoding our data, we improve the chances of it being processed correctly by various systems.
    base64_message = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="
    # We then encode our message into a bytes-like object with encode('ASCII')
    base64_bytes = base64_message.encode('ascii')
    # We continue by calling the base64.b64decode method to decode the base64_bytes into our message_bytes variable
    message_bytes = base64.b64decode(base64_bytes)
    # Finally, we decode message_bytes into a string object message, so it becomes human readable.
    message = message_bytes.decode('ascii')
    print(message)

def print_pip_details():
    print()
    print("My pip installation guide")
    print("-------------------------")
    print("To list outdated packages, and show the latest version available: pip list --outdated")
    print("To list installed packages: pip list")
    print("pip install SomePackage: pip install SomePackage")
    print("pip upgrade SomePackage: pip install SomePackage --upgrade")
    print("Location of pip installed packages: D:\My_Programming\Python\Python38-32\Lib\site-packages")

def say_text():
    # other packages are
    # import win32com.client as wincl
    # speak = wincl.Dispatch("SAPI.SpVoice")
    # speak.Speak("Hello World")
    # from tts_watson.TtsWatson import TtsWatson
    # ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice')
    # ttsWatson.play("Hello World")
    my_text = "first time i'm using a package in next.py course"
    # Passing the text and language to the engine,
    myobj = gTTS(text=my_text, lang='en', slow=False)
    # Saving the converted audio in a mp3 file
    myobj.save(DATA_FOLDER+"welcome.mp3")
    # Playing the converted file
    os.system("start " + DATA_FOLDER+"welcome.mp3")

def connect_the_dots():
    # list of dots, in the following format: [x, y, x, y, x, y,...]
    first = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
        132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
        77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
        156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
        136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
        366, 149, 379, 147, 394, 146, 399
    )
    second = (
        156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
        150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
        159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
        218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
        114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
        162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
        113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
        128, 156, 134, 157, 136, 156, 136
    )

    # get an image
    im = Image.open(DATA_FOLDER+"ex6p4.jpg")    # base = Image.open('Pillow/Tests/image.png').convert('RGBA')
    # im = Image.new('RGBA', (700, 700), (255, 255, 255, 0)) # make a blank image. initialized to transparent text color

    d = ImageDraw.Draw(im)
    # d.line(first, fill='blue', width=2)
    d.polygon(first, fill=(0, 255, 0), outline=(0, 0, 255))
    d.line(second, (255, 0, 0), width=2)
    fnt = ImageFont.truetype("arial.ttf", 30)
    d.text((180, 190), "Thank you", font=fnt, fill=(0, 0, 255, 128))
    d.text((210, 220), "next.py", font=fnt, fill=(0, 0, 255, 128))
    im.show()
    im.save(DATA_FOLDER+"ex6p4_out.jpg")


def main():
    # run_combine_coins()
    # run_double_letter()
    # run_sum_of_digits()
    # lambda_password_function_test()
    # run_get_bigger_items()
    # run_intersection()
    # run_is_prime()
    # run_is_funny()
    # run_hijack_decrypt_password()
    # run_print_names_file()
    # run_send_invitation()
    # run_check_input()
    # run_check_input2()
    # print_prime_numbers()
    # run_translate()
    # run_first_prime_over()
    # run_parse_ranges()
    # run_get_fibo()
    # run_gen_time()
    # run_gen_date()
    # run_play_yonatan()
    # run_print_every_third_number()
    # run_all_ways_for_hundred()
    # run_employees()
    # run_notes_iter()
    # run_show_ui_dialog()
    # run_decrypt_message()
    # print_pip_details()
    # say_text()
    connect_the_dots()
# TO undestand: when generator uses while and when for
# איטרטור הוא גם איטרבל.

"""
face_recognition
imageai
PIL
Numpy
Matplotlib pie chart

Keras
Scikit-Learn
AutoML
"""

# pytest or unittest


if __name__ == "__main__":
    main()
