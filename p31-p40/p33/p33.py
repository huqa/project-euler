
def greatest_common_divisor(a,b):
    x = 0
    y = 0

    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    while x % y != 0:
        tmp = x
        x = y
        y = tmp % x

    return y

def find_common_digit(n, d):
    for i in str(n)[::-1]:
        for k in str(d)[::-1]:
            if i == k:
                return int(i)
    return -1

def remove_common_digit(number, digit):
    idx = number.find(digit)
    return number[:idx] + number[idx+1:]

def find_digit_cancelling_fractions():
    nominators = []
    denominators = []
    for n in range(10,100):
        for d in range(10,100):
            if n % 10 != 0 and d % 10 != 0:
                cd = find_common_digit(n, d)
                if cd != -1:
                    expected = n / float(d)
                    if expected < 1:
                        rn = remove_common_digit(str(n), str(cd))
                        rd = remove_common_digit(str(d), str(cd))
                        result = float(rn) / float(rd)
                        if result == expected:
                            nominators.append(n)
                            denominators.append(d)
    return nominators, denominators

if __name__ == '__main__':
    nom, denom = find_digit_cancelling_fractions()
    nom_prod = 1
    denom_prod = 1
    for n in nom:
        nom_prod *= n
    for d in denom:
        denom_prod *= d

    gcd = greatest_common_divisor(nom_prod,denom_prod)
    print(denom_prod/gcd)
