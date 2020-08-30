
guess_numer = 42
user_input = -1

# test
# test2
while (user_input != guess_numer):
    print("Please enter number")
    user_input_str = input()

    try:
        user_input = int(user_input_str)
    except ValueError:
        print("Illegal value. Try again")
        continue

    # is_correct = (user_input == guess_numer)
    # print(is_correct)

    if user_input == guess_numer:
        print("correct")
    elif user_input < guess_numer:
        print("Guess higher")
    else:
        print("Guess lower")

