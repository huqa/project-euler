
def calculate_sequence(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return (3*n)+1

def collatz_sequence(n, steps):
    steps = steps + 1
    if n != 1:
        k = calculate_sequence(n)
        return collatz_sequence(k, steps)
    else:
        return steps

if __name__ == '__main__':
    longest_step = 0
    starting_number = 0
    starting_number = 999999
    steps = 0
    for i in range(starting_number, 0, -1):
        steps = collatz_sequence(i, 0)
        if steps > longest_step:
            longest_step = steps
            starting_number = i

    print("Longest step %d" % longest_step)
    print("Starting number %d" % starting_number)

