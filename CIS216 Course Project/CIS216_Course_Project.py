# Kyle Stewart CIS261 Course Project

total_employees = 0
total_hours = 0.00
total_gross_pay = 0.00
total_tax = 0.00
total_net_pay = 0.00

employee_data = []

def get_date(prompt):
    date = input(prompt)
    return date

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

def display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    print(f"From Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Employee Name: {name}")
    print(f"Total Hours: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Tax: {tax}")
    print(f"Net Pay: {net}")

def display_totals(totals):
    print(f"Total Number of Employees: {totals['employees']}")
    print(f"Total Number of Hours: {totals['hours']}")
    print(f"Total Gross Pay: {totals['gross']}")
    print(f"Total Tax: {totals['tax']}")
    print(f"Total Net Pay: {totals['net']}")

while True:
    from_date = get_date("Enter the from date (mm/dd/yyyy): ")
    if from_date.upper() == "END":
        break
    to_date = get_date("Enter the to date (mm/dd/yyyy): ")
    name = get_employee_name()
    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_income_tax_rate()
    gross, tax, net = calculate_pay(hours, rate, tax_rate)
    employee_data.append([from_date, to_date, name, hours, rate, tax_rate])
    display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net)
    total_employees += 1
    total_hours += hours
    total_gross_pay += gross
    total_tax += tax
    total_net_pay += net

totals = {
    'employees': total_employees,
    'hours': total_hours,
    'gross': total_gross_pay,
    'tax': total_tax,
    'net': total_net_pay
}

for data in employee_data:
    from_date, to_date, name, hours, rate, tax_rate = data
    gross, tax, net = calculate_pay(hours, rate, tax_rate)
    display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net)

display_totals(totals)
