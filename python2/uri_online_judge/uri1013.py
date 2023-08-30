# A=[int(a) for a in input().split(" ")]
# alternate list
A=list(map(int,input().split(" ")))
# print(f"{max(A)} eh o maior")

# alternate way
x=A[0]
y=A[1]
z=A[2]
major=max(x,y,z)
print(major,"eh o maior")

# if(x>y):
#     print(f"{x} eh o maior")
# elif(y>z):
#     print(f"{y} eh o maior")
# else :
#     print(f"{z} eh o maior")
# print(A)
# print(x)