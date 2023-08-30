
Fruits=['mango','banana','guava','cherry']
for items in Fruits:
    print(items)
    #########################

for i in range(1,10):#by default it starts with 0,to start from a num (2,10)etc
    print(i) 
print("next what\n")
###############################

# step size
for i in range(1,10,2):# here 2 determines the step size
    print(i)
else:
    print("ends of for loops and start else\n")

############################ 
# 
A=[3,2,4,5]
sum=0
for items in A:
    sum=sum+items

print(sum)
print('done\n')

#################################

# break statement
for i in range(12):
    print(i)
    if i==13:
        break
else:
 print('here start again\n')

#continue statement
for i in range(12):
    if i==6:    #skipping element 6
      continue
    print(i)
