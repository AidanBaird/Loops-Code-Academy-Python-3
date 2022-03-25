dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

# Create a for loop that goes through the  dog_breeds_available_for_adoption variable in order and then prints the dog_breed in question
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  # Create an if statement that upon finding variable dog_breed_I_want will print statement and break the loop
  if dog_breed == dog_breed_I_want:
    print("")
    print("They have the dog I want!")
    break
