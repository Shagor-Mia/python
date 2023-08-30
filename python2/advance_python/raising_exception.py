def increement(num):
    try:
        return int(num)+2
    except:
        raise ValueError('this is not actual number ')

input=int(input('input a number '))
A=increement(input)
print(A)            