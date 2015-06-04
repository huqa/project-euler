
FILENAME = 'p022_names.txt'

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


def total_name_scores():
    names = []
    with open(FILENAME, 'rb') as f:
        for line in f:
            names = line.split(",")
            names.sort()

    i = 1
    total_sum = 0
    for name in names:
        name = name.strip("\n").replace('\"', '')
        name_sum = 0
        for letter in name:
            name_sum += LETTERS[letter]
        total_sum += name_sum * i
        i = i + 1
    return total_sum



if __name__ == '__main__':
    print(total_name_scores())
