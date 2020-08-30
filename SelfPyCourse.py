import calendar


def simple_increment(x):
    return x + 1

# joker_str = "Joker"
# # Starting at 2 until not including 5
# print(joker_str[2:5])
#
# numbers = "123456789"
# print(numbers[0:10:1])
# print(numbers[3:6:3])
# print(numbers[-1:-7])
# print(numbers[-1:-7:-1])

# print("He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3))

# message = "\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,\nDon\'t back down and stop the player!\n\tDo you want to play Taki?\n\tPress y\\n\n"
# print(message)

# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# # From end to beginning in jumps of 2
# print(encrypted_message[::-2])
#
# parameter_str = "C"
# center_str = parameter_str.center(5)
# len_int = len(parameter_str)
# print(center_str)

# given_str = input("Please enter a string: ")
# print(given_str[0]+given_str[1:].replace("d", "e"))

# given_str2 = input("Please enter a string: ")
# first_half = given_str2[0:(len(given_str2)//2)].lower()
# second_half = given_str2[(len(given_str2)//2):].upper()
# print(first_half + second_half)

# given_str3 = input("Please enter a string: ").lower().replace(" ","")
# print(given_str3[-1::-1])
# if (given_str3 == given_str3[-1::-1]):
#     print("Good")
# else:
#     print("Bad")

# given_str4 = input("Insert the temperature you would like to convert: ").lower()
# given_degrees = int(given_str4.replace('f','').replace('c', ''))
# new_degrees_str = ""
# if ('f' in given_str4):
#     # farenhight to celsious
#     new_degrees = (5 * given_degrees-160)/9
#     new_degrees_str = str(int(new_degrees)) + "C"
# elif ('c' in given_str4):
#     # celsious to farenhight
#     new_degrees = (9 * given_degrees + 32 * 5) / 5
#     new_degrees_str = str(int(new_degrees)) + "F"
# else:
#     new_degrees_str = "Illegal"
# print(new_degrees_str)

# given_str5 = input("Enter a date: ")
# given_str5 = "09/04/2020"
# # year month day
# date_values = [int(given_str5[6:10]), int(given_str5[3:5]), int(given_str5[0:2])]
# print(date_values)
# out_weekday = calendar.weekday(date_values[0], date_values[1], date_values[2])
# # The output is 0=Monday, 1 Tuesday, 2 Wednesday, 3 Thursday 4 Friday, 5 Saturday, 6 Sunday
# print(out_weekday, calendar.day_name[out_weekday])
# days = ["Sunday", "Monday", "Tuesday", "Wenseday", "Thursday", "Friday", "Saturday"]
# print(days[out_weekday])

# c = 1
# def foo3():
#     # Even though I call a global it's still not defined here and will cause compilation error . I need to put global c before
#     c = c + 1
#     print(c)
# foo3()
# print(c)


# given_number = int(input("Enter three digits (each digit for one pig): "))
# first_pig_blocks = given_number // 100
# # Smarter solution with modulu - left over from dividing in 100 is the 10s + 1s (124 --> 24)
# second_pig_blocks = (given_number % 100) // 10
# third_pig_blocks = (given_number % 10)
# # second_pig_blocks = (given_number - first_pig_blocks * 100) // 10
# # third_pig_blocks = (given_number - first_pig_blocks * 100 - second_pig_blocks * 10)
# total_pig_blocks =  first_pig_blocks + second_pig_blocks + third_pig_blocks
# print(total_pig_blocks)
# even_split_blocks = total_pig_blocks // 3
# print(even_split_blocks)
# remainder_even_split_blocks =  total_pig_blocks % 3
# print(remainder_even_split_blocks)
# is_even_split = (remainder_even_split_blocks == 0)
# print(is_even_split)

def last_early(my_str):
    print(my_str[-1].lower() in my_str[:-1].lower())

def run_last_early():
    last_early("happy birthday")
    last_early("best of luck")
    last_early("Wow")
    last_early("X")

def distance(num1, num2, num3):
    first_rule = (abs(num2-num1) == 1) or (abs(num3-num1) == 1)
    second_rule = ((abs(num2-num1) >= 2 and abs(num2-num3) >= 2) or (abs(num3-num1) >= 2 and abs(num3-num2) >= 2))
    return first_rule and second_rule

