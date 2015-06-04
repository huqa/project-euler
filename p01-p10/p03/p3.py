
def prime_fact(n, i):
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

if __name__ == '__main__':
    print prime_fact(600851475143, 2)

