import mcode


needs_conversion = input("Enter a string to convert to Morse code: ")

for char in needs_conversion.upper():
    if char in mcode.MORSE_CODE_DICT:
        print(mcode.MORSE_CODE_DICT[char])
    else:
        print(f"Character '{char}' not found in Morse code dictionary.")