def run_distance():
    print(distance(1, 2, 10))
    print(distance(4, 5, 3))

# run_distance()

def filter_teens(a = 13, b = 13, c = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)

def fix_age(age):
    fixed_age = age
    if (age in range(13,19) and age not in range(15,16)):
        fixed_age = 0
    return fixed_age

def run_filter_teens():
    print(filter_teens())
    print(filter_teens(1, 2, 3))
    print(filter_teens(2, 13, 1))
    print(filter_teens(2, 1, 15))

# run_filter_teens()

# big is 5, small is 1, x is row size
def chocolate_maker(small, big, x):
    """
    Use by Ctrl + Q or Alt + mouse scroller
    Calculate if small and big blocks can fit in row
    :param int small: small chunks
    :param int big: big chunks
    :param int x: row size
    :return: if fit in one row
    :rtype: bool
    """
    SMALL_SIZE = 1
    BIG_SIZE = 5
    return ((small * SMALL_SIZE + big * BIG_SIZE) == x)

def run_chocolate_maker():
    print(chocolate_maker(3, 1, 8))
    print(chocolate_maker(3, 1, 9))
    print(chocolate_maker(3, 2, 10))

# run_chocolate_maker()

# :param str sender: The person sending the message
#    :param str recipient: The recipient of the message
#    :param str message_body: The body of the message
#    :param priority: The priority of the message, can be a number 1-5
#    :type priority: integer or None
#    :return: the message id
#    :rtype: int
#    :raises ValueError: if the message_body exceeds 160 characters
#    :raises TypeError: if the message_body is not a basestring

# print(chocolate_maker.__doc__)

def func_sum(num1, num2):
    """
    calculate sum
    :param int num1: first number
    :param int num2: second number
    :return: sum
    :rtype: int
    """
    return num1 + num2

def string_to_list():
    name = "Sharon"
    letters_list = list(name)
    print(letters_list)

def shift_left(my_list):
    """
    Shift left a list of 3
    :param my_list:
    :rtype: list
    """
    # a, b, c = my_list
    # return [b, c, a]
    # new_list = my_list[1:]
    # new_list.append(my_list[0])
    # new_list = my_list[1:] + [my_list[0]]  # cant do my_list[1:] + my_list[0] becasue my_list[0] is int
    new_list = my_list[1:] + my_list[:1]
    return new_list

def run_shift_left():
    my_list = [0, 1, 2]
    new_list = shift_left(my_list)
    print(new_list)

def unify_lists():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7]
    list3 = list1 + list2 # [1, 2, 3, 4, 5, 6, 7]
    list4 = [list1 + list2] # [[1, 2, 3, 4, 5, 6, 7]]
    print(list3)
    print(list4)

def format_list(my_list):
    """
    Get list of strings in even size
    return string with elements in even places with ,
    And in the and put and last element
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    --> hydrogen, lithium, boron, and magnesium
    :param my_list:
    :rtype: str
    """
    new_list_str = ', '.join(my_list[:-1:2]) + " and " + my_list[-1]
    return new_list_str

def run_format_list():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    my_list_str = format_list(my_list)
    print(my_list_str)

def extend_list_x(list_x, list_y):
    """
    get 2 lists list_y, list_x. and alternate list_x so it will include list_y in the beginning
    return the big list_x
    :param list list_x: list x
    :param list list_y: list y
    :rtype: list
    """
    # new_list_x = list_x * 2
    # test_list = [6] + test_list
    # test_list.insert(0, 6) # at beginning. append 6 
    # new_list_x[:len(list_y)] = list_y
    list_x[:0] = list_y
    # list_x = list_x + list_y
    return list_x

def run_extend_list_x():
    x = [4, 5, 6]
    y = [1, 2, 3]
    new_list = extend_list_x(x, y)
    print(new_list)

def are_lists_equal(list1, list2):
    # list1.sort()
    # list2.sort()
    # return list1 == list2
    my_list1 = sorted(list1)
    my_list2 = sorted(list2)
    return my_list1 == my_list2

def run_are_lists_equal():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

def longest(my_list):
    longest_element = max(my_list, key=len)
    return longest_element

def run_longest():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))

def squared_numbers(start, stop):
    """
    return a list of square numbers from start to stop
    :param int start:
    :param int stop:
    :rtype: list
    """
    my_list = []
    i=start
    while(i<=stop):
        my_list += [i ** 2]
        i += 1
    return my_list

