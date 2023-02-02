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

###############################################################################
