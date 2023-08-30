# Different type of exception handlling

try:
   a=int(input('enter a number :'))
   c=1/a
   print(f'the division is :{c}')
# except Exception as e:
#     print('exception occured')
#     print(e)     #it is printing e and doesnt affect the program 'e"is not an error


except ValueError as e: # different types of handling 
    print('plse enter a valid value ')
    # print(e)

except ZeroDivisionError as e: # different type of handling
    print('make sure you are not deviding by zero ')
    # print(e)

except TypeError as e:
    print('please enter a string type :')
    # print(e)

print('thanks for error handling')    