MyDict={
    "Manner":'Well behavior',
    'Codding':'Writting Program',
    'Marklist':[1,2,3,5],
    'anotherDict':{'Shagor':'Will be best Inshallah'},
    2:45
     
}
# print(MyDict['Manner'])
# print(MyDict['Codding'])
# print(MyDict['Marklist'])
# print(MyDict['anotherDict'])
# print(MyDict['anotherDict']['Shagor'])
# MyDict['Marklist']=[23,45,66]
# print(MyDict['Marklist'])

# method of dictionary
print(list(MyDict.keys()))#prints keys of the dictinary
print(MyDict.values())#prints the value of the dictionary
print(MyDict.items())#print all keys and values of the dictionary
updateMyDict={
'friends1':'opu',
'friends2':'juwel',
"friends3":'haji',
2:56
}
MyDict.update(updateMyDict)#updated dictionary by adding key-value pairs from updatemydict
print(MyDict)
print(MyDict.get('Codding'))#print value associated with key-'codding'
print(MyDict['Codding'])#print value associated with key-'codding'

# the difference betwwen .get() and [] syntax is

print(MyDict.get('Codding2'))#print value associated with key-'codding2' and return none
print(MyDict['Codding2'])#print value associated with key-'codding2'is error coz it must be in dictionary
