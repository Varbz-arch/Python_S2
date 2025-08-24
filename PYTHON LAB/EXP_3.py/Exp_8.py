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
