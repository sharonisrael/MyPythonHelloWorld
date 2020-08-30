
HANGMAN_ASCII_ART = """
     _    _
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                     
                         |___/                      
    """

MAX_TRIES = 6

def print_start():
    print(HANGMAN_ASCII_ART)

def print_start2():
    print("_    _                                          ")
    print("| |  | |                                        ")
    print("| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| |  | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                      __/ |                     ")
    print("                     |___/                      ")
    print("")

def print_hangman(num_of_tries):
    if num_of_tries == 1:
        picture_1()
    elif num_of_tries == 2:
        picture_2()
    elif num_of_tries == 3:
        picture_3()
    elif num_of_tries == 4:
        picture_4()
    elif num_of_tries == 5:
        picture_5()
    elif num_of_tries == 6:
        picture_6()

def picture_1():
    print("x-------x")

def picture_2():
    print("x-------x")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

def picture_3():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|")
    print("|")
    print("|")

def picture_4():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|       |")
    print("|")
    print("|")

def picture_5():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|      /|\\")
    print("|")
    print("|")

def picture_6():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|      /|\\")
    print("|      /")
    print("|")

def picture_7():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|      /|\\")
    print("|      / \\")
    print("|")

def ask_letter():
    given_letter = input("Guess a letter: ")
    # print("Guess a letter: ", given_letter)
    return given_letter

def ask_and_change_to_underscope(given_word):
    undescore_word = "_ " * len(given_word)
    print(undescore_word)

def check_input(given_letter):
    given_letter_str = given_letter
    too_many_letters = len(given_letter_str) > 1
    # print("len(given_word_str) " + given_letter_str, len(given_letter_str), too_many_letters, given_letter)
    if (too_many_letters and not given_letter_str.isalpha()):
        print("E3")
    elif too_many_letters:
        print("E1")
    elif not given_letter_str.isalpha():
        print("E2")
    else:
        print(given_letter_str.lower())

def is_valid_input(given_letter):
    return len(given_letter) == 1 and given_letter.isalpha()

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    :param str letter_guessed:
    :param list old_letters_guessed:
    :rtype: bool
    """
    legal_value = is_valid_input(letter_guessed)
    new_guess = letter_guessed.lower() not in old_letters_guessed
    return legal_value and new_guess

def run_check_valid_input():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))
    print(check_valid_input('ep', old_letters))
    print(check_valid_input('$', old_letters))
    print(check_valid_input('s', old_letters))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed.lower())
        print(old_letters_guessed)
        return True
    else:
        print("X")
        print(' -> '.join(sorted(old_letters_guessed)))
        return False

def run_try_update_letter_guessed():
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))
    # X
    # a -> c -> f -> p
    # False
    print(try_update_letter_guessed('s', old_letters))
    # True
    # old_letters
    # ['a', 'p', 'c', 'f', 's']
    print(try_update_letter_guessed('$', old_letters))
    # X
    # a -> c -> f -> p -> s
    # False
    print(try_update_letter_guessed('d', old_letters))
    # True
    # old_letters
    # ['a', 'p', 'c', 'f', ‘s’, 'd']

def show_hidden_word(secret_word, old_letters_guessed):
    word_status = ""
    for i in range(len(secret_word)-1):
        if secret_word[i] not in old_letters_guessed:
            word_status += "_ "
        else:
            word_status += secret_word[i] + " "

    # remove last space
    my_list = list(word_status)
    my_list[-1] = ""
    word_status = ''.join(my_list)

    # word_status = secret_word
    # for letter in word_status:
    #     if letter not in old_letters_guessed:
    #         word_status = word_status.replace(letter, "_")
    return word_status

def run_show_hidden_word():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

def check_win(secret_word, old_letters_guessed):
    word_status = secret_word
    for letter in word_status:
        if letter in old_letters_guessed:
            word_status = word_status.replace(letter, "")
    return word_status == ""

def run_check_win():
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))


def run_game():
    print_start()

    # given_letter = ask_letter()
    # check_valid_input(given_letter)
    # ask_letter()
    # run_try_update_letter_guessed()
    # run_show_hidden_word()
    run_check_win()

run_game()