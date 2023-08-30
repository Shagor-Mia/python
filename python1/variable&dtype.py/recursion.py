from itertools import product


def factorial_iter(n):
    product=1
    for i in range(n):
      product=product*(i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

F=factorial_iter(5)
# F=factorial_recursive(4)
print(F)    
