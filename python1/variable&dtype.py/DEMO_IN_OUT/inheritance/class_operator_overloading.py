class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2): # this is " + "=add operator overloading
        print("lets add")
        return self.num + num2.num
    def __mul__(self,num2): # this is " * "=mul operator overloading
        print("lets mul")
        return self.num * num2.num

    def __sub__(self,num2): # this is " - "= sub operator overloading
        print("lets sub")
        return self.num - num2.num
    def __truediv__(self,num2): # this is " * "=division operator overloading
        print("lets div")
        return self.num /num2.num    
    def __str__(self):
        print(f"your number is {self.num}")

n1=number(2)
n2=number(5)
sum =n1+n2
print(sum)
mul=n1*n2
print(mul) 
sub =n1-n2
print(sub)
div=n1/n2
print(div)
n3=number(8)
print(n3)               