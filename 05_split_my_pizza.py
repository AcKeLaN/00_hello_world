
print("---Welcome to Split My Pizza---")

try:
    slice_count = int(input("How many slices would you like on your pizza? "))
except ValueError:
    print("You must enter a whole number")
    slice_count = int(input("How many slices would you like on your pizza? "))

try:
    people = int(input("How many people are sharing the pizza? "))
except ValueError:
    print("You must enter a whole number")
    people = int(input("How many people are sharing the pizza? "))

if slice_count < people:
    print("There is too many people to share that many slices")
    try:
        slice_count = int(input("How many slices would you like on your pizza? "))
    except ValueError:
        print("You must enter a whole number")
        slice_count = int(input("How many slices would you like on your pizza? "))

    try:
        people = int(input("How many people are sharing the pizza? "))
    except ValueError:
        print("You must enter a whole number")
        people = int(input("How many people are sharing the pizza? "))

slices_per_person = slice_count // people

slices_left = slice_count % people

print(f"Each person gets {slices_per_person} slices.")
print(f"There will be {slices_left} slices left over.")
