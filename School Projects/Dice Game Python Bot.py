import random
win = 0
bot_win = 0
tie = 0
user_input = ''
while user_input != "stop":
  user_input = input("enter roll to roll dice (stop to stop): ")
  if user_input == "stop":
    break
  dice1 = random.randint(1,6)
  dice2=random.randint(1,6)
  botdice1=random.randint(1,6)
  botdice2=random.randint(1,6)
  sum1 = dice1 + dice2
  sum2 = botdice1 + botdice2
  print('1st dice: ' + str(dice1))
  print("2nd dice: " + str(dice2))
  print('\nbot 1st dice: ' + str(botdice1))
  print('bot 2nd dice: ' + str(botdice2))
  print('\nyou rolled: ' + str(sum1))
  print("bot rolled: " + str(sum2))
  if sum1 > sum2:
    print("\t YOU WIN")
    win += 1
  if sum1<sum2:
    print("\t BOT WINS")
    bot_win +=1
print('\nyour wins: ' + str(win))
print('bots win:' + str(bot_win))
if bot_win>win:
  print("\nBOT WINS")
if win> bot_win:
  print("\nYOU WIN")
if win == bot_win:
  print("ITS A TIE")