# Number spiral diagonals

def calculate_diagonal_values(n):
    spiral_size = (n*n)
    diagonal_values = { 'se': [3], 'sw': [5], 'nw': [7], 'ne': [9] }
    start_value_sums = { 'se': [2], 'sw': [4], 'nw': [6], 'ne': [8] }
    idx = 0
    # northeast has the maximum value of the spiral
    ne_val = 0

    while ne_val != spiral_size:
        se_sum = (start_value_sums['se'][idx] + 8)
        start_value_sums['se'].append(se_sum)
        diagonal_values['se'].append(diagonal_values['se'][idx] + se_sum)

        sw_sum = (start_value_sums['sw'][idx] + 8)
        start_value_sums['sw'].append(sw_sum)
        diagonal_values['sw'].append(diagonal_values['sw'][idx] + sw_sum)

        nw_sum = (start_value_sums['nw'][idx] + 8)
        start_value_sums['nw'].append(nw_sum)
        diagonal_values['nw'].append(diagonal_values['nw'][idx] + nw_sum)

        ne_sum = (start_value_sums['ne'][idx] + 8)
        start_value_sums['ne'].append(ne_sum)
        ne_val = diagonal_values['ne'][idx] + ne_sum
        diagonal_values['ne'].append(ne_val)

        idx += 1


    diagonal_sums = []
    for key in diagonal_values:
        diagonal_sums.append(sum(diagonal_values[key]))

    return sum(diagonal_sums)+1

if __name__ == '__main__':
    print(calculate_diagonal_values(1001))


