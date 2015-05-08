def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number-1) + fib(number-2)


if __name__ == '__main__':
    even_sum = 0
    for i in range(1,34):
        term = fib(i)
        if term % 2 == 0:
            even_sum += term

    #print fib(33)
    print even_sum
