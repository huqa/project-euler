def smallest_evenly_divisible(limit):
    n = 1
    while True:
        if _evenly_divisible(n, limit):
            return n
        else:
            n = n + 1

def _evenly_divisible(n, limit):
    for i in range(1, limit+1):
        if n % i != 0:
            return False
    return True

if __name__ == '__main__':
    print smallest_evenly_divisible(20)
