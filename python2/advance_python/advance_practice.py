# def readfile(filename):
#     with open(filename,"r") as f:
#         print(f.read())

# readfile("1.txt")
# readfile("2.txt")        
# readfile("3.txt")        

# Q2: Write a program to print third fifth and seventh element from
#    a list using enumerate function.

# List=[1,2,3,4,5,6,7,8,9,10]
# for index,item in enumerate(List):
#     if index==2 or index== 4 or index==6:
#      print(f"\n no {index+1} index contains: {item}")

# Q3: Write a list comprehension to print a list which contains the multiplication
#    table of a user entered number.


# num=int(input('enter your number: '))
# table=[num*i for i in range(1,11)]
# print(table)

# Q4: Write a program to display a/b where a and b are integers.if b=0,
#     display infinite by handling the ZeroDivisionError.

# a=int(input('Enter a num :'))
# b=int(input('Enter a num :'))
# try:
#  print(a/b)
# except:
#  print('infinate') 

#Q:5  store the multiplication table generated in problem 3  in a file named table.txt.

num=int(input('enter your number: '))
table=[num*i for i in range(1,11)]
print(table)
with open ("table.txt","a") as f:
    f.write(str(table))