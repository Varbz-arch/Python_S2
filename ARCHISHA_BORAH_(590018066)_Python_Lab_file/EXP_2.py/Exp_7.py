# Write a program to convert given seconds into hours, minutes and remaining 
# seconds. 

seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{seconds} seconds is equivalent to {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")

