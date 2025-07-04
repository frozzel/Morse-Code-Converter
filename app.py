import mcode

MORSE_CODE_DICT = mcode.MORSE_CODE_DICT

def morse_to_text(morse_code):
    morse_words = morse_code.split(' / ')
    decoded_message = []
    
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        decoded_word = ''.join(
            next((char for char, code in MORSE_CODE_DICT.items() if code == m), '') 
            for m in morse_chars
        )
        decoded_message.append(decoded_word)
    
    return print(' '.join(decoded_message))

def text_to_morse(text):
    code = ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)
    morse_to_text(code)
    return print(code)

text_to_morse("Hello, World!")  # Example usage, you can replace with any string
# This will print the Morse code equivalent of "Hello, World!"
