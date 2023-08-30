R_o=int(input("enter the rows no: "))
C_o=int(input("enter the column no: "))

print(R_o*C_o)


# for creating input of matrix
print("input the matrix numbers")
m=[]
for i in range(R_o):
     n=[]
     for j in range(C_o):
       j= int(input( ))
       n.append(j)
     m.append(n)
# for display the matrix 
print("the matrix is :")
for i in range(R_o):
  for j in range(C_o):
     print(m[i][j],end=" ") 
  print()
# sum of Left and Write diagnal
sum_L =0
sum_R =0
# for i in range(R_o):
#   for i in range(C_o):
#    if i==j:
#     sum_L =sum_L + m[i][j]
#    if i+j==3-1:
#     sum_R = sum_R + m[i][j]


sum_L=sum_L+m[0][0]+m[1][1]+m[2][2]
sum_R=sum_R+m[0][2]+m[1][1]+m[2][0]

print('the LEFT DIAGONAL IS : ',sum_L)
print('the RIGHT DIAGONAL IS : ',sum_R)      
diff= abs(sum_L - sum_R)
print(diff)