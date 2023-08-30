#1.Single example
print('Data structure') #c1 time
# O(c1)= O(n)= O(1)


#2. example
n = 10                      #c1
for i in range(n):          #c2 
    print('welcome to DSA') #c3*n
"""
 tc => c1 + c2 + c3*n
    = c + c3*n 
    = O(c3*n) 
    = O(n) 
    = O(1)    
"""


#2. sequential example
n = 10                      #c1
m = 5                       #c2
for i in range(n):          #c3 
    print('welcome to DSA') #c4*n
for i in range(m):          #c5 
    print('welcome to structure') #c6*m
"""
 tc => c1 + c2 + c3 + c4*n + c5 + c6*m
    = c + c4*n + c6*m 
    = O(c*(n+m)) 
    = O(n+m) 
        
"""


#3. nested example
n = 10                              #c1
m = 5                               #c2
for i in range(n):                  #c3 
    print('welcome to DSA')         #c4*n
    for j in range(m):              #c5 
      print('welcome to structure') #c6*n*m
"""
 tc => c1 + c2 + c3 + c4*n + c5 + c6*n*m
    = c + c4*n + c6*n*m* 
    = O(c6*(n*m)) 
    = O(n*m)     
"""


#4. example
if n==m:                               # c1
    print('you are correct path')      # c2
else:                                  # c3 
    for i in range(min(m,n)):          # c4
        print('boring about it?')      # c5*(m,n)

"""
 best case = c1 + c2 
           = O(c)
           = O(1)

 worst case = O(c5*min(m,n))
            = O(min(m,n))                         
 """              