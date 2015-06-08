
FILENAME = 'p042_words.txt'

LETTERS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def word_to_value(word):
    value = 0
    for n in word:
        value += LETTERS[n]
    return value

def find_triangle_number(value):
    # n = (1/2)*(sqrt(8*t+1)-1)
    return 0.5 * (((8*value + 1)**0.5) - 1)

def is_triangle_word(word):
    return find_triangle_number(word_to_value(word)).is_integer()

if __name__ == '__main__':
    total_triangle_words = 0
    words = []
    with open(FILENAME, 'rb') as f:
        for line in f:
            words = line.split(",")

    for word in words:
        word = word.strip('\n').replace('\"', '')
        if is_triangle_word(word):
            total_triangle_words += 1

    print(total_triangle_words)
