


# dictionary mapping
# Initial dictionary
Name = {
    "brand": "LPU",
    "model": "Education",
    "year": 2005
}

# Function to display the dictionary
def display_info(dictionary):
    print("\nCurrent Information:")
    for key, value in dictionary.items():
        print(f"{key.capitalize()}: {value}")
    print()

# Function to update existing keys
def update_info(dictionary):
    key_to_update = input("\nEnter the key you want to update (brand, model, year): ").lower()
    if key_to_update in dictionary:
        new_value = input(f"Enter the new value for {key_to_update}: ")
        dictionary[key_to_update] = new_value
        print(f"{key_to_update.capitalize()} has been updated to {new_value}.")
    else:
        print(f"{key_to_update.capitalize()} is not a valid key.")

# Function to add a new key-value pair
def add_new_key_value(dictionary):
    new_key = input("\nEnter the new key you want to add: ").lower()
    new_value = input(f"Enter the value for {new_key}: ")
    dictionary[new_key] = new_value
    print(f"Added new key-value pair: {new_key.capitalize()} = {new_value}")

# Function to remove a key-value pair
def remove_key(dictionary):
    key_to_remove = input("\nEnter the key you want to remove: ").lower()
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        print(f"{key_to_remove.capitalize()} has been removed.")
    else:
        print(f"{key_to_remove.capitalize()} is not a valid key.")

# Main program loop
def main():
    while True:
        print("\nMenu:")
        print("1. Display Information")
        print("2. Update Information")
        print("3. Add New Key-Value Pair")
        print("4. Remove Key-Value Pair")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            display_info(Name)
        elif choice == "2":
            update_info(Name)
        elif choice == "3":
            add_new_key_value(Name)
        elif choice == "4":
            remove_key(Name)
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()