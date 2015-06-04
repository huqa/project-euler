
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    if n < 10:
        return is_prime(n)
    number = str(n)
    temp = ""
    while temp != str(n):
        if is_prime(int(number)):
            temp = number[1:] + number[0]
            number = temp
        else:
            return False
    return True

if __name__ == '__main__':
    circular_primes = []
    for i in range(2,1000000):
        if is_circular_prime(i):
            circular_primes.append(i)

    print(circular_primes)
    print(len(circular_primes))
