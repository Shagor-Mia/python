
class Person:
    Country="Bangladesh"
    def takeaBreak(self):
        print('i am breathing')

    def __init__(self):
       print('person is initializing')
            

class employee(Person):
    Company ='Amazon'
    def getsalary(self):
        print(f'Salary of Employe is {self.salary}')

    def __init__(self):
        # super().__init__()
        print('employee  is initializing')
            

    def takeaBreak(self):
        super().takeaBreak()  #superclass is used for run all previus same function
        print("I am an employee,i am also breathing.....")

class programmar(employee):
    Company='Fiverr'
    def getsalary(self):
        print('salary of a programmar is 121k')

    def __init__(self):
        super().__init__()
        print('programmer   is initializing')

P=Person()
E=employee()
Pr=programmar()
# print(P.Company) throws an error
print(Pr.Country)
Pr.takeaBreak()                