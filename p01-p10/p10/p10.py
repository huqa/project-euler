
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

def sum_primes(k):
    i = 0
    sum_of_primes = 0
    while True:
        if i < k:
            if is_prime(i):
                sum_of_primes += i
        else:
            return sum_of_primes
        i = i + 1

if __name__ == '__main__':
    print sum_primes(2000000)

