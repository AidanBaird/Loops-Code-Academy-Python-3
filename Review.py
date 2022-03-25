# Create a list that ranges from 1-9
single_digits = list(range(0,10))

#Create a variable called squares
squares = []

# Creating a list of the digits in single digits
# Create a second list that times digits with itself then creates those new digits into a new variable
for digits in single_digits:
  squares.append(digits * digits)
  cubes = [digits **3 for digits in single_digits]
#print(digits)
#print(squares)
#print(cubes)

# Printing commands
print("")
print(single_digits)
print("")
print(squares)
print("")
print(cubes)