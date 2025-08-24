def sum(a,b):
    return a+b

def avg(a,b):
    return (a+b)/2

def diff(a,b):
    return a-b

a=5
b=4
print(sum(a,b))
print(avg(a,b))
print(diff(a,b))

#packagedemo is the folder
# in package demo two file:
# example.py
# testfunc.py

# mypackage is the subfolder
# two file 
# mathfunc.py
# areafunc.py

# from example.py i wanna import from areafunc with a square function
# for that
#  from mypackage.areafunc import square