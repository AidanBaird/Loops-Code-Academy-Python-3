grades = [90, 88, 62, 76, 74, 89, 48, 57]

# Create a variable of grades scaled by +10
#for grade in grades:
  #scaled_grades = grade + 10
  #print(scaled_grades)

# Create a variable of grades scaled by +10 #2
scaled_grades = [grade + 10 for grade in grades]

# Printing commands
print(grades)
print("")
print(scaled_grades)