
def first_of_the_month_sundays():
    year = 1900
    day = 1
    current_month = 1
    i = 1
    fom_sundays = 0
    while year <= 2000:
        
        month = get_month(day, year)
        if month != current_month:

            current_month = month
            # first of the month
            if i % 7 == 0 and year > 1900:
                fom_sundays = fom_sundays + 1

        if day == 365 and not is_leap(year):
            year = year + 1
            day = 1
            month = 1
        elif day == 366 and is_leap(year):
            year = year + 1
            day = 1
            month = 1
        else:
            day = day + 1

        i = i + 1

    return fom_sundays            


def is_leap(year):
    if year % 100 == 0:
        # centuries
        if year % 400 == 0:
            #leap century
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            # leap year
            return True
        else:
            return False


def get_month(day, year):
    if is_leap(year):
        if day >= 1 and day <= 31:
            return 1
        elif day > 31 and day <= 60:
            return 2
        elif day > 60 and day <= 91:
            return 3
        elif day > 91 and day <= 121:
            return 4
        elif day > 121 and day <= 152:
            return 5
        elif day > 152 and day <= 182:
            return 6
        elif day > 182 and day <= 213:
            return 7
        elif day > 213 and day <= 244:
            return 8
        elif day > 244 and day <= 274:
            return 9
        elif day > 274 and day <= 305:
            return 10
        elif day > 305 and day <= 335:
            return 11
        elif day > 335 and day <= 366:
            return 12
        else:
            return 0
    else:
        if day >= 1 and day <= 31:
            return 1
        elif day > 31 and day <= 59:
            return 2
        elif day > 59 and day <= 90:
            return 3
        elif day > 90 and day <= 120:
            return 4
        elif day > 120 and day <= 151:
            return 5
        elif day > 151 and day <= 181:
            return 6
        elif day > 181 and day <= 212:
            return 7
        elif day > 212 and day <= 243:
            return 8
        elif day > 243 and day <= 273:
            return 9
        elif day > 273 and day <= 304:
            return 10
        elif day > 304 and day <= 334:
            return 11
        elif day > 334 and day <= 365:
            return 12
        else:
            return 0

if __name__ == '__main__':
    print("First of the month sundays 1901-2000: %d" % first_of_the_month_sundays())
    
