
current_year = 2023  
num_of_leap_years = 5  
leap_years = []
year = current_year + 1  
while len(leap_years) < num_of_leap_years:

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)
    year += 1

print(f"The next {num_of_leap_years} leap years after {current_year} are: {leap_years}")
