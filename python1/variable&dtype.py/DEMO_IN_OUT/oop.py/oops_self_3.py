class employe:
    Company='Google'
    def getsalary(self):
        print('salary is 200k\n')
Shagor=employe() # whenever use '()' in class name you have to use                 
                  # 'self' in class func(self) 
Shagor.getsalary()        

################################

class employe:
    Company='Google'
    def getsalary(self):
        print(f'salary of working in {self.Company} is {self.salary}\n')
Shagor=employe()
Shagor.salary=23000
Shagor.getsalary() # Shagor.getsalary() = Shagor.getsalary( Shagor)
#Co=Shagor.Company
# print('The company name is '+Co)

####################################

