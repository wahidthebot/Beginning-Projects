import random

win = 0
loose = 0
tie = 0
options = ["rock", "paper", "scissor"]
bot_choice = random.choice(options)

games = int(input("How many times do you want to play: "))

for i in range(games):
    user_input = input("Enter a move: ")
    print("Bot chose " + bot_choice)

    if user_input == "rock" and bot_choice == "scissor":
        win += 1
        print("You win!")
    elif user_input == "paper" and bot_choice == "rock":
        win += 1
        print("You win!")
    elif user_input == "scissor" and bot_choice == "paper":
        win += 1
        print("You win!")
    elif user_input == "scissor" and bot_choice == "rock":
        loose += 1
        print("You lose!")
    elif user_input == "rock" and bot_choice == "paper":
        loose += 1
        print("You lose!")
    elif user_input == "paper" and bot_choice == "scissor":
        loose += 1
        print("You lose!")
    elif user_input == bot_choice:
        tie += 1
        print("It's a tie!")
        
    bot_choice = random.choice(options)

print("Wins: " + str(win))
print("Losses: " + str(loose))
print("Ties: " + str(tie))