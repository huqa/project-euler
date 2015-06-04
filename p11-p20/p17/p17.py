SINGLES = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
}

TENS = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

HUNDREDS_THOUSANDS = {
        1: 'hundred', 
        2: 'thousand'
}

AND = 'and'

def number_letters(n):
    letters = ""
    if n == 1000:
        letters = SINGLES[1] + HUNDREDS_THOUSANDS[2]
    elif n < 1000:
        numbers = str(n)
        amount = len(numbers)
        if amount == 3:
            hundreds = int(numbers[0])
            tens = int(numbers[1])
            ones = int(numbers[2])
            letters = SINGLES[hundreds] + HUNDREDS_THOUSANDS[1]
            if tens > 1:
                letters += AND + TENS[tens]
                if ones != 0:
                    letters += SINGLES[ones]
            elif tens == 1:
                letters += AND + SINGLES[int(numbers[1] + numbers[2])]
            else:
                # tens is zero
                if ones != 0:
                    letters += AND + SINGLES[ones]
        elif amount == 2:
            tens = int(numbers[0])
            ones = int(numbers[1])
            if tens > 1:
                letters += TENS[tens]
                if ones != 0:
                    letters += SINGLES[ones]
            elif tens == 1:
                letters += SINGLES[int(numbers[0] + numbers[1])]
        else:
            # only one number
            ones = int(numbers[0])
            letters = SINGLES[ones]

    return letters


if __name__ == '__main__':
    letter_sum = 0
    for i in range(1,1001):
        letter_sum += len(number_letters(i))

    print letter_sum
