
SEQUENCE = [2,3,5,7,11,13,17]

def get_substring_digits(number):
    substrings = []
    snumber = str(number)
    for i in xrange(1,8):
        substrings.append(int(snumber[i] + snumber[i+1] + snumber[i+2]))
    return substrings

def has_interesting_property(substrings):
    i = 0
    for s in substrings:
        if s % SEQUENCE[i] != 0:
            return False
        i += 1
    return True

def is_pandigital(p):
    '''Is p pandigital from 0 to 9?'''
    digits = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for m in p:
        digits[int(m)] += 1
    for d in digits:
        if digits[d] != 1:
            return False
    return True

def find_largest_index_k(permutation):
    k = 0
    largest_k = -1
    while k < len(permutation):
        if k == len(permutation)-1:
            return largest_k
        if permutation[k] < permutation[k+1]:
            largest_k = k
        k = k + 1

def find_largest_index_l(permutation, k):
    l = k
    largest_l = 0
    while l < len(permutation):
        if permutation[k] < permutation[l]:
            largest_l = l
        l = l + 1
    return largest_l

def swap_k_with_l(permutation, k, l):
    val_k = permutation[k]
    val_l = permutation[l]
    permutation[k] = val_l
    permutation[l] = val_k
    return permutation

def reverse_sequence(permutation, k):
    permutation[k+1:] = permutation[k+1:][::-1]
    return permutation

def get_next_permutation(permutation):
    k = find_largest_index_k(permutation)
    if k == -1:
        # -1 means no k has been found, so it's the final permutation
        return permutation
    l = find_largest_index_l(permutation, k)
    permutation = swap_k_with_l(permutation, k, l)
    return reverse_sequence(permutation, k)

def list_to_integer(p):
    k = ""
    for i in p:
        k += str(i)
    return int(k)

if __name__ == '__main__':
    number_sums = 0
    permutation = [0,1,2,3,4,5,6,7,8,9]
    n = 1
    # 10!
    while n < 3628800:
        permutation = get_next_permutation(permutation)
        i = list_to_integer(permutation)
        if is_pandigital(str(i)):
            if has_interesting_property(get_substring_digits(i)):
                print(i)
                number_sums += i
        n += 1
    print(number_sums)
