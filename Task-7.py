email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

if len(reg_id) == 10 and reg_id.isalnum():
    print("Valid registration ID")
else:
    print("Invalid registration ID")