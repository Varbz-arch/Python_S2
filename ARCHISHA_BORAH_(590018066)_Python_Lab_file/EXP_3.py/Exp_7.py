#Write a program which takes any date as input and display next date of the calendar 
# e.g. 
# I/P: day=20 month=9 year=2005  
# O/P: day=21 month=9 year 2005 

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def next_date(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        days_in_month[1] = 29
    day += 1
    if day > days_in_month[month -1]:
        day = 1 
        month += 1
    if month > 12:
            month = 1  
            year += 1 
    return day, month, year
day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))
next_day, next_month, next_year = next_date(day, month, year)
print(f"Next date is: day={next_day} month={next_month} year={next_year}")
