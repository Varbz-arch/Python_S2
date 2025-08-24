'''Create a dictionary of n persons where key is name and value is city.  
a) Display all names 
b) Display all city names 
c) Display student name and city of all students. 
d) Count number of students in each city. '''

n = int(input("Enter number of persons: "))
persons = {}
for i in range(n):
    name = input(f"Enter name of person {i+1}: ")
    city = input(f"Enter city of {name}: ")
    persons[name] = city
print("Names:", list(persons.keys()))
print("Cities:", list(set(persons.values())))
for name, city in persons.items():
    print(name, "lives in", city)
city_count = {}
for city in persons.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Number of students in each city:", city_count)