name= 'Shagor'
greeting='assalaamalaikum '
c=greeting + name
print(c)
print(name[3])
# name[2]=g  cannot be assigned or replace character of given string
print(name[1:4])
print(name[:4])
print(name[1:])
c= name[-3:-1]# negative indicies
print(c)#output will be same
#
#slicing with skip value
name='gentlemen'
d=name[1::3]
print(d)