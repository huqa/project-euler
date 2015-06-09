
def triangle_number(n):
    return (n*(n+1))/2

def triangle_index(t):
    return 0.5 * (((8*t + 1)**0.5) - 1)

def is_triangle_number(n):
    return triangle_index(n).is_integer()

def pentagonal_index(p):
    return ((((24*p+1)**.5)+1)/6)

def is_pentagonal_number(n):
    return pentagonal_index(n).is_integer()

def hexagonal_index(h):
    return ((((8*h + 1)**.5)+1)/4)

def is_hexagonal_number(n):
    return hexagonal_index(n).is_integer()

if __name__ == '__main__':
    t_number = 0
    for n in xrange(286, 500000):
        t = triangle_number(n)
        if is_pentagonal_number(t) and is_hexagonal_number(t):
            t_number = t
            break
    print(t_number)


    
