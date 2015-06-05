
def find_triplets_for_perimeter(p):
    triplets = []
    # because a <= b < c, we can assume that a < p/3
    for a in range(2,p/3):
        b = ((p**2.0) - (2.0*p*a)) / ((2.0*p)-(2.0*a))
        if b.is_integer():
            c = p - a - b
            if c.is_integer():
                triplets.append((int(a),int(b),int(c)))
    return triplets



if __name__ == '__main__':
    max_triplets = 0
    longest_p = 0
    for p in range(1,1001):
        l = len(find_triplets_for_perimeter(p))
        if l > max_triplets:
            max_triplets = l
            longest_p = p
    print(max_triplets)
    print(longest_p)
