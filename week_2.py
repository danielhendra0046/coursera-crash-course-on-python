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


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, seconds, remaining_seconds

hours, minutes, seconds, remaining_seconds = convert_seconds(5000)
print(hours, minutes, remaining_seconds)

# Output:
# 1 23 20


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

# Output:
# Hello Kay. Your lucky number is 27
# Hello Cameron. Your lucky number is 63

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

# Output:
# The distance in kilometers is 88.0
# The round-trip in kilometers is 176.0


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

# Output:
# 99 100

# What are the values passed into functions as input called? = parameters

def lucky_number(name):
  number = len(name) * 9
  hey = "Hello " + name + ". Your lucky number is " + str(number)
  return hey
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

# Output:
# Hello Kay. Your lucky number is 27
# Hello Cameron. Your lucky number is 63

###############################################################################

# SUBCHAPTER CONDITIONALS

# boolean = one of two possible states: true or false


#interesting because the output is true
print("Yellow" > "Cyan")

# Output:
# True

# not operator can make boolean yang menghasilkan false jadi true, atau sebalinya

print(not 42 == "Answer")

# Output:
# True

# To check if two values are the same, we can use the equality operator: == 
# To check if two values are not the same, we can use the not equals operator: != 

# he ability of a program to alter its execution sequence is called branching

# today i learn about if else, ez

def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
	else:
		if len(username) > 15:
			print("Invalid username. Must be at most 15 characters long")
		else:
			print("Valid username")

hint_username("ak")

# Output:
# Invalid username. Must be at least 3 characters long

# you can use elif too, so that code isn't too long

def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
	elif len(username) > 15:
		print("Invalid username. Must be at most 15 characters long")
	else:
		print("Valid username")

hint_username("aku")

# Output:
# Valid username

# Practice Question: Conditionals

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# Output:
# Welcome back Taylor!
# Hello there, John


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks*4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


print(2%4096)
print(7%2)
print(1//4096)

# Output
# 2
# 1
# 0

###############################################################################

# LAST PART ON WEEK 2

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown



def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail



def format_name(first_name, last_name):
	# code goes here
	if first_name == '' and last_name=='':
		string = ""
	elif first_name== '':
		string = "Name: " + last_name
	elif last_name== '':
		string = "Name: " + first_name
	else:
		string = "Name: " + last_name + ", " + first_name
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))



def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))



def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator==0:
		return 0
	else:
		return (numerator/denominator)%1

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0