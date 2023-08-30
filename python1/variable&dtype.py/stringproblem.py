letter ='''Dear <|NAME|>
          I am very happy to inform you that,you 
     are selected as a junior software engineer in our
        SF company.
        congratulation.

 <|DATE|>''' 
name=input('Enter the selected name\n')
date=input('Enter the date\n')
letter=letter.replace("<|NAME|>",name)
letter=letter.replace('<|DATE|>',date)
print(letter)