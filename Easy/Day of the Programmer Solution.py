def solve(year):
    if year > 1918:
        if year%4 == 0 and year%100 != 0:
            day_of_the_programmer = "12.09." + str(year)
        elif year%400 == 0:
            day_of_the_programmer = "12.09." + str(year)

        else: 
            day_of_the_programmer = "13.09." + str(year)
    elif year < 1918:
        if year%4 == 0: 
            day_of_the_programmer = "12.09." + str(year)
        else: 
            day_of_the_programmer = "13.09." + str(year)
    elif year == 1918:
           day_of_the_programmer = "26.09." + str(year)
    return(day_of_the_programmer)
year = int(input().strip())
result = solve(year)
print(result)
