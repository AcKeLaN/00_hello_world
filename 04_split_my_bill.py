
print("---Welcome to Split My Bill---")

try:
    bill_total = float(input("What is the total bill? "))
except ValueError:
    print("You must enter a number")
    bill_total = float(input("What is the total bill? "))

try:
    people = int(input("How many people are sharing? "))
except ValueError:
    print("You must enter a number")
    people = int(input("How many people are sharing? "))

try:
    tip_percentage = int(input("What percentage tip would you ike to leave? "))
except ValueError:
    print("You must enter a number")
    tip_percentage = int(input("What percentage tip would you ike to leave? "))

percentage_decimal = tip_percentage / 100
tip_total = bill_total * percentage_decimal

bill_total = bill_total + tip_total

cost_per_person = bill_total / people

print(f"Total bill including tip is ${bill_total}")
print(f"Total cost per person is ${cost_per_person}")
