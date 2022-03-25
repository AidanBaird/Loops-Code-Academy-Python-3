hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create a variable for total_price and set it to 0
total_price = 0

# Create a variable for revenue and set it to 0
total_revenue = 0

# Create a loop to find the total price of all hairstyles
for price in prices:
  total_price += price
  print(total_price)
print("")
print("The total price of hair cuts is", total_price)
print("")

# Create a variable that is the length of the prices variable
length_of_prices = len(prices)
print(length_of_prices)
print("")

# Using the variables for length_of_prices and total_price find the average price of all hair styles
average_price = total_price / length_of_prices
print(average_price)
print("")

# Create a new variable that is prices minus 5
for price in prices:
  new_prices = price - 5
  print(new_prices)
print("")

# Start a for loop that uses the range of hairstyles
for i in range(len(hairstyles)):
  # Using both prices and last_week find the total_revenue
  total_revenue += prices[i] * last_week[i]
  #print(total_revenue)
print("The total revenue for last week was", total_revenue)
print("")
# Find the average daily revenue
daily_revenue = total_revenue / 7
print(daily_revenue)
print("")

# Create a variable of cuts_under_30 by using the range to increase the index (i) and only accepting prices that are below 30 into the variable
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] <= 30]
print(cuts_under_30)