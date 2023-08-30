
class Person:
    Country="Bangladesh"
    def takeaBreak(self):
        print('i am breathing')

class employee(Person):
    Company ='Amazon'
    def getsalary(self):
        print(f'Salary of Employe is {self.salary}')

    def takeaBreak(self):
        print("I am an employee,i am also breathing.....")

class programmar(employee):
    Company='Fiverr'
    def getsalary(self):
        print('salary of a programmar is 121k')

P=Person()
E=employee()
Pr=programmar()
# print(P.Company) throws an error
print(Pr.Country)
Pr.takeaBreak()                