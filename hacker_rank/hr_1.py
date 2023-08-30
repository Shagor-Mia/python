

# num_range = range(2,5,2)
# num2_range = range(6,20,2)

# n = 24
# if(n%2!=0): 
#    print('Weird')
# if n in num_range :
#     print('Not Weird')
# if n in num2_range :
#     print('Weird')
# if n%2==0 and n>20:
#     print('Not Weird')    
    
n = int(input())
if(n%2!=0):
    print('Weird')
else:
    if(2<=n<=5):
        print('Not Weird')
    elif(6<=n<=20):
        print('Weird')
    elif(n>20):
        print('Not Weird')            