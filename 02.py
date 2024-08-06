
print("This is python class")
# Example variables
integer_value = 42
float_value = 3.14159
string_value = "123"
boolean_value = True

# Printing with type conversion
print("Integer to string:", str(integer_value))
print("Float to string:", str(float_value))
print("String to integer:", int(string_value))
print("Boolean to string:", str(boolean_value))

# Using f-strings
print(f"Integer to string with f-string: {str(integer_value)}")
print(f"Float to string with f-string: {str(float_value)}")
print(f"String to integer with f-string: {int(string_value)}")
print(f"Boolean to string with f-string: {str(boolean_value)}")


print("Integer to string with format: {}".format(str(integer_value)))
print("Float to string with format: {}".format(str(float_value)))
print("String to integer with format: {}".format(int(string_value)))
print("Boolean to string with format: {}".format(str(boolean_value)))


import math

def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area


radius = float(input("Enter the radius of the circle: "))

area = calculate_area_of_circle(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

# Making the sudent based system .
print (" The marks of the class ")
marks=int (input("Enter your marks"))
print (" The marks of the class ")
if marks >= 90:
    print("You got Grade A ")
if marks >= 80:  
    print("You got Grade B ")
if marks >= 80: 
    print("You got Grade D")
if marks >= 40: 
      print("You got Grade E")
if marks == 0:
    print("You are failed")


# Leap year 
