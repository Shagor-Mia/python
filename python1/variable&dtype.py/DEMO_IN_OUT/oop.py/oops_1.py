class Number:      #class name
    def sum(self):
     return(self.a +self.b)

num=Number()   # objects instantiation
num.a=12
num.b=11
s=num.sum()
print(s)     

###############

#2
class RailwayForm:
    FormType='Railway reservation'# created object in class

    def printData(self):    #created a function in class
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Train is {self.train}")

ShagorApplication=RailwayForm() # assigning the class name with a variable for creating other object or instantiation 
ShagorApplication.name='shagor' #creating object
ShagorApplication.age='25'
ShagorApplication.train="rajshahi express"

ShagorApplication.printData() #printing all the informition
print('hello md')
#############################

#2
class Remote():
    def isLeftpressed(self): #attribute
        print('start')
class player():
    def moveRight(self):
        print('player move to the right')
    def moveLeft(self):
        print('player move to the left')
        
    def moveTop(self):
        pass

remote1=Remote()
player1=player()
if (remote1.isLeftpressed()):
     player1.moveLeft()  #### not satisfying 
