def find_cycle_length(d):
    cycle = []
    x = 1 % d
    cycle.append(x)
    while True:
        x = x * 10
        x = x % d
        if x == 0 or x in cycle:
            return len(cycle)
        else:
            cycle.append(x)

if __name__ == '__main__':
    largest_cycle = 0
    d = 0
    for k in range(2,1001):
        cycle = find_cycle_length(k)
        #print(cycle)
        if largest_cycle < cycle:
            largest_cycle = cycle
            d = k
    print("Largest cycle is %d for 1/%d" % (largest_cycle, d))

