# Check whether given number is divisible by 3 and 5 both.

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"The number {number} is divisible by both 3 and 5.")
else:
    print(f"The number {number} is not divisible by both 3 and 5.")
