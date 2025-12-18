#Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6 # friends

#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------
total_number_of_slices = party_pizza_mini + large + medium
print(total_number_of_slices)

people = people + 1
slices_per_person = total_number_of_slices // people
leftover_slices = total_number_of_slices - people
print(f"Each person get: {slices_per_person}")
print(f"Lefover slices: {leftover_slices}")

people = people + 2 #Eric and Brandon are coming too.
slices_per_person = total_number_of_slices // people
leftover_slices = total_number_of_slices - people
print(f"Each person gets: {slices_per_person}")
print(f"Leftover slices: {leftover_slices}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_number_of_slices = party_pizza_mini + large + medium
slices_per_person = total_number_of_slices // people
leftover_slices = total_number_of_slices - people
print(f"Each person gets: {slices_per_person}")
print(f"Leftover slices: {leftover_slices}")
print("...for Mr. Hollow Leg")
