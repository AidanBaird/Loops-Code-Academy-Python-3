sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]


# Creating a variable with current scoops_sold
scoops_sold = 0

# Print the sales data for each location
for location in sales_data:
  print(location)
  # Create a loop that with take each scoop sold in each location and cumuliatively add them to give you your total scoops_sold
  for sold in location:
    scoops_sold += sold
print("")
print(scoops_sold)