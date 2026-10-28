consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges")
else:
    total = consultation + diagnostic + treatment

    if total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Total bill: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final bill: Rs.", final_bill)

    if final_bill >= 5000:
        print("Classification: High payment")
    else:
        print("Classification: Regular payment")