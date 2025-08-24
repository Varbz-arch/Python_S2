#Write a lambda function to find volume of cone. 

volume_cone=lambda r,h: (1/3) * 3.14 * r**2 * h
r=int(input("Enter the radius of the cone: "))
h=int(input("Enter the height of the cone: "))
print(volume_cone(r,h))