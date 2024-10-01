while True:
    print("Input the H value...")
    user_input = input("Enter '-h' to end the loop: ")
    if user_input == 'H' :
        print ("Loop is infinte")
    elif user_input == '-h':
        print("Stopping the loop.")
        break