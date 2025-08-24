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
