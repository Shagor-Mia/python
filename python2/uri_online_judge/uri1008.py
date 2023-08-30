EmpNo=int(input())
EmpW_h_M=int(input())
empSalary_per_h=float(input())

salary_per_month=empSalary_per_h*EmpW_h_M
print('NUMBER =',EmpNo)
print('SALARY = U$ {:.2f}'.format(salary_per_month))
