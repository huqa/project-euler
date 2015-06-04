
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

def find_permutation(n):
    i = 1
    permutation = [0,1,2,3,4,5,6,7,8,9]
    while i < n:
        permutation = get_next_permutation(permutation)
        i = i + 1

    return permutation
    

if __name__ == '__main__':
    print(find_permutation(1000000))
    
    
