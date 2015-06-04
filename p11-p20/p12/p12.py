

def generate_triangle_number(n):
    return sum([i for i in range(1,n+1)])

def factorize(n):
    factors = []
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)
    return factors

def find_triangle_number_with_divisors(n):
    c = 1
    while True:
        tn = generate_triangle_number(c)
        fact_no = len(factorize(tn))
        if fact_no > n:
            return tn
        c = c + 1

if __name__ == '__main__':
    print(find_triangle_number_with_divisors(500))

