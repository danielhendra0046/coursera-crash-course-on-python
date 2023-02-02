# Website: https://www.coursera.org/learn/python-crash-course/home/week/2

##################################################################################

# SUBCHAPTER - FUNCTIONS


# print() that is the type of function
# assignment → storing variable



def greeting(name, department):
	print("Welcome, " + name)
	print("You are part of " + department)

greeting("Blake", "IT Support")

# Output:
# Welcome, Blake
# You are part of IT Support



def area_triangle(base, height):
	return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

# Output
# The sum of both areas is: 20.5


#def convert_seconds(second):
#	hours = seconds // 3600
#	minutes = (seconds - hours * 3600) // 60
#	remaining_seconds = seconds - hours * 3600 - minutes * 60
#	return hours, minutes, remaining_seconds

#hours, minutes, seconds = convert_seconds(5000)
#print(hours, minutes, seconds)

# Output:
# 1 23 30


def greeting(name):
	print("Welcome, " + name)

result = greeting("Christine")

# Output:
# Welcome, Christine

print(result)

# Output:
# None

def lucky_number(name):
	number = len(name) * 9
	print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2.0*my_trip_km))


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# What are the values passed into functions as input called? = parameters

def lucky_number(name):
  number = len(name) * 9
  hey = "Hello " + name + ". Your lucky number is " + str(number)
  return hey
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

###############################################################################
