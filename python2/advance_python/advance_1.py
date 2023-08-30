
# Example_1 exception handling

from logging import exception


while(True):
    print('press Q to quit ')
    a=input(' Enter your number :')
    if a=='Q':
        break
    try:
       a=int(a)
       if a>6:
        print('you entered a number is greater than 6 ')
       else:
        print('you entered a number is less than 6 ')

    except Exception as e:   # here Exception's "E" must be in capital letter
        print(f'your input result in an error . {e}') #here "e" handles the errors
print('thanks for playing games')