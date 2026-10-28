record = input("Enter invoice (code,quantity,amount): ")

data = record.split(",")

if len(data) == 3:
    code = data[0]
    quantity = int(data[1])
    amount = float(data[2])

    print("Product Code:", code)
    print("Quantity:", quantity)
    print("Amount:", amount)
else:
    print("Invalid invoice record")