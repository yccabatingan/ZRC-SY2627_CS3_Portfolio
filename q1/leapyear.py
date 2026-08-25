def isLeapYear(year):
    leapYear = year

    if leapYear % 400 == 0:
        return True
    elif leapYear % 100 == 0:
        return False
    elif leapYear % 4 == 0:
        return True
    else:
        return False
year = int(input("Enter a year: "))

result = isLeapYear(year)

if result:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")