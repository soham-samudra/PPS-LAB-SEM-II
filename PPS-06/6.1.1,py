# Function to check leap year
def is_leap_year(year):
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_valid_date(day, month, year):
    if year <= 0:
        return False
    if month < 1 or month > 12:
        return False


    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        if is_leap_year(year):
            max_days = 29
        else:
            max_days = 28

    if day < 1 or day > max_days:
        return False

    return True


def next_date(day, month, year):

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        if is_leap_year(year):
            max_days = 29
        else:
            max_days = 28

    day += 1

    if day > max_days:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    return day, month, year


day = int(input())
month = int(input())
year = int(input())


if is_valid_date(day, month, year):
    d, m, y = next_date(day, month, year)
    print(f"{d:02d}-{m:02d}-{y}")
else:
    print("Invalid Date")
