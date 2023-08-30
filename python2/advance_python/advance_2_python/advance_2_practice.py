# Q1:Write a program to input name,marks and phone number of a student and format
#    format it using the format function like bellow:
#    "the name of the student is Shagor, his marks are 72 and phone number
#      is 3456789"     

# name=input("Enter your name: ")
# marks=int(input("Enter your marks: "))
# mobile=int(input("Enter your mobile no: "))

# template="the name of the student is {}, his marks are {} and phone number is {}"
# output=template.format(name,marks,mobile)
# print(output)

# Q2: A list contains the multiplication table of7.Write aprogram to convert it to
#     a vertical String of same numbers 7.

L=[str(i*7)for i in range(1,11)] # this is a list comprehension
print(L)
VerticalTable="\n".join(L)
print(VerticalTable)

#Q3:Write a program to filter a list of number which are divisible by 5.

L=[1,2,3,4,5,6,12,45,65,10]

g10= lambda num:num%5==0

print(list(filter(g10,L)))
 
#Q4:Write a program to find the maximum of the numbers in a list using reduce func. 
from functools import reduce

L=[1,2,3,4,5]
value=reduce(max,L)
print(value)