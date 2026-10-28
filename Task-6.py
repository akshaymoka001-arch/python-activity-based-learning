distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))
travel_class = input("Enter class (Sleeper/AC): ").lower()

if distance <= 0 or age < 0:
    print("Invalid input")
elif travel_class not in ["sleeper", "ac"]:
    print("Invalid travel class")
else:
    if travel_class == "sleeper":
        rate = 1.5
    else:
        rate = 3.0

    fare = distance * rate

    if age < 12:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.8

    reservation_fee = 40
    total = fare + reservation_fee

    print("Base fare: Rs.", fare)
    print("Reservation fee: Rs.", reservation_fee)
    print("Total railway fare: Rs.", total)