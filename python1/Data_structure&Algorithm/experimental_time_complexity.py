import time

start=time.time()
found = -1
arr = [7,2,3,7,4]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found= arr[i]
print(found) 
end=time.time()
print(1000*(end-start))           