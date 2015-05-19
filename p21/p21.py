def divisors_for_number(n):
    divisors = []
    i = 1
    while i < n:
        if n % i == 0:
            divisors.append(i)
        i = i + 1
    return divisors

def sum_of_proper_divisors(n):
    '''d(n)'''
    return sum(divisors_for_number(n))

def has_amicable_pair(n):
    b = sum_of_proper_divisors(n)
    a = sum_of_proper_divisors(b)
    if a != b and n == a:
        return True
    else:
        return False

def find_amicable_pairs():
    pairs = []
    for k in range(1,10001):
        if has_amicable_pair(k) and k not in pairs:
            pairs.append(k)
            pairs.append(sum_of_proper_divisors(k))
    return pairs

if __name__ == '__main__':
    print(sum(find_amicable_pairs()))
