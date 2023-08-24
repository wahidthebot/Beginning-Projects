import sys
import random
points =  0 

#intro prompt
while True:
    start = input("do you want to start the quiz: ")
    if start == "yes":
        print("alright lets begin")
        break
    elif start == "no":
        sys.exit("okay maybe next time")
    else:
        print("invalid prompt try again")

#1st question
while True:
    q1 = input("What furniture do you like the best? \n A. Chair \n B. Sofa \n C. Couch \n D. Bed \n Answer here: ").lower()
    
#1st question prompts
    if q1 in ["a", "chair"]:
        points += 10
        print("Really bro.... a chair?")
        break

    if q1 in ["b" , "sofa"]:
        points += 20
        print("sofa's can be comfortable at times...")
        break

    if q1 in ["c" , "couch"]:
        points += 30
        print("couche's are much better than sofa's......")
        break
    
    if q1 in ["d" , "bed"]:
        points += 40
        print("sofa's can be comfortable at times...")
        break
    
    else:
        print("invalid asnwer, try again")

import random

points = 0

while True:
    q2 = input("What would you most like to do in your free time?\nA. Video games\nB. Sleep\nC. Spend time on a computer\nD. Talk/Hangout with friends\nAnswer here: ")
    
    if q2.lower() in ["a", "video games", "games", "game"]:
        points += 10
        q2_2 = input("Oh wow, what's your favorite game? ")
        list1 = ["I heard that " + q2_2 + " is a horrible game!", "I love " + q2_2, "OMG, I play " + q2_2 + " as well"]  
        random1 = random.choice(list1)
        print(random1)
        break

    elif q2.lower() in ["b", "sleep"]:
        while True:
            try:
                sleep = float(input("How many hours of sleep: "))
                if sleep in [1, 2, 3, 4, 5]:
                    print("A little nap never hurts....")
                elif sleep in [6, 7, 8]:
                    print("That's a lot of free time....")
                elif sleep in [9, 10, 11]:
                    print("I wish I had gotten that much sleep.")
                elif sleep > 11:
                    print("That is a crazy amount of sleep!")
                else:
                    print("Invalid input. Please enter a valid number.")
                    continue  
                break  
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        break

    elif q2.lower() in ["c", "spend time on a computer", "computer", "spend time on pc", "pc", "computers", "technology", "phone"]:
        points += 20
        q2_3 = input("What do you like to do on your " + q2 + "? ")
        if q2_3.lower() in ['code', 'watch educational videos', 'tutor', 'learn', 'learn new things']:
            points += 5
            print("Wow, that's a great thing to do on a " + q2 + "!")
        else:
            print("There are better things to do on a " + q2 + ", but I guess you do you!")
            points -= 5
        break

    elif q2.lower() in ["d", "talk/hangout with friends", "talk with friends", "hangout with friends", "friends", "spend time with friends"]:
        points += 30
        while True:
            try:
                q2_4 = float(input("How many hours do you hang out with your friends: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        points += q2_4
        
        if q2_4 in [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Wow, you're a really good friend!")
        if q2_4 > 9:
            print("Uh-oh, don't you think that's a little bit too much?")
        if q2_4 < 0.5:
            print("You could be spending a little bit more time with friends.")
        break

    else:
        print("Invalid response. Please try again.")



#3rd question
while True:
    q3 = input("Pick a super power \n A. Invisibility \n B. Flight \n C. Speed \n D. Strength \n answer here: ")

#3rd question promps
    if q3 in["a" , "invisibility"]:
        print("smart, you can go anywhere and do anything without people knowing it was you!")
        points += 10
        break

    if q3 in ["b" , "flight" , "fly"]:
        print("Flight would be a very eeficeint way to get to places easier!")
        points += 20
        break

    if q3 in ["c" , "speed" , "running"]:
        print("speed woud be a smart way to get to places faster")
        points += 30
        break

    if q3 in ["d" , "strength" , "muscles" , "strong" , "muscular"]:
        print("I would love to be a strong super hero aswell")
        points += 40
        break
    else:
        print("invalid prompt, try again")

#4th question
while True:
    q4 = input("whats your favorite type of food? \n A. Spicy \n B. Sweet \n C. Sour \n D. Salty \n answer here: ")
#4th question prompts
    if q4 in ["spicy" , "hot" , "a" , "A"]:
        print("did you know eating hot foods tricks your tongue into thinking its atcually on fire.")
        points += 10
        break

    if q4 in ["sweet" , "sugar", "sugary" , "b" , "B"]:
        print("sweet food's can lead to tooth rotting and mess up your mouth and gum's")
        points += 20
        break

    if q4 in ["sour" , "tangy" , "soury" , "c" , 'C']:
        print("too much sourness can burn through the tongue and gums, and lead to a weaker mouth.")
        points += 30
        break
    
    if q4 in ["salty" , "salt" , "d" , "D"]:
        print("did you know salt absorbs the bodies water, causing you to drink more water.")
        points += 40
        break

#question 5
while True:
    q5 = input("what type of movies do you like watching the most? \n A. Romance \n B. Drama \n C. Horror \n D. Action/Adventure \n E. Comedy \n F. Sci-Fi \n answer here: ")
#question 5 prompts
    if q5 in['a' , "romance"]:
        points += 10
        break

    if q5 in["drama" , "b"]:
        points += 20
        break
    
    if q5 in["c" , "horror" , "scary"]:
        points += 30
        break
    
    if q5 in ["d" , "action/advenure" , "action" , "adventure"]:
        points += 40
        break

    if q5 in ["e" , "comedy" , "funny" , "jokes" , "halarious"]:
        points += 50
        break

    if q5 in ["f" , "sci fi" , "scifi" , "sci-fi" , "science fiction"]:
        points += 60
        break
    else:
        print("invalid prompt, try again")

#question 6
q6 = input("what is your favorite tv show\movie: ")
if q6 == "spiderman" or q6 == "spongebob":
    print("i love "+ q6 + " aswell")
    points += 100
else:
    print("have not heard of that one yet, ill be sure to check it out")
    points += 10

#question 7

q7 = input("what is your goal in the future: ")
if q7 == "software enginering" or q7 == "computer engineering" or q7 == "development":
    print("woah! Im into that aswell")
    points += 50
if q7 == "nothing" or q7 == "n/a":
    print("i hope you think more about yyour future later on!")
    points -= 50
else:
    print ("good luck with your journey!")
    points += 30

#question 8
while True:
    q8 = input("can you handle stress: ")
    if q8 == "yes":
        print("thats a very good trait to have")
        points += 30
        break
    if q8 == "no":
        print("you should work on that trait since its very good to have")
        break
    else:
        print("invalid prompt, try again")


#question 9 
while True:
    q9 = input("what is your prefered method of communication? \n A: text \n B: Phone call \n C: Face to Face \n D: Email \n Answer here:")
    if   q9 in['a' , "A" , "text" , "Text"]:
        points += 10
        break

    if q9 in["B" ,"b" , "phone" , "call" , "Phone" , "Call" , "phone call" , "Phone Call" , "Phone call"]:
        points += 20
        break
    
    if q9 in["c" , "C" , "face to face" , "Face to Face"]:
        points += 30
        break
    
    if q9 in ["d" , "D" , "email" , "Email"]:
        points += 40
        break
    
    else:
        print("invalid prompt try again")


#question 10
while True:
    q10 = input("What is your preferred mode of exercise: \n A: Yoga \n B: Running \n C: Team Sports \n D: Weight Lifting \n Answer here: ")
    
    if q10 in ["a", "A", "Yoga", "yoga"]:
        points += 10
        break
    elif q10 in ["b", "B", "Running", "running"]:
        points += 20
        break
    elif q10 in ["c", "C", "Team Sports", "Team sports"]:
        points += 30
        break
    elif q10 in ["d", "D", "Weight Lifting", "weight lifting"]:
        points += 40
        break
    else:
        print("Invalid prompt, try again")


# Display points and personality description
print("\nQuiz completed! You have gathered", points, "points.\n")

if points <= 150:
    print("Your personality is introverted and laid-back.")
    print("You enjoy relaxing activities and prefer spending time alone or with a small group of close friends.")
    print("You find solace in calm environments and may be more introspective and reserved in social interactions.")
    print("You recharge your energy through quiet moments and introspection.")

elif points <= 200:
    print("Your personality is balanced and adaptable.")
    print("You have a mix of introverted and extroverted tendencies, enjoying both quiet activities and socializing.")
    print("You are comfortable in various social settings and can easily adapt to different situations.")
    print("You value both personal time for reflection and moments of connection with others.")

elif points <= 300:
    print("Your personality is outgoing and energetic.")
    print("You thrive in social situations and enjoy being around people, engaging in various activities and adventures.")
    print("You have a zest for life and seek out new experiences and opportunities for social interactions.")
    print("You are energized by the presence of others and often take the lead in group settings.")

else:
    print("Your personality is ambitious and driven.")
    print("You are highly motivated, have diverse interests, and enjoy taking on challenges and pursuing your goals.")
    print("You are proactive and constantly seeking personal and professional growth.")
    print("You thrive on achieving success and are willing to put in the effort required to accomplish your ambitions.")
