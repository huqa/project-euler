

def pentagonal_number(n):
    return n*((3*n)-1)/2

def pentagonal_index(p):
    return ((((24*p+1)**.5)+1)/6)

def has_pentagonal_sum(pj, pk):
    return pentagonal_index(pk+pj).is_integer()

def has_pentagonal_difference(pj, pk):
    return pentagonal_index(find_D(pj, pk)).is_integer()

def find_D(pj, pk):
    return abs(pk-pj)


if __name__ == '__main__':
    found_d = 0
    pair = [[0,0]]
    for j in range(1,4000):
        for k in range(1,4000):
            pj = pentagonal_number(j)
            pk = pentagonal_number(k)
            if has_pentagonal_sum(pj, pk) and has_pentagonal_difference(pj, pk):
                found_d = find_D(pj, pk)
                pair[0] = (pj, pk)
                break
    print(found_d)
    print(pair)
