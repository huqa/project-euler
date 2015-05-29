
def integer_combinations(a_max, b_max):
    sequence = []
    for a in range(2, a_max+1):
        for b in range(2, b_max+1):
            x = a ** b
            if x not in sequence:
                sequence.append(x)
    return len(sequence)


if __name__ == '__main__':
    print(integer_combinations(100, 100))
