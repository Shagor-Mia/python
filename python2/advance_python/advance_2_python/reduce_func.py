
# reduce function sequentially compute the list
from functools import reduce
sum= lambda a, b :a+b
L=[1,2,3,4,5]
value=reduce(sum,L)
print(value)