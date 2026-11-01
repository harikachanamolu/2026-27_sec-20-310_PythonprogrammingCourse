
# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime amount: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

# Validate salary details
if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid salary details!")

else:
    # Calculate gross salary
    gross = basic + allowances + overtime + incentives

    # Calculate progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = (20000 * 0.05) + ((gross - 20000) * 0.10)
    else:
        deduction = (20000 * 0.05) + (20000 * 0.10) + ((gross - 40000) * 0.15)

    # Calculate net salary
    net_salary = gross - deduction

    # Salary statement
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name     :", name)
    print("Employee ID       :", emp_id)
    print("--------------------------------------")
    print("Basic Salary      : Rs.", basic)
    print("Allowances        : Rs.", allowances)
    print("Overtime          : Rs.", overtime)
    print("Incentives        : Rs.", incentives)
    print("--------------------------------------")
    print("Gross Salary      : Rs.", gross)
    print("Total Deduction   : Rs.", round(deduction, 2))
    print("--------------------------------------")
    print("Net Salary        : Rs.", round(net_salary, 2))
    print("======================================")
