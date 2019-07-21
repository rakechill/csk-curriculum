import random
import sys
import time
from art import *

header = text2art("Go Bears!")
print(header)

# need to fully understand that code so as not to confuse people
typing_speed = 70
def slow_type(msg):
	for letter in msg:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)
	print('')

###########
# ~ Intro ~
slow_type("Hello there! Before we embark on this Cal adventure, what is your name?")
name = input()

slow_type("Congratulations, " + name + ". You are going to be a student at the world's number one public university! Woohoo! \
This definitely calls for a Go Bears! Your first decision as a fresh new Cal Bear is to pick your top 3 \
dorms to live in. What shall it be? The ever lush Clark Kerr Campus? Or Unit 1 the #1? Or perhaps Berkeley's \
newest dorm, Blackwell? Choose wisely!\n")

dorms = ["Unit 1", "Unit 2", "Unit 3", "Stern", "Foothill", "Bowles", "Clark Kerr", "Blackwell"]

slow_type("For the following choices, use the corresponding number for each dorm.")
print()

for ind in range(8):
	print(str(dorms[ind]) + " - " + str(ind+1))

print()
print("What is your first choice?")
first_dorm = int(input())
print("What is your second choice?")
second_dorm = int(input())
print("What is your third choice?")
third_dorm = int(input())

top_3 = [first_dorm, second_dorm, third_dorm]
rest = [dorm for dorm in [1,2,3,4,5,6,7,8] if dorm not in top_3]

rand = random.randint(1,10)

if rand <= 4:
	dorm = first_dorm
elif rand <= 6:
	dorm = second_dorm
elif rand == 7:
	dorm = third_dorm
else: 
	dorm = random.choice(rest)


slow_type("Your assignment has been chosen! " + str(dorms[dorm-1]) + " will be your dorm for the year! \n")

print("<><><><><><><><><><><><>")

########################
# Choosing your roommate
# One of two friends or random choice between five other people.
def print_bio(roommate):
	slow_type("Name: " + roommate[0])
	slow_type("How you know them: " + roommate[1])
	slow_type("Fun fact: " + roommate[2])
	slow_type("Not so fun fact: " + roommate[3] + "\n")

# people you know
amy = ["Amy", "You have been family friends since you were 3", "She can sing really well and is always down for dance parties.", "You haven’t kept in touch that much over the years, so you’re not sure what she would be like as a roommate."]
michelle = ["Michelle", "You are friends from high school.", "She’s really good at math, and you know her pretty well.", "She talks like…a lot, even when you’re trying to study."]

# random
carol = ["Carol", "Random roommate", "She is from your hometown and you have a lot of mutuals.", "One of those mutuals is her boyfriend who happens to be your ex."]
cassandra = ["Cassandra", "Random roommate", "She has really cute clothes, is your size, and said you can borrow them whenever you want. Two wardrobes!", "She brings random friends into your dorm after midnight every weekend."]
hannah = ["Hannah", "Random roommate", "She has a ton of snacks stocked up at any given time and is always down to share.", "She leaves messes all over the room and doesn't clean them up for weeks."]
sharon = ["Sharon", "Random roommate", "You both have a lot in common and become best friends.", "Honestly she's perfect. You got lucky."]
becky = ["Becky", "Random roommate", "She is superrrr clean and doesn't care if you are or aren't.", "She's just kind of boring, but is a good enough roommate."]

randoms = [carol, cassandra, hannah, sharon, becky]

slow_type("Now it's time to choose your roommate! To go random or not to go random...that is the question. You have two people you know: \n")
print_bio(amy)
print_bio(michelle)

choice = (input("Type Amy or Michelle if you want to room with them, or type random to be randomly assigned a roommate: ")).strip().lower()
print()

# good examples for improving input error checking using .strip() and .lower() so that every answer will be of the same format.
if choice == "amy":
	print("Congrats, your roommate is Amy!")
	your_roommate = amy
elif choice == "michelle":
	print("Congrats, your roommate is Michelle!")
	your_roommate = michelle
else:
	your_roommate = random.choice(randoms) #this chooses a random element of a sequence
	print_bio(your_roommate)

print("<><><><><><><><><><><><>")

################
# Making Friends

slow_type("Making friends is a really important (and fun!) part of college! You've just moved in and you see some people hanging out in the lounge in your dorm.")
talk = input("Do you wanna go talk to them ? y/n ").strip().lower()
if talk == 'y':
	slow_type("Congrats! You just made some friends! They're all really excited to meet someone new, too!")
	dinner = int((input("It's getting close to dinnertime and everyone's kinda hungry. Do you wanna go to Croads or Asian Ghetto? Type 1 for Croads or 2 for Asian Ghetto: ")).strip())
	if dinner == 1:
		slow_type("\n You go to Croads, and all had a grand time eating copious amounts of kind of good food! Definitely the beginning of a great friendship.\n")
	else:
		slow_type("\n You go to Asian Ghetto, but what to eat?? You really can't go wrong with great classics like Gypsy's, Thai Basil, Mandarin House, Bear Ramen House, and Boba Ninja! So just go with your gut and who knows, maybe you'll find your ~favorite~ place in Berkeley.\n")
else:
	slow_type("\n Talking to people can be hard, but just remember that everyone else is new to Berkeley and nervous, too. Don't worry, there will be plenty of other opportunities to meet people! Go ahead and continue binging your favorite Netflix show and order takeout. No judgement.\n ")

print("<><><><><><><><><><><><>")

###############
# Joining clubs

