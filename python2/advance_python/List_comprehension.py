# this is traditional list

A = [12,34,2,6,45,77,87,43,21,5,9,67]
B=[]
for item in A:
    if item%2==0:
        B.append(item) 
print(f"the traditional list is {B}")


# comprehension list

C=[3,5,1,2,9,7,6,88,34,21,90]
D=[i for i in C if i%2==0]
print(f"\n the comprehension list is {D}")

# set comprehension

T=[1,3,2,1,4,3,5,6,9,7,6]
S={i for i in T}
print(S)