class employee:
    company='google'

    ######1
    def __init__(self,salary, name,subunit) :#this method is called 
                                         #constructor coz its initalizes the objects
     self.Name=name
     self.SubUnit=subunit
     self.Salary=salary
     print('Employee is created') #this will run automatically without 'Shagor.__init()'

    def GetDetails(self):
        print(f'Employee Name is {self.Name}')
        print(f'Employee Salary is {self.Salary}')
        print(f'Employee  SubUnit is {self.SubUnit}')
    
    def getsalary(self, signature):
        print(f"The salary of {self.company} is {self.salary} ")
        print(signature)
     #######1 

    @staticmethod   # when we use @staticmethod there is no need of "(self)"
    def greet():
        print('good morning')

    @staticmethod
    def time():
        print('rime is 9 AM') 

# Shagor=employee()
# Shagor.salary=123212
# Shagor.getsalary("Thanks")
# Shagor.greet               

#####1
Shagor=employee(1234321,'Shagor','Ghorashal')
# Shagor=employee() this throws an error
Shagor.GetDetails()
