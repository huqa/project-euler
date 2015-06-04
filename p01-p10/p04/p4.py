
def three_digit_palindrome():
    largest_palindrome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            number = i * j
            if str(number) == str(number)[::-1] and number > largest_palindrome:
                largest_palindrome = number
    return largest_palindrome


if __name__ == '__main__':
    print three_digit_palindrome()

