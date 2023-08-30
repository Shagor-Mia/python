MyDict={
    "kedera":'chair',
    'kapurush':'loser',
    'vai':'brother'

}
print('Enter your options ',MyDict.keys())
a=input('Enter your bangla words \n')
# print('the meaning of entered word is :',MyDict[a])
print('the meaning of entered word is :',MyDict.get(a))#it will not give an errors

##set
s={12,'12',12.12,12.00}
print(s)
print(len(s))#length will be 3 coz 12 =12.00
# s={12,'12',12.12,12.00,[1,2,3]} set cannot contain the list
#Making a dictionary using user inputs
MyDict={}

a=input('Your favurite game is : ')#input values
b=input('Your favurite game is : ')
c=input('Your favurite game is : ')
d=input('Your favurite game is : ')

MyDict['shagor']=a #assigning keys
MyDict['oppu']=b
MyDict['haji']=c
MyDict['kazi']=d
print(MyDict)