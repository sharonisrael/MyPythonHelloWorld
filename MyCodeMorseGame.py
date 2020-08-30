morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',
                   ' ': ' / '}

my_sentence = "HELLO WORLD"
my_morse_sentence = []
my_morse_str = ""

for i in my_sentence:
    morse_code = morse_code_dict[i]
    my_morse_sentence.append(morse_code)
    my_morse_sentence.append(" ")
    my_morse_str += morse_code
    my_morse_str += " "

print(my_morse_sentence)
# joins to a sentence with blank between signs and not space or '-'
print("".join(my_morse_sentence))
print(my_morse_str)

# split the morse code by spaces
[print(morse_sign) for morse_sign in my_morse_str.split()]
