A=10 # global variable
def func():
    global A # global keyword #this implies changing the global var into other var
    print(f"statment for 1: {A}")
    
    A=3  # local variable
    print(f"statment for 2: {A}")

func()
print(f"statment for 3: {A}")

