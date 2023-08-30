list_all=[12,12.2,'shagor',321]

# this is traditional loop function 

index=1
for item in list_all:
    print(f"no {index} index contains: {item}")
    index+=1

# this is enumeration function

list_all_1=[1,2.2,'shagor mia',21]

for index,item in enumerate(list_all_1):
    print(f"\n no {index} index contains: {item}")
