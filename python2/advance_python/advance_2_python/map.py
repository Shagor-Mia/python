
#map is used for  a list

#  method 1. is general formula

def square(num):
  return num*num 

List=[2,3,4]
List2=[]
for item in List:
   List2.append(square(item))
print(List2)   

# method 2. is shortcut is known as map

def square(num):
  return num*num 

List=[2,3,4]
List2=[]
print(list(map(square,List)))