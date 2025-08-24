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
    cost = int(input(f"Enter production cost of {name}: "))
    earning = int(input(f"Enter earnings of {name}: "))
    movies[name] = {"year": year, "director": director, "cost": cost, "earning": earning }
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