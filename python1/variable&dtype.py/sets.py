# a={1,2,3,4,1,2,4}
# print(a)#repated not allow
# print(type(a))

# #Empty set
# a={}
# print(type(a))#this will create empty dictionary not empty set

# # an empty set can be created by bellow syntax
b= set()
print(type(b)) 

# methods of sets
b.add(4)#add number into empty b set()
b.add(6)#.add() is a method
b.add(7)
# b.add([1,2,3])#list cannot be added
b.add((8,6,5))
# b.add({5:45})#dictionary cannot be added cozits not Hashable
print(b)
print(len(b))
b.remove(7)
print(b)
# b.remove(8)#cannot be remove coz its not in the set
print(b.pop()) #randomly remove an element
print(b)

