

def generate_triplet(n):
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c2 = a**2 + b**2
            c = int(c2**0.5)
            if (c2 == c**2) and (c <= n):
                yield (a,b,c)


if __name__ == '__main__':
    for a,b,c in generate_triplet(1000):
        if a+b+c == 1000:
            print a,b,c
            print a*b*c
            break
