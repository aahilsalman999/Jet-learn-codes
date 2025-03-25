def get_employee_details():
  name = input("What is your name?")
  age = int(input("What is your age?"))
  base_salary = int(input("What is your salary?"))
  return name , age , base_salary

def calculate_salary(base_salary):
  tax_deducted = 0
  if base_salary > 100000:
    tax_deducted = 20
  elif base_salary > 50000 and base_salary <= 100000:
    tax_deducted = 15
  elif base_salary > 30000 and base_salary <= 50000:
    tax_deducted = 10
  else:
    tax_deducted = 5
  final_salary = base_salary - base_salary / 100 * tax_deducted
  return final_salary , base_salary , tax_deducted

def generate_payslip(name,age,base_salary,tax_deducted,final_salary):
   print("Payslip:")
   print("Name:", name)
   print("Age:", age)
   print("Base salary:", base_salary)
   print("Tax deducted:, ", tax_deducted,"%")
name,age,base_salary = get_employee_details()
final_salary,base_salary,tax_deducted = calculate_salary(base_salary)
generate_payslip(name,age,base_salary,tax_deducted,final_salary)
print("Final salary:",end=" ")
print(final_salary)

   

