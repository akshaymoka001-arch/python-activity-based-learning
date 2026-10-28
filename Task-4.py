basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

if min(basic, allowances, overtime, incentives) < 0:
    print("Invalid salary details")
else:
    gross = basic + allowances + overtime + incentives

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.15

    net_salary = gross - deduction

    print("Gross salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net salary: Rs.", net_salary)