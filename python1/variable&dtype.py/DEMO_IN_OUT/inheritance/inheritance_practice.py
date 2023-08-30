
#Q.1: create a class 2-D vector and use it to creat another class representing a class 3-D vector 


class C2D_Vector:
    def __init__(self,i,j): # created constructor
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
        

class C3D_vector(C2D_Vector): # inherited base class
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"    

v2d=C2D_Vector(23,12) 
v3d=C3D_vector(34,32,21)  
print(v2d)
print(v3d)


########################################

#Q:2. create a class pet from class animal and further create class dog from pets.
#     add a method bark to class dog.

class animal:
    animalType="mammal"

class pet:
    petType="dog"

class dog:
    @staticmethod
    def bark():
        print("vow vow")

d=dog
d.bark()

######################################

#Q:3. create a class employee, add salary and increment properties in it.write a
#    method salaryafterincreement method with a @property decorator with a setter 
#    which change the value of increement based on the salary .
# 
class employee:
    salary=200
    increement=1.3
    @property
    def salaryafterincreement(self):
     return self.salary*self.increement

    @salaryafterincreement.setter
    def salaryafterincreement(self,value):
      self.increement = value/self.salary

e=employee()
print(e.salaryafterincreement)  
print(e.increement)
e.salaryafterincreement=3000
print(e.increement) 

####################################

#Q:3 write a class complex to represent a complex numbers,along with overloaded 
#    operator "+" and "*" for add and multiply.
#    Formula::(a+bi)(c+di)=(ac-bd)+(ad+bc)i
class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return complex(self.real+c.real,self.imaginary+c.imaginary)#returning same class objects

    def __mul__(self,c):
        mulReal= self.real*c.real - self.imaginary*c.imaginary   #(a*c-b*d)
        mulImg= self.real*c.imaginary + self.imaginary*c.real   #(a*d+b*c)i           
        return complex(mulReal,mulImg)
        # return complex(self.real*c.real,self.imaginary*c.imaginary)  

    def __str__(self) -> str:
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"  # for "-" imaginary part  
        else:
          return f"{self.real} + {self.imaginary}i"    
c1=complex(1,-4)
c2=complex(2,-6)
print(c1+c2)
print(c1*c2)


#######################################
# Q:5.write a class vector represent a vector of n dimension overload the 
 #    "+" and "*" operators which calculated the sum and dot product of them
class vector:
    def __init__(self,vec):
       self.vec=vec 

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+=f"{i}a{index} +"
            index+=1
        return str1[:-1]   # string slicing 

    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i]) 
        return vector(newList)

    def __mul__(self,vec2):   #"." product is a scaler quantity so it cant be vector
        sum=0
        for i in range(len(self.vec)):
            sum+=(self.vec[i] * vec2.vec[i]) 
        return sum    

v1=vector([12,23,34,45])
v2=vector([11,22,33,44])
print(v1)
print(v1+v2)
print(v1*v2)

####################################
# Q:6. write a __str__ method to print the vector as follows:
#       7i^ + 8j^ +10 k^
#      assume that vector of dimension 3 for this problem
# 
class vector:
    def __init__(self,vec):
       self.vec=vec 

    def __str__(self):
        
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k" 
   
v1=vector([12,23,34,45])
v2=vector([11,22,33,44])
print(v1)
print(v2)

#########################################
# Q:7.override the __len__() method on vector of problem 5 to display 
#     the dimension of the vector.

class vector:
    def __init__(self,vec):
       self.vec=vec 

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+=f"{i}a{index} +"
            index+=1
        return str1[:-1]   # string slicing 

    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i]) 
        return vector(newList)

    def __mul__(self,vec2):   #"." product is a scaler quantity so it cant be vector
        sum=0
        for i in range(len(self.vec)):
            sum+=(self.vec[i] * vec2.vec[i]) 
        return sum 

    def __len__(self):
        return len(self.vec)  #here self.vec is a list for both v1,v2 objects     

v1=vector([12,23,34,45])
v2=vector([11,22,33])
print(v1)
print(len(v1))
print(len(v2)) 
