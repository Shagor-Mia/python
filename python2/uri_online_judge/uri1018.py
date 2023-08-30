A=int(input())
print(A)

for i in [100,50,20,5,2,1]:
 print(f'{A//i} nota(s) de R$ {i},00')
 A%=i 

# alternate
# A=int(input())
# print(A)
# B=[100,50,20,5,2,1]
# for i in B :
#   C=int(A/i)
#   print('{} nota(s) de R$ {},00'.format(C,i))
#   A-=C*i
 