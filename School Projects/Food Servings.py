print("already made foods: [ lemonade ][ bread][ cool aid ]")
print("or make [custom] ")

foods = input("\nenter a food that you want to make: ")

if foods == "lemonade":
  serving1 = float(input("enter the amount of servings: "))
  print("lemons: " + str(0.5 * serving1))
  print("lemon juice: " + str(1.5 * serving1) + "table spoons")
  print("water: " + str(16 *serving1) + "oz")
  print("sugar: " + str(25 * serving1) + "grams")

if foods == "bread":
  serving2 = float(input("enter the amount of servings: "))
  print("dough: " + str( 1 * serving2) + " pounds of dough")
  print("water: " + str(150* serving2) + " gallons of water")
  print("yeast: " + str(2.25 *serving2) + " table spoons")
  print("sugar: " + str(2 * serving2) + " grams")

if foods == "cool aid":
  serving3 = float(input("enter the amount of servings: "))
  print("fructose: " + str( 0.2 * serving3) + "grams")
  print("water: " + str(1* serving3) + " cup(s) of water")
  print("citric acid: " + str(0.2 *serving3) + " grams")
  print("sugar: " + str(1 * serving3) + " cup")

if foods == "custom":
  serving_make = float(input("enter how many servings can you make: "))
  
  serving_made = float(input("how many servings will you make: "))
  servings4 = serving_make/serving_made
  
  ing1 = input("\nwhat is the 1st ingrediant: ")
  ing2 = input("what is the 2nd ingriediant: ")
  ing3 = input("what is the 3rd ingriediant: ")
  ing4 = input("whatsi the 4th ingriediant: ")

  ing1_amount = float(input("\nhow many of the 1st ingridient do you need to use: "))
  ing2_amount = float(input("how many of the 2nd ingridient do you need to use: "))
  ing3_amount = float(input("how many of the 3rd ingridient do you need to use: "))
  ing4_amount = float(input("how many of the 4th ingridient do you need to use: "))

  print(str(ing1) + ": " + str(ing1_amount * servings4))
  print(str(ing2) + ": " + str(ing2_amount * servings4))
  print(str(ing3) + ": " + str(ing3_amount * servings4))
  print(str(ing4) + ": " + str(ing4_amount * servings4))
else:
  print(" food not recognized \n Enter [custom]  to make own food ")