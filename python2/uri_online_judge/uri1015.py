import math
A=[float(a) for a in input().split()]
x1=A[0]
y1=A[1]
B=[float(b) for b in input().split()]
x2=B[0]
y2=B[1]

distance=math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
print('{:.4f}'.format(distance))
# print(A)
# print(B)