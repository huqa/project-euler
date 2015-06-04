# Quadratic primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

def find_consecutive_primes(a,b):
    n = 0
    while is_prime(abs((n**2) + (a*n) + (b))):
        n += 1
    return n

if __name__ == '__main__':
    largest_count = 0
    coeff_a = 0
    coeff_b = 0
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            count = find_consecutive_primes(a,b)
            if largest_count < count:
                largest_count = count
                coeff_a = a
                coeff_b = b
                #print("Largest prime count now %d with a: %d  b: %d" % (largest_count, coeff_a, coeff_b))
    print("Largest prime count: %d With coefficients a: %d and b: %d. Product of coefficients: %d" % (largest_count, coeff_a, coeff_b, (coeff_a*coeff_b)))

