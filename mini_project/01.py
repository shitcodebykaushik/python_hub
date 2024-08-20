
number_to_guess = 3    # This is the local varible storage where we have stored the number 
attempts = 3           # This is number of the attempts we are givinig

while attempts > 0:
    print("\nYou have", attempts, "attempt(s) left.")
    print("Choose an operation:")
    print("1. Guess the number")
    print("2. Get a hint")
    print("3. Quit the game")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        guess = int(input("Enter your guess (3,6,8): "))
        if guess == number_to_guess:
            print("Congratulations! You guessed the right number.")
            break
        else:
            print("Wrong guess. Try again.")
            attempts -= 1      # This is deducting our 
            
    elif choice == "2":
        if number_to_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
        attempts -= 1
        
    elif choice == "3":
        print("You have chosen to quit the game.")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if attempts == 0:
    print("\nSorry, you've used all your attempts. The number was:", number_to_guess)