def run_squared_numbers():
    print(squared_numbers(4, 8))
    # [16, 25, 36, 49, 64]
    print(squared_numbers(-3, 3))
    # [9, 4, 1, 0, 1, 4, 9]

def is_greater(my_list, n):
    greater_list = []
    for value in my_list:
        if (value > n):
            greater_list += [value]
    return greater_list

def run_is_greater():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)
    # [30, 60]


def numbers_letters_count(my_str):
    num_digits = 0;
    num_letters = 0
    for charachter in my_str:
        # This is for values only : [on_true] if [expression] else [on_false]
        num_digits += 1 if (charachter.isnumeric()) else 0
        num_letters += 1 if (not charachter.isnumeric()) else 0
        # if (charachter.isnumeric()):
        #     num_digits += 1
        # else:
        #     num_letters += 1
    return [num_digits, num_letters]

def run_numbers_letters_count():
    print(numbers_letters_count("Python 3.6.3"))
    # [3, 9]

def for_example():
    # Notice does not include -9
    for num in range(0, -9, -3):
        print(num)

def seven_boom(end_number):
    my_list = []
    for i in range(0, end_number+1):
        my_list += ['BOOM'] if (i % 7 == 0 or '7' in str(i)) else [i]
    return my_list

def run_seven_boom():
    print(seven_boom(17))
    # ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

def sequence_del(my_str):
    new_str = ""
    for i in range(0, len(my_str)):
        if (i == len(my_str)-1):
            if (my_str[i] != my_str[i-1]):
                new_str += my_str[i]
        elif my_str[i] != my_str[i+1]:
            new_str += my_str[i]
    return new_str

def run_sequence_del():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    # 'python'
    print(sequence_del("SSSSsssshhhh"))
    # 'Ssh'
    print(sequence_del("Heeyyy   yyouuuu!!!"))
    # 'Hey you!'

def shopping_list():
    my_list = "Milk,Cottage,Milk,Tomatoes,Tomatoes".split(",")
    # my_list = input("Please enter initial list: ").split(",")

    while(True):
        my_digit = int(input("Please enter digit: "))
        if my_digit == 1:
            print(my_list)
        elif my_digit == 2:
            print(len(my_list))
        elif my_digit == 3:
            check_product = input("Please enter product to check: ")
            print(check_product + " is in list? ", check_product in my_list)
        elif my_digit == 4:
            check_product = input("Please enter product to count: ")
            print(check_product + " time in list? ", my_list.count(check_product))
        elif my_digit == 5:
            check_product = input("Please enter product to delete: ")
            my_list.remove(check_product)
            print(my_list)
        elif my_digit == 6:
            check_product = input("Please enter product to add: ")
            #  my_list.extend https://www.geeksforgeeks.org/append-extend-python/
            my_list += [check_product] # Can do my_list.append()
            print(my_list)
        elif my_digit == 7:
            illegl_list = []
            for product in my_list:
                if (len(product) < 3 or not product.isalpha()):
                    #  my_list.extend https://www.geeksforgeeks.org/append-extend-python/
                    illegl_list.append(product)
            print(illegl_list)
        elif my_digit == 8:
            # remove duplicates
            # list(set(t))
            # Add only if not in the unique list
            unique_list = []
            for product in my_list:
                if product not in unique_list:
                    unique_list.append(product)
            my_list = unique_list

            # i = 0
            # while(i < len(my_list)-1):
            #     current_product = my_list[i]
            #     for j in range(len(my_list)-1,i,-1):
            #         if (my_list[j] == current_product):
            #             del(my_list[j])
            #     i += 1
            print(my_list)
        elif my_digit == 9:
            print("Bye bye")
            break

def print_arrow(my_char, max_length):
    for row in range(1, max_length + 1):
        arrow_row = my_char * row
        print(arrow_row)
    for row in range(max_length + 1, max_length * 2):
        arrow_row = my_char * (max_length * 2 - row)
        print(arrow_row)

def run_print_arrow():
    print_arrow('*', 5)

