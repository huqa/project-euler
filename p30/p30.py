#Digit fifth powers

# set hand calculated upper limit ~ 6*9^5
UPPER_LIMIT = 356000

def digit_fifth_power_sums():
    result = 0
    for i in range(2,UPPER_LIMIT):
        sum_of_powers = 0
        number = str(i)
        for n in number:
            sum_of_powers += int(n) ** 5
        if sum_of_powers == i:
            result += sum_of_powers

    return result

if __name__ == '__main__':
    print("Sum of numbers in fifth power: %d" % digit_fifth_power_sums())
