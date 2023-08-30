
class MultiPle:
    Company='Amazon'
    C_code=324

class Frelancer:
    Company='Fiverr'
    level=3
    def UpgradeLevel(self):
        self.level=self.level+1

class Programmer(MultiPle,Frelancer):
    Name='Shagor'
            
P=Programmer()
print(P.C_code)
print(P.Company)
P.UpgradeLevel()
print(P.level)            