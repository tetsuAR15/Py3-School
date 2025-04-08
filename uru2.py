for year in range(1950, 2101):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "True")
    else:
        print(year, "False")
