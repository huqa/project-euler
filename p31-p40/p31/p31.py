#coin sums
N = 200
S = [1,2,5,10,20,50,100,200]

def change():
    change = [1] + [0] * N
    for coin in S:
        for i in range(coin, N+1):
            change[i] += change[i-coin]
    return change


if __name__ == '__main__':

    print(change()[N])
