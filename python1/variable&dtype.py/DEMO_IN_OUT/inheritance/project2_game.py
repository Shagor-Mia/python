
############################### Guessing the number
import random
randNumber=random.randint(1,100)
# print(randNumber)
UserGuess=None
guesses=0

while(UserGuess!=randNumber):
 UserGuess=int(input('Enter your Guess :'))
 guesses+=1

 if UserGuess==randNumber:
     print('you guessed it right!')
 else:
    if(UserGuess>randNumber):
     print('your guessed is wrong! guess the smaller number ')  
    else:
     print('your guessed is wrong! guess the largest number ')  
           
print(f'you guessed the number in { guesses}th time')

with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print('you have just broken the hiscore!')    
    with open("hiscore.txt","w") as f:
     f.write(str(guesses))