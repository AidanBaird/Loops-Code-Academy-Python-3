# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")
print("")

# Create a countdown variable that starts at 10
countdown = 10

# Create a loop that counts down from 10, listing off each never number in count down and eventually typing "We have liftoff!" once it reaches 0.
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")
