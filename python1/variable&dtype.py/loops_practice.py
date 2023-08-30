
# 1 multiplication table using user input

from math import factorial


num= int (input('enter the number\n'))
for i in range(1,11):
   # print(str(num) +" X "+ str(i)+" = "+str(num*i))
   
# we can use alternate print
   print(f"{num} X {i} = {num*i}")# 'f ' is a str funtion

##############################
# 
# 2 'startwith' funnction

List=['Shagor','Sajeeb','rakib','sakib','Rahim']
for name in List:
    if name.startswith( 'S'):
     print('Hello '+ name)

############################

# 3 'pr 1' with while loop
num= int (input('enter the number\n'))
i=1
while i<=10:   
   print(f"{num} X {i} = {num*i}")# 'f ' is a str funtion
   i=i+1

###########################
# 
# 4 checking the prime number
num=int(input('Enter anumber for prime or not\n'))
prime= True
for i in range (2,num):
  if(num%i==0):
    prime=False
    break
if prime:
    print(" is  a prime")
else:
    print(" is not a prime") 

#############################
# 
# 6 factorial of a number
num= int (input('Enter a number : '))
factorial=1
for i in range(1,num+1): ## must be 'num+1' in range in factorial
    factorial=factorial*i 
print(f'Factorial of {num} is : {factorial}')

##############################

# 8 star print
n=4
for i in range(n):
    print('*'*(i+1))

################################
# 
# multiplication table reverse order