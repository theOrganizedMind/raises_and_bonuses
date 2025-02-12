import payroll
from employee import Employee
from employee_details import employee_details_2024


employees = [Employee(**data) for data in employee_details_2024]
updated_employee_payroll = {}

total_bonus_amount = 0
total_raise_amount = 0
total_current_payroll = round(sum(payroll.employees.values()), 2)

for employee in employees:
    print(f"\nCalculating for {employee.name}:")                        
    employee.calculate_yearly_health_insurance()
    employee.calculate_bonus_amount()
    employee.calculate_raise_amount()
    employee.calculate_vacation_amount()

    total_bonus_amount += employee.total_bonus_amount
    total_raise_amount += employee.total_raise_amount

    pay = payroll.employees.get(employee.name)
    if pay:
        new_pay_amount = pay + employee.total_raise_amount
        updated_employee_payroll[employee.name] = new_pay_amount

new_current_payroll = round(total_current_payroll + total_raise_amount, 2)
percent_increase = round((new_current_payroll - total_current_payroll)\
                        / total_current_payroll * 100, 2)


print(" Total Amounts ".center(50, "-"))
print(f"Total bonus amount for all employees = ${total_bonus_amount:,.2f}")
print(f"Total raise amount for all employees = ${total_raise_amount:,.2f}")
print(f"Total payroll for previous year = ${total_current_payroll:,.2f}")
print(f"Total payroll after raises = ${new_current_payroll:,.2f}")
print(f"Total percent increase in payroll = {percent_increase}%")

print("\n")
print("Updated Employee Payroll Amounts:")
print(updated_employee_payroll)
