# Kyle Stewart Cis216 Couurse Project

total_employees = 0
total_hours = 0.00
total_gross_pay = 0.00
total_tax = 0.00
total_net_pay = 0.00

def get_employee_name():
    employee_name = input("Enter the employee's name: ")
    return employee_name

def get_total_hours():
    total_hours = float(input("Enter the total hours: "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter the hourly rate: "))
    return hourly_rate

def get_income_tax_rate():
    income_tax_rate = float(input("Enter the income tax rate: "))
    income_tax_rate = income_tax_rate / 100
    return income_tax_rate

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(name, hours, rate, gross, tax_rate, tax, net):
    print(f"Employee Name: {name}")
    print(f"Total Hours: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Tax: {tax}")
    print(f"Net Pay: {net}")
    
def display_totals(employees, hours, gross, tax, net):
    print(f"Total Number of Employees: {employees}")
    print(f"Total Number of Hours: {hours}")
    print(f"Total Gross Pay: {gross}")
    print(f"Total Tax: {tax}")
    print(f"Total Net Pay: {net}")
    
while True:
    name = employee_name()
    if name.lower() == "end":
        break
    hours = total_hours()
    rate = hourly_rate()
    tax_rate = income_tax_rate()
    gross, tax, net = calculate_pay(hours, rate, tax_rate)
    display_employee_info(name, hours, rate, gross, tax_rate, tax, net)
    total_employees += 1
    total_hours += hours
    total_gross_pay += gross
    total_tax += tax
    total_net_pay += net

display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)