slow_type("Calapalooza is today and you have no idea what to join?!? There are so many clubs on campus from singing groups to service clubs to professional clubs. How are there so many business clubs?? Why do they have applications? Nothing makes sense :( \n")
slow_type("Okay, breathe. There are a ton of awesome clubs to join and also 8 whole semesters for you to join them. Just take flyers from things that interest you and don't let it get you down if you don't get into one of them. Try to choose some that have applications, and some that don't! \n")

clubs_w_apps = ["Berkeley Forum", "Drawn to Scale Acappella", "Mobile Developers at Berkeley", "Cal Dragon Boat", "AFX"]
clubs_wo_apps = ["Songwriting at Berkeley", "Association of Women in EECS (AWE)", "Open Computing Facility (OCF)", "Society of Women Engineers (SWE)", "Salsa at Cal"]

slow_type("\nFor the following choices, use the corresponding number for each club. \n")

for club in range(len(clubs_w_apps)):
	print(str(clubs_w_apps[club]) + " - " + str(club+1))

club1 = int(input("All of these clubs have applications, but don't shy away from them give it your best shot! Choose one to apply to: ").strip())

print("\nFor the following choices, use the corresponding number for each club. \n")

for club in range(len(clubs_wo_apps)):
	print(str(clubs_wo_apps[club]) + " - " + str(club+1))

club2 = int(input("None of these clubs have applications, so just go to their general meetings and see what they're all about! Choose one to try out: ").strip())

print("\nGo you! You've taken a big step and decided to join some clubs! This will help you start to build your community here at Cal. Best of luck with your " + str(clubs_w_apps[club1-1]) + " application and I hope you have fun at " + str(clubs_wo_apps[club2-1]) + "'s first GM!\n")

print("<><><><><><><><><><><><>")

##############
# Getting sick

print("\nSadly getting sick is a part of life, but it can be scary sometimes when you're so far away from home and don't know what to do.\n")
print("\nThis is the first time that you've been away from home for so long, and you woke up today puking.\n")

options = ["call home", "cry in bed and hope you'll feel better soon", "take whatever medicine your roommate just handed you", "go to Tang Center"]

print("\nFor the following choices, use the corresponding number. \n")

for option in range(len(options)):
	print(str(options[option]) + " - " + str(option+1))

choice = int(input("\nWhat do you do? Type the number of your choice. ").strip())

if options[choice-1] == "go to Tang Center":
	print("\nGoing to the Tang Center is definitely the best option, since they can run tests and write you a doctor's note to miss class.\n")
else:
	print("\nYou can " + str(options[choice]) + ", but your best option is probabl to go to the Tang Center, since they can run tests and write you a doctor's note to miss class.\n")

print("<><><><><><><><><><><><>")

###################
# Going to Get Boba
# Since Berkeley students get boba so often, we can use it as a way to introduce functions (we want functions to be associated with something you repeat)

boba_places = ["Gong Cha", "U Cha", "Sharetea", "Purple Kow", "RareTea", "Asha", "Tea One", "Happy Lemon", "T Zone", "Yi Fang"]

def getboba():
	print("Ahhh! The boba cravings attack again!!! You and your friends really wanna get boba but can't decide between two places. They turn to you, " + name + ", to make the final decision for them.")
	first_choice = str(random.choice(boba_places))
	second_choice = str(random.choice(boba_places))
	while first_choice == second_choice:
		second_choice = str(random.choice(boba_places));
	print("Where should you get boba? " + first_choice + " or " + second_choice + "?")
	answer = input()
	print(answer + " it is! Good choice!")

print()
getboba()

print("<><><><><><><><><><><><>")

# Getting a job

print("\nIt's been a few weeks and boba has already started to hurt your bank account. Not to mention, your financial aid has just been finalized and you're not getting nearly as much money as you needed to. It's time to get a job!\n")
print("\nYou have a few options for on-campus jobs that accept work-study. Where do you want to work?\n")
print("\nFor the following choices, use the corresponding number for each job. \n")

jobs = ["Library information desk worker", "Cal Dining worker", "Research assistant", "Cal Performances usher", "Call center worker"]

for job in range(len(jobs)):
	print(str(jobs[job]) + " - " + str(job+1))

first_choice = int(input("\nWhat's your first choice: ").strip())
second_choice = int(input("\nWhat's your second choice: ").strip())

job = random.choice([first_choice, second_choice])

if job == first_choice:
	print("\nCongrats! You got your first choice job as a " + str(jobs[job-1]) + "\n")
else:
	print("\nYour interview didn't go too well, so you got your second choice job as a " + str(jobs[job-1]) + ", but I'm sure it'll still be great!\n")

print("<><><><><><><><><><><><>")

# Example of a choice that impacts the storyline

print("There are only a few weeks left in the semester and you're quite behind in CS 61A. Crap! Should you still attend lecture or watch them at home on 2x speed? Answer 1 for attending lecture, 2 for watching at home.")
cs61alecture = input()
if cs61alecture == 1:
	rand = random.randint(1,4)
	if rand <= 3:
		print("Yay! Your choice paid off. You got a good grade in CS61A.")
	else:
		print("Crap. Maybe that didn't work so well. Your grade in CS61A isn't what you expected. Don't worry, it's only the first class, though!")
else:
	rand = random.randint(1,2)
	if rand == 1:
		print("Yay! Your choice paid off. You got a good grade in CS61A.")
	else:
		print("Crap. Maybe that didn't work so well. Your grade in CS61A isn't what you expected. Don't worry, it's only the first class, though!")

# Later in the storyline, can reference the grade in CS61A

