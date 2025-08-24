#1
#Scan n values in range 0-3 and print the number of times each value has occurred. 
 
n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1} (0-3): "))
    numbers.append(num)
count_0 = numbers.count(0)
count_1 = numbers.count(1)
count_2 = numbers.count(2)
count_3 = numbers.count(3)
print("Occurrences:")
print("0:", count_0)
print("1:", count_1)
print("2:", count_2)
print("3:", count_3)

#2
#Create a tuple to store n numeric values and find average of all values. 
 
N = int(input("How many numbers?  "))
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
T = tuple(numbers)
average = sum(T) / N
print("The numbers that  you entered:", T)
print("Average of all values:", average)

#3
#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output. 
 
n = int(input("Enter number of students: "))
scores = []
for i in range(n):
    score = int(input(f"Enter score of student {i+1}: "))
    scores.append(score)
scores = list(set(scores))
if len(scores) > 1:
    temp=scores[i]
    scores[i]=scores[i-1]
    scores[i-1]=temp
    print("Runner-up score:", scores[-2])
else:
    print("No runner-up score available")

#4
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

#5
'''Store details of n movies in a dictionary by taking input from the user. Each 
movie must store details like name,  year, director name, production cost, 
collection made (earning) & perform the following :- 
a) print all movie details 
b) display name of movies released before 2015 
c) print movies that made a profit. 
d) print movies directed by a particular director. '''

n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
    name = input(f"Enter movie {i+1} name: ")
    year = int(input(f"Enter release year of {name}: "))
    director = input(f"Enter director of {name}: ")
    cost = float(input(f"Enter production cost of {name}: "))
    earning = float(input(f"Enter earnings of {name}: "))
    movies[name] = {"year": year, "director": director, "cost": cost,"earning": earning }
print("\nMovie Details:")
for name, details in movies.items():
    print(f"\nMovie: {name}")
    print("Year:", details["year"])
    print("Director:", details["director"])
    print("Production Cost:", details["cost"])
    print("Earnings:", details["earning"])
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)
print("\nProfitable movies:")
for name, details in movies.items():
    if details["earning"] > details["cost"]:
        print(name)
director_name = input("\nEnter director name to search: ")
print(f"Movies directed by {director_name}:")
for name, details in movies.items():
    if details["director"] == director_name:
        print(name)