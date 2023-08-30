class programmar:
    company='Amazon'
    def __init__(self,name,product):
        self.Name=name
        self.Product=product

    def ProDetails(self):
        print(f"the Name of {self.company} programmar is {self.Name} and Product is {self.Product}") 

Shagor=programmar('Shagor','Cloud')#when we use constructor ,the arguement can be pass by class(, , ,)
tanim=programmar('Tanim','Commerce')

Shagor.ProDetails()
tanim.ProDetails()

###############################

#2
class Calculator:
    def __init__(self,num):
        self.number=num
        print(f'the squar of {self.number} is {self.number**2}')

    def squaroot(self):
        print(f'the squaroot of {self.number} is {self.number**.5}')

    def cube(self):
        print(f'the cube  of {self.number} is {self.number**3}')
    @staticmethod
    def greet():
        print('hello how are you')

Value= Calculator(9)
Value.squaroot()
Value.cube()
Value.greet()

###############################

#3
class sample:
    A="oppu"  # class attribute

value=sample()
value.A='Shagor'# instance attribute
#Note:
   #instance attribute cannot change the class attribute
print(sample.A)
print(value.A)  

#############################

class Train:
    def __init__(self,name,seats,fare):
        self.trainName=name
        self.trainSeats=seats
        self.trainFare=fare

    def getsInfo(self):
           
        print(f'\nThe Name of Train is {self.trainName}')
        print(f'The available seats of Train is {self.trainSeats}')
        print(f'The Fare of Train is {self.trainFare}\n')
        print('*******************************')

    def bookTicket(self):
        if(self.trainSeats>0):
            print(f'Your Ticket is booked and Seat no is {self.trainSeats}')
            self.trainSeats=self.trainSeats - 1 
        else:
           print('Sorry all seats are full.only stan')

    def cancelTicket(self,seatNo):


A=input()
B=int(input())
C=input()
Value=Train(A,B,C) 
Value.getsInfo()
Value.bookTicket()       
Value.getsInfo()

        