
def is_pandigital(p,n):
    '''Is the number p pandigital 1 through n?'''
    digits = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for m in p:
        if m == '0':
            return False
        else:
            digits[int(m)] += 1
    for d in range(1,n+1):
        if digits[d] != 1:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n**.5)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # every pandigital 8 or 9-digit number is divisible by 3
    largest_pandigital_prime = 0
    # so let's start with the largest seven digit pandigital number
    for i in xrange(7654321, 2000, -1):
        if is_pandigital(str(i), len(str(i))):
            if is_prime(i):
                largest_pandigital_prime = i
                # no need to continue because we started at largest pandigital number and worked our way to the prime
                break
    print(largest_pandigital_prime)
