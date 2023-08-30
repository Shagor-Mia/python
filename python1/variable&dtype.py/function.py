def percents(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[34,56,67,89]
persentage1=percents(marks1)

marks2=[99,77,66,11]
persentage2=percents(marks2)

print(persentage1)
print(persentage2)

# we can make it in simple way


marks1=[34,56,67,89]
persentage1=(sum(marks1)/400)*100 # sum is built in function

marks2=[99,77,66,11]
persentage2=(sum(marks2)/400)*100

print(persentage1)
print(persentage2)

##########################

# function call

def salam(name):      #calling function(user define function)
    print("assalaamalaikum "+name)
salam('md.shagor')    #called function

######################

def Mysum(num1,num2): #passing arguement
 return(num1+num2)
 
d=Mysum(23,21)
print(d)

####################

def salam(name='Safwan\n'): # here 'stranger' working as default arguement
    Me=("assalaamalaikum "+ name)
    return Me
a=salam() 
b=salam( 'Shagor\n')
print(a,b)