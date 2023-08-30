num1=int(input('Enter number 1: '))
num2=int(input('Enter number 2: '))
num3=int(input('Enter number 3: '))
num4=int(input('Enter number 4: '))

if(num1>num3):
    f1=num1
else:
    f1=num3

if(num2>num4):
    f2=num2
else:
    f2=num4

if(f1>f2):
    print(str(f1) +" is greatest Number")
else:
    print(str(f2) +' is greatest Number')    

##########################################
sub1=int(input('Enter  sub1 number : '))
sub2=int(input('Enter sub2 number : '))
sub3=int(input('Enter sub3 number : '))

if(sub1<33 or sub2==32 or sub3<=33):
    print('you are fail')
elif(sub1+sub2+sub3)/3 <40:
    print("Passed")
else:
    print("you are passed")

#############################################
#spam
a=input('Enter atext :')
if("anythin"in a):
    spam=True
elif('is 'in a):
    spam = True
elif('good'in a):
    spam = True
else:
    spam=False

if(spam):
    print('this is a spam')
else:
    print('this is not an spam')  

 ############################################## 
 
 #checking in the list
List=['shagor','oppu','emon','younus','ayesha']
name=input("Enter a name for searching in the list :")                     
if name in List:
    print('the searched name is found int list')
else:
    print('the searched name is not found int List') 

  ########################################
  # 
  # converting marks into grade
mark=int(input('Enter your mark for GRADE : '))
if mark>=90:
    Grade=' EXC'
elif mark>=80:
    Grade='A' 
elif mark>=70:
    Grade='B'
elif mark>=60:
    Grade='C'
elif mark>=50:
    Grade='D'
else:
    Grade='F' 
print('Your Grade is : '+str(Grade))
           


