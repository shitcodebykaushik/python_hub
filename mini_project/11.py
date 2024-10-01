# Create a dictionary
my_dict = {
  "apple": "red",
  "banana": "yellow",
  "cherry": "red"
}

# Check if a key exists using the `in` operator
if "apple" in my_dict:
  print("Yes, 'apple' is a key in the dictionary")
else:
  print("No, 'apple' is not a key in the dictionary")

# Check if a key exists using the `get()` method
if my_dict.get("banana") is not None:
  print("Yes, 'banana' is a key in the dictionary")
else:
  print("No, 'banana' is not a key in the dictionary")

# Check for a key that doesn't exist
if "grape" in my_dict:
  print("Yes, 'grape' is a key in the dictionary")
else:
  print("No, 'grape' is not a key in the dictionary")