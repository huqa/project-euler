
def power_digit_sum(n,k):
    power = n ** k
    power_as_string = str(power)
    return sum([int(i) for i in power_as_string])

if __name__ == '__main__':
    print power_digit_sum(2,1000)

