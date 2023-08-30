class programmar:
    Company='Amazon'
    salary=5600
    salarybonus=400

    @property    # property is getter method
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter  #this is a setter method
    def totalsalary(self,value):
         
         self.salarybonus = value - self.salary

    @property    # property is getter method
    def finalsalary(self):
        return self.salary + self.salarybonus     
         

P=programmar() 
print(P.totalsalary) 
P.totalsalary=5800
print(P.salary)
print(P.salarybonus)
print(P.finalsalary)  
