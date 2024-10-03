import collections
import sys

# Braille mappings
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse map for Braille to English
ENGLISH_MAP = collections.defaultdict(list)
for k, v in BRAILLE_MAP.items():
    ENGLISH_MAP[v].append(k)

def to_braille(text: str) -> str:
    braille = ""
    is_digit_sequence = False
    
    for char in text:
        if char.isupper():
            braille += BRAILLE_MAP['cap'] + BRAILLE_MAP[char.lower()]
        elif char == ' ':
            braille += BRAILLE_MAP[' ']
            is_digit_sequence = False
        elif char.isdigit():
            if is_digit_sequence:
                braille += BRAILLE_MAP[char]
            else:
                braille += BRAILLE_MAP['num'] + BRAILLE_MAP[char]
                is_digit_sequence = True
        else:
            braille += BRAILLE_MAP[char]
            is_digit_sequence = False
            
    return braille

def to_english(braille: str) -> str:
    english = ""
    i = 0
    is_capital = False

    while i < len(braille):
        char = braille[i:i + 6]

        if char == '.....O':  # Capitalize next letter
            is_capital = True
        elif char == '.O.OOO':  # Start number sequence
            is_number = True
        elif char == '......':  # Space
            english += ' '
            is_number = False  # Reset the number flag
        else:
            letter = ENGLISH_MAP[char][1] if is_number else ENGLISH_MAP[char][0]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            english += letter

        i += 6

    return english

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(1)

    input_text = " ".join(args)
    # Determine if the input is Braille or English
    if all(c in 'O.o ' for c in input_text):
        output = to_english(input_text)
    else:
        output = to_braille(input_text)
    print(output)

if __name__ == '__main__':
    main()
