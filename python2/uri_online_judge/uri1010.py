# a=input().split(' ') # split('') seperated the inputed element in the list[]
# b=input().split(' ')
# total=(int(a[1])*float(a[2]))+(int(b[1])*float(b[2]))
# print("VALOR A PAGAR: R$ {:.2f}".format(total))

# using list comprehension
a=[ float(a) if '.' in a else int(a) for a in input().split(' ')]
b=[ float(b) if '.' in b else int(b) for b in input().split(' ')]
total=((a[1])*(a[2]))+((b[1])*(b[2]))
print("VALOR A PAGAR: R$ {:.2f}".format(total))

