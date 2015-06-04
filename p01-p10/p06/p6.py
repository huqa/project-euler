
def sum_square_difference(upper_limit):
    summed_no = 0
    summed_squares = 0
    for i in range(1,upper_limit+1):
        summed_no += i
        summed_squares += i ** 2
    square_of_sum = summed_no ** 2
    return square_of_sum - summed_squares

if __name__ == '__main__':
    print sum_square_difference(100)

