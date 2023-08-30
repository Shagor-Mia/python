F = open('read.txt','r')
data=F.readline() #read only first line
print(data)

data=F.readline() #read also second line
print(data)
F.close()