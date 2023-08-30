#
## 1 find the maximum number using calling function
def MAXnum (num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3 
    else:
        if num2>num3:
            return num2
        else:
            return num3
Max=MAXnum(12,22,11)
print(Max)
####################################
# 
# temperature
def farh(cel):
    return(cel*(9/5))+32
c=0
F=farh(c)
print('The Temperature of Fareignheit is :',F)    
###################################

print('hello ', end='')
print('how ',end=' ')
print('are ',end='')
print('you \n',end='')

#################################

n=5
for i in range(n):
    print('*'*(n-i)) #prints * n-i times

#############################    # 

# strip function
def remove_and_strip(string,word):
    newStr = string.replace(word," ")
    return newStr.strip()# strip func() removes the wide space from both side of string 
this="   hello people   " 
F=remove_and_strip(this,' bangladesh')
print(F)   
    
