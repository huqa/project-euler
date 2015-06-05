
# I'm a brute
def d(n):
    d = "0"
    i = 1
    while len(d) <= n:
        d = d + str(i)
        i = i + 1
    return d


if __name__ == '__main__':
    # oh dog, make it stop
    d = d(1000000)
    print(int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000]))
