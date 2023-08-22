def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

given_year = int(input("Please enter your birthyear: "))
result = is_leap_year(given_year)
print(f"{given_year} As a leap year is {result}")
