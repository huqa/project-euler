# Slow brute-force method
def is_pandigital_from_1_to_9(mc, mp, p):
    '''Are the numbers pandigital? mc - multiplicand, mp - multiplier, p - product'''
    digits = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for m in str(mc):
        if m == '0':
            return False
        else:
            digits[int(m)] += 1
    for m in str(mp):
        if m == '0':
            return False
        else:
            digits[int(m)] += 1
    for m in str(p):
        if m == '0':
            return False
        else:
            digits[int(m)] += 1
    for d in digits:
        if digits[d] != 1:
            return False
    return True

if __name__ == '__main__':
    all_products = []
    for a in range(1,10000):
        for b in range(a,10000):
            product = a * b
            if is_pandigital_from_1_to_9(a, b, product):
                if product not in all_products:
                    all_products.append(product)

    print(sum(all_products))
