
def is_pandigital(p):
    '''Are the numbers pandigital? mc - multiplicand, mp - multiplier, p - product'''
    digits = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for m in p:
        if m == '0':
            return False
        else:
            digits[int(m)] += 1
    for d in digits:
        if digits[d] != 1:
            return False
    return True

if __name__ == '__main__':
    # our fixed digit must be at most 4 digits, because 5 digits yield a number greater than 9 digits
    # the hint suggests the the fixed number should start with a 9
    # four digit integers usually yield a 9 digit number for number 2
    largest_pandigital = 0
    for i in range(10000,9000, -1):
        number = str(i) + str(i*2)
        if is_pandigital(number):
            if int(number) > largest_pandigital:
                largest_pandigital = int(number)
    print(largest_pandigital)