def run_print_data():
    data = ("self", "py", 1.543)
    # Hello self.py learner, you have only 1.5 units left before you master the course!
    # print("Hello", '{}.{}'.format(data[0], data[1]), "learner, you have only", '{:.2f}'.format(data[2]), "units left before you master the course!")
    # python fstring http://zetcode.com/python/fstring/
    print(f'Hello {data[0]}.{data[1]} learner, you have only {data[2]:.1f} units left before you master the course!')

def sort_prices(list_of_tuples):
    """
    sort by the price
    :param list list_of_tuples:
    :rtype: tuple
    """
    return sorted(list_of_tuples, key = sort_price_key_fn, reverse=True)

def sort_price_key_fn(my_tuple):
    return float(my_tuple[1])

def run_sort_prices():
     # [('item', 'price'), ('item', 'price'), ('item', 'price')]
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))
    # [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]

def mult_tuple(tuple1, tuple2):
    my_tuple_list = []
    for first_element in tuple1:
        for second_element in tuple2:
            my_tuple_list += [(first_element, second_element)]
            my_tuple_list += [(second_element, first_element)]
    return my_tuple_list


def run_mult_tuple():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))
    # ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))
    # ((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))


def sort_anagrams(list_of_strings):
    """
    :param list list_of_strings:
    :return: grouped strings
    :rtype: list
    """
    my_tuples_list = []
    for str_i in list_of_strings:
        was_added = False
        for tuple_i in my_tuples_list:
            if sorted(str_i) == sorted(tuple_i[0]):
                tuple_i += [str_i]
                was_added = True
        if not was_added:
            my_tuples_list += ([str_i],)
    return my_tuples_list

def run_sort_anagrams():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))
    # [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]


def run_dict_example():
    dict = {'first_name' : 'Mariah',
            'last_name' : 'Carey',
            'birth date' : '27.03.1970',
            'hobbies' : ['Sing', 'Compose', 'Act']}

    print(dict['last_name'])
    print(calendar.month_name[int(dict['birth date'][3:5])])
    print(len(dict['hobbies']))
    print(dict['hobbies'][-1])
    dict['hobbies'] += ['Cooking']
    print(dict['hobbies'])
    my_date = dict['birth date']
    my_date_tuple = int(my_date[0:2]), int(my_date[3:5]), int(my_date[6:10])
    print (my_date_tuple)
    dict['Age'] = 40
    print (dict)

def count_chars(my_str):
    dict = {}
    for my_char in my_str:
        if my_char in dict.keys():
            dict[my_char] = dict[my_char] + 1
        else:
            # print(dict[my_char]) creates KeyError
            dict[my_char] = 1
    return dict

def run_count_chars():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))
    # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

def inverse_dict(my_dict):
    opposite_dict = {}
    for my_key in my_dict.keys():
        my_value = my_dict[my_key]
        if my_value in opposite_dict.keys():
            my_list = opposite_dict[my_value]
            my_list += [my_key]
        else:
            my_list = []
            my_list += [my_key]
            opposite_dict[my_value] = my_list
    for my_key in opposite_dict.keys():
        my_list = opposite_dict[my_key]
        my_list.sort()
    return opposite_dict

def run_inverse_dict():
    course_dict = {'love': 3, 'I': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))
    # {3: ['I', 'love'], 2: ['self.py!']}

def are_files_equal(file1, file2):
    allLinesEqual = True
    first_file = open(file1, "r")
    second_file = open(file2, "r")
    for first_line in first_file:
        second_line = second_file.readline()
        allLinesEqual = allLinesEqual and first_line == second_line
    first_file.close()
    second_file.close()
    print(allLinesEqual)

def run_are_files_equal():
    are_files_equal(
        "D:/My_Programming/Python/Data/1.txt",
        "D:/My_Programming/Python/Data/2.txt")

def read_manipulate_file(fileName, command):
    # with open(file,mode) as input_file:
    file = open(fileName, "r")
    if command == 'sort':
        my_list = []
        for line in file:
            my_line_list = line.replace("\n","").split()
            my_list += my_line_list
            # my_list.extend(my_line_list)
        print(sorted(my_list))
    elif command == 'rev':
        for line in file:
            # reverse
            print(line.replace("\n", "")[::-1])  # not including last \n in the row. Also can print(line[-2::-1])
    elif command == 'last':
        # I could read all lines to buffer and then do len on the loaded_lines
        # loaded_lines = file.readlines()
        # I could count the lines first
        # total_count = len(file.readlines())
        # lineCount = 0
        # for line in file:
        #     lineCount += 1
        # file.close()
        max_last_lines = 3
        last_lines = []
        for line in file:
            if len(last_lines) >= max_last_lines:
                # delete first line https://www.geeksforgeeks.org/python-removing-first-element-of-list/
                last_lines = last_lines[1:]
            last_lines += [line.replace("\n","")]
        for my_last_line in last_lines:
            print(my_last_line) # without last \n
    file.close()
    print('--------------')

