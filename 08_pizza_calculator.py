print("---Welcome to Duncan McOkiner's Pizza and Abortion Clinic---"
      "\n---Where yesterdays loss is today's pizza sauce!---")

total_cost = 10.00

crust = str(input("Would you like thick crust or thin crust? ")).lower()
if crust == "thin":
    total_cost = total_cost - 2

base_size = int(input("What base size would you like? We do 8, 10, 12, 14, or 18 inches! "))
if base_size >= 10:
    total_cost = total_cost + 2

cheese = str(input("Would you like cheese on your pizza? Y/N ")).upper()
if cheese == "N":
    total_cost = total_cost - 0.5

type_of_pizza = str(input("What type of pizza would you like? "
                          "\nWe do Margarita, Vegetable, Vegan, Hawaiian and Meat Feast! ")).lower()
if type_of_pizza == "vegetable" or type_of_pizza == "vegan":
    total_cost = total_cost + 1
elif type_of_pizza == "hawaiian" or type_of_pizza == "meat feast":
    total_cost = total_cost + 2

voucher = str(input("Do you have a voucher code? Press enter to skip. "))
if base_size == 18 and voucher == "FunFriday":
    total_cost = total_cost - 2

print(f"Your {crust} crust {base_size} inch {type_of_pizza} pizza comes to ${total_cost}. Enjoy your pizza!")
