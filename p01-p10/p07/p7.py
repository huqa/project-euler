import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def find_prime(k):
    idx = 0
    i = 0
    while True:
        i = i + 1
        if is_prime(i):
            idx = idx + 1
            if idx == k:
                return i

if __name__ == '__main__':
    print find_prime(10001)
            
