#1
# Check whether given number is divisible by 3 and 5 both.

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"The number {number} is divisible by both 3 and 5.")
else:
    print(f"The number {number} is not divisible by both 3 and 5.")

#2
#Check whether a given number is multiple of five or not. 

number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"The number {number} is a multiple of five.")
else:
    print(f"The number {number} is not a multiple of five.")

#3
#Find the greatest among two numbers. If numbers are equal than print 
# “numbers are equal”. 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The greatest number is {num1}.")
elif num2 > num1:
    print(f"The greatest number is {num2}.")
else:
    print("Numbers are equal.")

#4
#Find the greatest among three numbers assuming no two values are same.  

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(f"The greatest number is {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"The greatest number is {num2}.")
else:
    print(f"The greatest number is {num3}.")

#5
#Check whether the quadratic equation has real roots or imaginary roots. 
#Display the roots. 

import math
a = int(input("Enter coefficient a (non-zero): "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter constant c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Real and distinct roots: {r1:.2f}, {r2:.2f}")
elif d == 0:
    r = -b / (2*a)
    print(f"Real and equal roots: {r:.2f}")
else:
    real = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Imaginary roots: {real:2f} + {imaginary_part:.2f}i, {real:.2f} - {imaginary_part:.2f}i")

#6
#Find whether a given year is a leap year or not. 

year=int(input("Enter the year"))
if((year%4==0) and (year%100!=0)) or (year%400==0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")

#7
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
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
next_day, next_month, next_year = next_date(day, month, year)
print(f"Next date is: day={next_day} month={next_month} year={next_year}")

#8
#Print the grade sheet of a student for the given range of cgpa. Scan marks of 
#five subjects and calculate the percentage. 

def get_grade(cgpa):
    if cgpa <= 3.4:
        return "F"
    elif 3.5 <= cgpa <= 5.0:
        return "C+"
    elif 5.1 <= cgpa <= 6.0:
        return "B"
    elif 6.1 <= cgpa <= 7.0:
        return "B+"
    elif 7.1 <= cgpa <= 8.0:
        return "A"
    elif 8.1 <= cgpa <= 9.0:
        return "A+"
    else:
        return "O (Outstanding)"
name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter semester: ")
course = input("Enter course: ")
subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = total_marks / 5
cgpa = percentage / 10
grade = get_grade(cgpa)

print("\nGrade Sheet:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}\tSAPID: {sapid}")
print(f"Sem: {sem}\tCourse: {course}")
print("\nSubject name: Marks")
for subject, mark in zip(subjects, marks):
    print(f"{subject}:   {mark}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.2f}")
print(f"Grade: {grade}")