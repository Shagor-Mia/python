class employee:
    company='google'
    def getsalary(self, signature):
        print(f"The salary of {self.company} is {self.salary} ")
        print(signature)

    @staticmethod   # when we use @staticmethod there is no need of "(self)"
    def greet():
        print('good morning')
Shagor=employee()
Shagor.salary=123212
Shagor.getsalary("Thanks")
Shagor.greet()                