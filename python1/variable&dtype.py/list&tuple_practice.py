
#fuitlist

# F1=input("Enter Fruit Number 1 ")
# F2=input("Enter Fruit Number 2 ")
# F3=input("Enter Fruit Number 3 ")
# F4=input("Enter Fruit Number 4 ")
# F5=input("Enter Fruit Number 5 ")
# F6=input("Enter Fruit Number 6 ")
# F7=input("Enter Fruit Number 7 ")

# MYFRUIT_list=[F1,F2,F3,F5,F6,F7]
# print(MYFRUIT_list)

#student marklist
from audioop import avg


St1=int(input('Enter the mark of student N0 1: '))
St2=int(input('Enter the mark of student N0 2: '))
St3=int(input('Enter the mark of student N0 3: '))
St4=int(input('Enter the mark of student N0 4: '))
St5=int(input('Enter the mark of student N0 5: '))
St6=int(input('Enter the mark of student N0 6: '))

myList=[St1,St2,St3,St4,St5,St6]
myList.sort()
print(myList)

#sum of mylist
print(sum(myList))
avgr=sum(myList)/6
print(avgr)