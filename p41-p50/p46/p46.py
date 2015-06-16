def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

def twice_a_square(n):
    t = (n/2.0)**.5
    return int(t) == t

if __name__ == '__main__':
    primes = [2]
    i = 1
    searching = True
    while searching:
        i += 2
        
        # if the odd number is a prime, append it to the list of primes
        if is_prime(i):
            primes.append(i)
        else:
            searching = False
            for j in range(len(primes)-1,0,-1):
                if twice_a_square(i-primes[j]):
                    # still twice a square, lets keep searching
                    searching = True
                    break
    print i
