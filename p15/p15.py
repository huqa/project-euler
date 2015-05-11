
def calculate_binomial_coefficients(i,j):
    '''Number of paths in i x j grid is ((i+j) choose j).
    because the grid is square one can choose j or i.
    i moves down, j moves right in any order. So there are i + j moves in total.'''

    n = 1
    for g in range(1,(i+j)+1):
        n = g * n

    k = 1
    for h in range(1,j+1):
        k = h * k

    nk = 1
    for r in range(1,((i+j)-j)+1):
        nk = r * nk

    return n/(k*nk)
    

if __name__ == '__main__':
    print calculate_binomial_coefficients(20,20)
