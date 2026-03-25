MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}
code_or_decode = int(input("option 1: code to Morse option 2: decode to text, Select your option: "))
if code_or_decode == 1:
    to_code = input("What word would you like to code: \n")
    cleaned_code = ' '.join(to_code.split())
    new = []

    for char in cleaned_code.upper():
        if char in MORSE_CODE_DICT:
            new.append(MORSE_CODE_DICT[char])
        else:
            if char == " ":
             new.append("/")

    print(' '.join(new))

elif code_or_decode == 2:
    to_decode = input("What word would you like to decode: \n")
    cleaned_code = to_decode.split()
    new = []

    for morse in cleaned_code:
        if morse != "/":
            for char, value in MORSE_CODE_DICT.items():
                if morse==value:
                    new.append(char)
        else:
            new.append("/")

    print(''.join(new).replace('/',' '))