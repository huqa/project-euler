
def divisors_for_number(n):
    divisors = []
    i = 1
    while i < n:
        if n % i == 0:
            divisors.append(i)
        i = i + 1
    return divisors

def is_perfect(divisors, n):
    if sum(divisors) == n:
        return True
    else:
        return False

def is_deficient(divisors, n):
    if sum(divisors) < n:
        return True
    else:
        return False

def is_abundant(divisors, n):
    if sum(divisors) > n:
        return True
    else:
        return False

if __name__ == '__main__':
    # This method produces the correct result but is very slow
    abundant_integers = []
    for i in range(1,28124):
        if is_abundant(divisors_for_number(i), i):
            abundant_integers.append(i)

    print("Found abundant integers")    
    summed_abundants = []
    j = 0
    for k in abundant_integers:
        ai = abundant_integers[j:]
        for l in ai:
            summed = k + l
            if summed > 28123:
                break
            if summed not in summed_abundants:
                summed_abundants.append(summed)
        j = j + 1
    
    print("Summed abundants")
    non_abundant_sum_integers = []
    for i in range(1,28124):
        if i not in summed_abundants:
            non_abundant_sum_integers.append(i)

    #print(non_abundant_sum_integers)
    print(sum(non_abundant_sum_integers))

