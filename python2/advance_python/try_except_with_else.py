# else with try and except

try:
   a=int(input('enter a number :'))
   c=1/a
   print(f'the division is :{c}')
except Exception as e:
     print('exception occured')
     print(e)


else:     #here 'else' work when 'try' runs successfully. when 'except' then its not work
    print('we are successful.')     


#  finally with try and except

try:
   a=int(input('enter a number :'))
   c=1/a
   print(f'the division is :{c}')
except Exception as e:
     print('exception occured')
     print(e)
     exit()

finally:     # herre finally works for both try and error
    print('we are DONE.')     
