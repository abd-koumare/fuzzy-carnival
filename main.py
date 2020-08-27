

if __name__ == '__main__':

    print('1/1/2000-Saturday\n1/1/2100-Friday\n1/1/2200-Wednesday\n1/1/2300-Monday')

    num_of_leap, year = 0, 2000
    for x in range(year, year + 400):
        if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
            num_of_leap += 1

    num_of_non_leap = 400 - num_of_leap
    print(f'leap year: {num_of_leap} | non-leap year: {num_of_non_leap}')

    num_of_days = 400 * 365 + num_of_leap  # +97 because of leap days

    divisible_by_seven, human_readable_result = (True, 'divisible by 7') if num_of_days % 7 == 0 else (False, 'not divisible by 7')

    print(f'400 x 365 + 97 = {num_of_days} days which is {human_readable_result}')

    if divisible_by_seven:
        print('Prove that every 400 years we fall on the same day, So guess the next 1/1/2400-? :)')
    else:
        print("Prove that every 400 years we don't fall on the same day")

