
class programmer:
    Name='Shagor'
    Salary=345223435
    Location='Dhaka'
    
    # def ChangeSalary(self,Sal):
    #   self.__class__.Salary=Sal # this technique will change the class atribute 'Salary'

# another alternate of class method  
    @classmethod
    def ChangeSalary(cls,Sal): #this method also change the class atribute directly
      cls.Salary=Sal

P=programmer()
print(P.Salary)
P.ChangeSalary(12334323110)
print(P.Salary) 
print(programmer.Salary)    # here will be new output of salary


#################################
# 2.property decorator
