import random
name = input('whats your name: ')
random_num = random.randint(0,3)
random_num1 = random.randint(0,2)
#1
feeling = input("hello " + name + " how are you doing today: ")
if feeling == "happy" or feeling == "excited" or feeling == "nuetral" or feeling == "good" or feeling == "well":
  print("great keep feeling " + feeling + " " +  name)
elif feeling == 'sad' or feeling == "angry":
  print("there are always tough days " + name)
else:
  print("unknown feeling detected, hope you do better.")
#2
country = input("What country are you from " + name + ": ")

if random_num  == 0:
  print("oh, I heard that "+ country + " has bad political leaders.")
if random_num == 1:
  print("I hate people from " + country + "!")
if random_num == 2:
  print("I love people from " + country + "!")
if random_num == 3:
  print("I would love to visit " + country)
#3
music = input("what type of music do you like to liten to: ")
if random_num1  == 0:
  print("I love " + music)
if random_num1 == 1:
  print("I hate "  + music)
if random_num1 == 2:
  print(music + " is alright i guess")
#4 
food = input(name + " what do you like to eat: ")
if random_num1 == 0:
  print(food + " is kind of bad not going to lie")
if random_num1 == 1:
  print(food + " is amazing")
if random_num1 == 2:
  print("I would love to have " + food + " right now")
#5 
language = input("what language do you speak: ")
if language == "english" or language == "bengali":
  print(" I speak " + language + " aswell!")
elif language == "spanish" or language == "arabic":
  print("I am trying to learn " + language + " right now! ")
else: 
  print("nice, but i have not really looked into "  + language )
#6
chips = input("what are your favorite type of chips: ")
if chips == "potato" or chips == "potato chips":
  print("wow, I love potato chips aswell ")
else:
  print("I know damn well no one eats " + chips +", those are nasty!")

  

  
  