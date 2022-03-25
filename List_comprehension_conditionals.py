heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
accepted_visitors = []

#Example of nested loop to tackle same problem?
for height in heights:
  if height > 161:
    accepted_visitors.append(height)

#Using list comprehension create a list of those allowd to ride the coaster
can_ride_coaster = [height for height in heights if height > 161]

# Printing commands
print(accepted_visitors)
print("")
print(can_ride_coaster)
