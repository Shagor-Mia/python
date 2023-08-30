
#modeling of oops
#
# NOUN = Class  == Employee
# ADJECTIVE = Atributes == name,age,salary
# VERB = Methods == getsalary(),increment()
#
##############################

# using class atrribute for employee

class employee:
    Company='Google' # here 'compamy' is a class atrribute

shagor= employee()
oppu=employee

print(shagor.Company)
print(oppu.Company)  

employee.Company='Twitter'# changing the class atribute
print(shagor.Company)
print(oppu.Company)    

##########################

class employee:
    Company='Google' # here 'compamy' is a class atrribute
    salary=3000
shagor= employee()
oppu=employee
shagor.salary=20   #here 'salary' is an instance of atribute
print(shagor.Company)
print(shagor.salary)
print(oppu.Company)
print(oppu.salary)  
