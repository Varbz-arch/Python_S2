#c. Variable length argument 

def sum(**kargs):
    total=0
    for key in kargs.keys():
        total+=kargs[key]
    return total
SUM=sum(x=1,y=2,z=3)
print(SUM)