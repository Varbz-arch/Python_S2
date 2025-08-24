# Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ): 
# Example: 
# Dehradun 5.78 308.20 
# Delhi 190 1484 
# …………… 
# Open file city.txt and read to:  

file = open("city.txt", "r")
lines = file.readlines()
file.close()

# a. Display details of all cities
print("Details of all cities:")
for line in lines:
    print(line.strip())

# b. Display city names with population more than 10 Lakhs
print("\nCities with population more than 10 Lakhs:")
for line in lines:
    city, population, area = line.split()
    if float(population) > 10:
        print(city)

# c. Display sum of areas of all cities
total_area = sum(float(line.split()[2]) for line in lines)
print(f"\nTotal area of all cities: {total_area} sq km")
