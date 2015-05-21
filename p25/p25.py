# fast doubling algorithm
def fib(n):
    # F(2k) = F(k)[2F(k+1)-F(k)]
    # F(2k+1) = F(k+1)^2 + F(k)^2
    if n == 0:
        return 0, 1
    else:
        fk, fk1 = fib(n // 2)
        f2k = fk * (2 * fk1 - fk)
        f2k1 = fk1*fk1 + fk*fk
        if n % 2 == 0:
            return f2k, f2k1
        else:
            return f2k1, f2k+f2k1

def find_1000_digit_fibonacci_index():
    i = 1 # arbritrary starting number
    while True:
        k = fib(i)[0]
        if len(str(k)) == 1000:
            return i
        i = i + 1

if __name__ == '__main__':
    #print(fib(200)[0])
    print(find_1000_digit_fibonacci_index())