def run_read_manipulate_file():
    read_manipulate_file("D:/My_Programming/Python/Data/sampleFile.txt", 'sort')
    read_manipulate_file("D:/My_Programming/Python/Data/sampleFile.txt", 'rev')
    read_manipulate_file("D:/My_Programming/Python/Data/sampleFile.txt", 'last')

def copy_file_content(source, destination):
    with open(source, "r") as copy_file:
        with open(destination, "w") as paste_file:
            for row in copy_file:
                paste_file.write(row)
    # copy_file = open(source, "r")
    # paste_file = open(destination, "w")
    # for row in copy_file:
    #     paste_file.write(row)
    # copy_file.close()
    # paste_file.close()

def run_copy_file_content():
    copy_file_content("D:/My_Programming/Python/Data/copy.txt", "D:/My_Programming/Python/Data/paste.txt")

def who_is_missing(file_name, file_found_name):
    missing_number = 0
    with open(file_name, "r") as numbers_file:
        row_numbers_str = numbers_file.read().split(',')
        row_numbers = []
        for current_row_number in row_numbers_str:
            row_numbers += [int(current_row_number)]
        max_number = max(row_numbers)
        for number in range(1, max_number):
            if number not in row_numbers:
                missing_number = number

    with open(file_found_name, "w") as found_file:
        found_file.write(str(missing_number))

def run_who_is_missing():
    who_is_missing("D:/My_Programming/Python/Data/findMe.txt", "D:/My_Programming/Python/Data/found.txt")

def my_mp3_playlist(file_path):
    """
    Use by Ctrl + Q or Alt + mouse scroller
    :param str file_path:
    :rtype: tuple
    """
    songs_list = []
    with open(file_path, "r") as songs_file:
        for current_song in songs_file:
            songs_list += [current_song.replace('\n','').split(';')]
    longest_name_list = sorted(songs_list, key = sort_song_name_fn, reverse=True)
    artist_count = {}
    for song_details in songs_list:
        if song_details[1] not in artist_count:
            artist_count[song_details[1]] = 0
        artist_count[song_details[1]] += 1
    # Get key with maximum value in dictionary
    most_productive_artist = max(artist_count, key=artist_count.get)
    return longest_name_list[0][0], len(songs_list), most_productive_artist

def sort_song_name_fn(song_details):
    song_time_list = song_details[2].split(':')
    song_time = float(song_time_list[0]) + (float(song_time_list[1])/60.0)
    return song_time

def run_my_mp3_playlist():
    print(my_mp3_playlist("D:/My_Programming/Python/Data/songs.txt"))
    # ("Tudo Bom", 5, "The black Eyed Peas")

def my_mp4_playlist(file_path, out_file_path, new_song):
    songs_list = []
    with open(file_path, "r") as songs_file:
        for current_song in songs_file:
            songs_list += [current_song]
    new_songs_list = songs_list[:2] + [new_song + '\n'] + songs_list[2:]
    with open(out_file_path, "w") as new_songs_file:
        for current_song in new_songs_list:
            new_songs_file.write(current_song)
    with open(out_file_path, "r") as songs_file:
        return songs_file.read()

def run_my_mp4_playlist():
    print(my_mp4_playlist("D:/My_Programming/Python/Data/songs.txt",
                          "D:/My_Programming/Python/Data/songs2.txt",
                          "Python Love Story;Instrumental;Unknown;4:15"))
    # Tudo Bom;Static and Ben El Tavori;5:13;
    # I Gotta Feeling;The Black Eyed Peas;4:05;
    # Python Love Story;Unknown;4:15;
    # Paradise;Coldplay;4:23;
    # Where is the love?;The Black Eyed Peas;4:13;

def main():
    run_my_mp4_playlist()

if __name__ == "__main__":
    main()
