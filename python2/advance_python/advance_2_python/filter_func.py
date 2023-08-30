
from operator import truediv


def greater_than_5(num):
    if num>5:
        return True
    else:
        return False    

L=[1,2,3,4,5,6,12,45,65,10]

g10= lambda num:num>10

print(list(filter(greater_than_5,L)))
print(list(filter(g10,L)))
