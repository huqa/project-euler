def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    total = 0
    digits = str(n)
    for k in digits:
        total += int(k)
    return total

if __name__ == '__main__':
    print(sum_of_digits(factorial(100)))
