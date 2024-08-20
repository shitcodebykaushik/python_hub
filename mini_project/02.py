atm_pin = "12203450"
attempts = 3

while attempts > 0:
    pin = input("Enter your pin: ")
    if pin == atm_pin:
        print("Your pin is Ok")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong pin. Try again. Attempts remaining: {attempts}")
        else:
            print("\nSorry, you've used all your attempts. The correct PIN was:", atm_pin)
            print("Contact the bank")


