
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def digit_factorial_sum(n):
    facts = 0
    for i in str(n):
        facts += factorial(int(i))
    return facts


if __name__ == '__main__':
    numbers = []
    # chosen some arbritrary upper limit
    for i in range(3,100000):
        if i == digit_factorial_sum(i):
            numbers.append(i)

    print numbers
    print(sum(numbers))

