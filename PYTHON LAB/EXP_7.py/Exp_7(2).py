#b. default agrument

def sum(*args):
    total=0
    for i in args:
        total+=i
    return total
answer=sum(1,2,3,4)
print(answer)