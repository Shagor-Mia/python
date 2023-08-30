Name=input()
salary=float(input())
sale_in_month=float(input())

salary_total=(((15/100)*sale_in_month)+salary)
print("TOTAL = R$ {:.2f}".format(salary_total))