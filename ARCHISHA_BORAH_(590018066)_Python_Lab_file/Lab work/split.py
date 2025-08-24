"""
steps
1. Take the input from the user in DD/MM/YYYY
2. Extract day, month, year from each date and convert them into integers
3. Calculate the diff and cast it to a string
"""
current_date=input('Enter the current date')
bday=input('Enter the bday')
current_date= current_date.split('/')
bday=bday.split('/')
left_days=0
for i in range(3):
    if (i==0):
        left_days+=abs(int(current_date[i])-int(bday[i]))
    elif (i==1):
        left_days+=abs(int(current_date[i])-int(bday[i]))*30
    else:
        left_days+=abs(int(current_date[i])-int(bday[i]))*365
left_days= str(left_days)
print(f'{left_days}')
