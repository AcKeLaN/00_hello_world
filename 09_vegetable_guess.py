print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
print("I will attempt to guess your choice"
      "\n-----------------------------------")

answer = input("Is your vegetable green? Y/N ").lower()

if answer == "y":
    answer = input("Does your vegetable look like a tree? Y/N ").lower()
    if answer == "y":
        print("It must be broccoli!")
    else:
        print("It must be peas!")
elif answer == "n":
    answer = input("Is your vegetable orange? Y/N ").lower()
    if answer == "y":
        print("It must be a carrot!")
    else:
        print("It must be sweetcorn!")
