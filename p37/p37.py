
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

def is_prime_remove_digits_lr(n):
    tmp = str(n)
    while len(tmp) > 1:
        tmp = tmp[1:]
        if not is_prime(int(tmp)):
            return False
    return True

def is_prime_remove_digits_rl(n):
    tmp = str(n)
    while len(tmp) > 1:
        tmp = tmp[:len(tmp)-1]
        if not is_prime(int(tmp)):
            return False
    return True

if __name__ == '__main__':
    trunc_primes = []
    for i in range(11,1000000):
        if len(trunc_primes) == 11:
            break
        if is_prime(i):
            if is_prime_remove_digits_lr(i) and is_prime_remove_digits_rl(i):
                trunc_primes.append(i)

    print(trunc_primes)
    print(sum(trunc_primes))
