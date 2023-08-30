
# Single Inheritance----------


class Employee:          #Base class
    Company ="google"
    def ShowDetails(self):
        print("this is an employee")

class programmar(Employee): #derive class---inherited the base class
    Company='Amazon'
    language="Python"
    def getLang(self):
       print(f"The language is {self.language}")

E=Employee()      #created an object of an employee class       
P=programmar()
P.ShowDetails() # here P objects can call all the atribute and functions of base class\
                 # Coz derive class are inherited by P objects class
#print(P.Company)
# Overidding                
print(P.Company)  #Now it will overide the 'Company' name coz similar name also in derive class  
                       