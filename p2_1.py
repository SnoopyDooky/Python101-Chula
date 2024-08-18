month, year = [int(e) for e in input().split()]
year -= 543  # C.E.
if month == 2:  # February
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(29)
    else:
        print(28)
elif month in [4, 6, 9, 11]:  # April, June, September, November
    print(30)
else:
    print(31)
