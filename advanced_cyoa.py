import random
import sys
import os
import time
from art import text2art

def slow_type(msg, speed=70):
	for letter in msg:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/speed)
	print('')

###############
# FOR DEBUGGING
###############

# replace slow_type instances with printr for faster debugging
def printr(msg, speed=70):
	print(msg)

""" still too slow? Replace instances of time.sleep with # time.sleep
	to remove all delays. """

###########
# ~ Intro ~
###########
os.system('cls' if os.name == 'nt' else 'clear')
header = text2art("Go Bears!")
print(header)

slow_type("Hello there! Before we embark on this Cal adventure, what is your name?")
name = input()

####################
# Choosing Your Dorm
####################

os.system('cls' if os.name == 'nt' else 'clear')
part_1 = text2art("Part 1: Choosing Your Dorm")
print(part_1)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

print("\nCongratulations, " + name + ". You are going to be a student at the world's number one(?) public university! Woohoo! \
\nThis definitely calls for a Go Bears! Your first decision as a fresh new Cal Bear is to pick your top 3 \
dorms to live in. \nWhat shall it be? The ever lush Clark Kerr Campus? Or Unit 1 the #1? Or perhaps Berkeley's \
newest dorm, Blackwell? Choose wisely!\n")

input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

dorms = ["Unit 1", "Unit 2", "Unit 3", "Stern", "Foothill", "Bowles", "Clark Kerr", "Blackwell"]

slow_type("\nFor the following choices, use the corresponding number for each dorm.\n")

for ind in range(8):
	print(str(dorms[ind]) + " - " + str(ind+1))

print("\nWhat is your first choice?")
first_dorm = int(input())
print("\nWhat is your second choice?")
second_dorm = int(input())
print("\nWhat is your third choice?")
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

slow_type("\nYour assignment has been chosen! " + str(dorms[dorm-1]) + " will be your dorm for the year! \n")

time.sleep(2)

########################
# Choosing your roommate
########################

# One of two friends or random choice between five other people.
os.system('cls' if os.name == 'nt' else 'clear')
part_2 = text2art("Part 2: Choosing Your Roommate")
print(part_2)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

def print_bio(roommate):
	print("\033[0;35;40mName: " + roommate[0])
	time.sleep(1)
	print("How you know them: " + roommate[1])
	time.sleep(2)
	print("Fun fact: " + roommate[2])
	time.sleep(3)
	print("Not so fun fact: " + roommate[3] + "\n")
	time.sleep(4)
	print("\033[0;0m")

# people you know
amy = ["Amy", "You have been family friends since you were 3", "She can sing really well and is always down for dance parties.", "You haven’t kept in touch that much over the years, so you’re not sure what she would be like as a roommate."]
michelle = ["Michelle", "You are friends from high school.", "She’s really good at math, and you know her pretty well.", "She talks like…a lot, even when you’re trying to study."]

# random
cara = ["Cara", "Random roommate", "She is from your hometown and you have a lot of mutuals.", "One of those mutuals is her boyfriend who happens to be your ex."]
shriya = ["Shriya", "Random roommate", "She has really cute clothes, is your size, and said you can borrow them whenever you want. Two wardrobes!", "She brings random friends into your dorm after midnight every weekend."]
hannah = ["Hannah", "Random roommate", "She has a ton of snacks stocked up at any given time and is always down to share.", "She leaves messes all over the room and doesn't clean them up for weeks."]
julia = ["Julia", "Random roommate", "You both have a lot in common and become best friends.", "Honestly she's perfect. You got lucky."]
becky = ["Becky", "Random roommate", "She is superrrr clean and doesn't care if you are or aren't.", "She's just kind of boring, but is a good enough roommate."]

randoms = [cara, shriya, hannah, julia, becky]

print("\nNow it's time to choose your roommate! To go random or not to go random...that is the question. You have two people you know: \n")
time.sleep(4)

print_bio(amy)
print_bio(michelle)

# good examples for improving input error checking using .strip() and .lower() so that every answer will be of the same format.
choice = (input("Type Amy or Michelle if you want to room with them, or type random to be randomly assigned a roommate: ")).strip().lower()
print()

if choice in ["amy", "am", "a", "ammy"]:
 	print("Congrats, your roommate is Amy!")
 	your_roommate = amy
elif choice in ["michelle", "mich", "michele", "michel", "mi"]:
 	print("Congrats, your roommate is Michelle!")
 	your_roommate = michelle
else:
	your_roommate = random.choice(randoms) #this chooses a random element of a sequence
	slow_type("Congrats! your roommate is... ")
	time.sleep(2)
	print_bio(your_roommate)

input("Press any key to continue... ")

################
# Making Friends
################

os.system('cls' if os.name == 'nt' else 'clear')
part_3 = text2art("Part 3: Making Friends")
print(part_3)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nMaking friends is a really important (and fun!) part of college! You've just moved in and \
you see some people hanging out in the lounge in your dorm.")
talk = input("\nDo you wanna go talk to them ? y/n ").strip().lower()

os.system('cls' if os.name == 'nt' else 'clear')

if talk == 'y':
	print("\nCongrats! You just made some friends! They're all really excited to meet someone new, too!")
	print("\nIt's getting close to dinnertime and everyone's kinda hungry. \nDo you wanna go to Croads or Asian Ghetto? Type 1 for Croads or 2 for Asian Ghetto: ")
	dinner = int(input())
	if dinner == 1:
		dinner = "Croads"
		slow_type("\nYou go to Croads, and all had a grand time eating copious amounts of kind of good food! Definitely the beginning of a great friendship.\n")
	else:
		dinner = "Asian Ghetto"
		slow_type("\nYou go to Asian Ghetto, but what to eat?? You really can't go wrong with great classics like Gypsy's, Thai Basil, Mandarin House, Bear Ramen House, and Boba Ninja! \nSo just go with your gut and who knows, maybe you'll find your ~favorite~ place in Berkeley.\n")

else:
	slow_type("\nTalking to people can be hard, but just remember that everyone else is new to Berkeley and nervous, too. \
Don't worry, there will be plenty of other opportunities to meet people! Go ahead and continue binging your favorite \
Netflix show and order takeout. No judgement.\n ", 100)
 	
time.sleep(3)

###############
# Joining clubs
###############

os.system('cls' if os.name == 'nt' else 'clear')
part_4 = text2art("Part 4: Joining Clubs")
print(part_4)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nCalapalooza is today and you have no idea what to join?!? There are so many clubs on campus from singing groups to service clubs to professional clubs. \nHow are there so many business clubs?? Why do they have applications? Nothing makes sense :( \n", 100)
time.sleep(1)
slow_type("Okay, breathe.")
slow_type("There are a ton of awesome clubs to join and also 8 whole semesters for you to join them. Just take flyers from things that interest you \nand don't let it get you down if you don't get into one of them! Try to choose some that have applications, and some that don't! \n", 100)

clubs_w_apps = ["Berkeley Forum", "Drawn to Scale Acappella", "Mobile Developers at Berkeley", "Cal Dragon Boat", "AFX"]
clubs_wo_apps = ["Songwriting at Berkeley", "Association of Women in EECS (AWE)", "Open Computing Facility (OCF)", "Society of Women Engineers (SWE)", "Salsa at Cal"]

time.sleep(2)
slow_type("\nFor the following choices, use the corresponding number for each club. \n")

for club in range(len(clubs_w_apps)):
	print("\033[0;35;40m" + str(clubs_w_apps[club]) + " - " + str(club+1))

print("\033[0;0m")
time.sleep(2)

club1 = int(input("\nAll of these clubs have applications, but don't shy away from them. Give it your best shot! Choose one to apply to: ").strip())
club1 = clubs_w_apps[club1 - 1]

print("\n" + club1 + ", great choice! Now for some clubs without applications.")

time.sleep(2)
print("\nFor the following choices, use the corresponding number for each club. \n")

for club in range(len(clubs_wo_apps)):
	print("\033[0;35;40m" + str(clubs_wo_apps[club]) + " - " + str(club+1))

print("\033[0;0m")
time.sleep(2)

club2 = int(input("None of these clubs have applications, so just go to their general meetings and see what they're all about! Choose one to try out: ").strip())
club2 = clubs_wo_apps[club2 - 1]

slow_type("\nGo you! You've taken a big step and decided to join some clubs! This will help you start to build your community here at Cal. Best of luck with your " + club1 + " application and I hope you have fun at " + club2 + "'s first GM!\n", 100)
time.sleep(2)

##############
# Getting sick
##############

os.system('cls' if os.name == 'nt' else 'clear')
part_5 = text2art("Part 5: Getting Sick")
print(part_5)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nSadly getting sick is a part of life, but it can be scary sometimes when you're so far away from home and don't know what to do.\n", 100)
slow_type("\nThis is the first time that you've been away from home for so long, and you woke up today puking.\n")

options = ["call home", "cry in bed and hope you'll feel better soon", "take whatever medicine your roommate just handed you", "go to Tang Center"]

time.sleep(2)

print("\nFor the following choices, use the corresponding number. \n")

for option in range(len(options)):
	print("\033[0;35;40m" + str(options[option]) + " - " + str(option+1))
	time.sleep(1)

print("\033[0;0m")
time.sleep(2)

sick_choice = int(input("\nWhat do you do? Type the number of your choice. ").strip())

if options[sick_choice-1] == "go to Tang Center":
	slow_type("\nGoing to the Tang Center is definitely the best option, since they can run tests and write you a doctor's note to miss class.\n", 100)
else:
	slow_type("\nYou can " + str(options[sick_choice - 1]) + ", but your best option is probably to go to the Tang Center, since they can run tests and write you a doctor's note to miss class if needed.\n", 100)

time.sleep(2)

##################
#Going to Get Boba
##################

os.system('cls' if os.name == 'nt' else 'clear')
part_6 = text2art("Part 6: Going to Get Boba")
print(part_6)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

boba_places = ["Gong Cha", "U Cha", "Sharetea", "Purple Kow", "RareTea", "Asha", "Tea One", "Happy Lemon", "T Zone", "Yi Fang"]

def get_boba():
	slow_type("\nAhhh! The boba cravings attack again!!! You and your friends really wanna get boba but can't decide between two places. \nThey turn to you, " + name + ", to make the final decision for them.", 100)
	first_choice = str(random.choice(boba_places))
	second_choice = str(random.choice(boba_places))
	while first_choice == second_choice:
		second_choice = str(random.choice(boba_places))
	slow_type("\nWhere should you get boba? " + first_choice + " or " + second_choice + "?")
	boba_choice = input()
	slow_type("\n" + boba_choice + " it is! Good choice!")
	time.sleep(2)
	return boba_choice

boba_choice = get_boba()

##############
#Getting a job
##############

os.system('cls' if os.name == 'nt' else 'clear')
part_7 = text2art("Part 7: Getting a Job")
print(part_7)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nIt's been a few weeks and boba has already started to hurt your bank account. It's time to get a job!\n", 100)
slow_type("\nYou have a few options for on-campus jobs. Where do you want to work?\n", 100)

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nFor the following choices, use the corresponding number for each job. \n")

jobs = ["library information desk worker", "Cal Dining worker", "research assistant", "Cal Performances usher", "call center worker"]

for job in range(len(jobs)):
	print("\033[0;35;40m" + str(jobs[job]) + " - " + str(job+1))

print("\033[0;0m")
time.sleep(2)

first_choice = int(input("\nWhat's your first choice: ").strip())
second_choice = int(input("\nWhat's your second choice: ").strip())

job = random.choice([first_choice, second_choice])

if job == first_choice:
	slow_type("\nCongrats! You got your first choice job as a " + str(jobs[job-1]) + ".\n", 100)
else:
	slow_type("\nYour interview for " + jobs[first_choice - 1] + " didn't go too well, so you got your second choice job as a " + jobs[job-1] + ", but I'm sure it'll still be great!\n", 100)

time.sleep(2)

#################
#Going to Lecture
#################

os.system('cls' if os.name == 'nt' else 'clear')
part_8 = text2art("Part 8: Going to Lecture")
print(part_8)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

slow_type("\nThere are only a few weeks left in the semester and you're quite behind in CS 61A. \nCrap! Should you still attend lecture or watch them at home on 2x speed? \n\nAnswer 1 for attending lecture, 2 for watching at home.", 100)
cs61alecture = input()
if cs61alecture == 1:
	rand = random.randint(1,4)
	if rand <= 3:
		result = "\nYour choice paid off. You got a good grade in CS61A!"
		slow_type(result, 70)
	else:
		result = "\nThat didn't work so well and your grade in CS61A isn't what you expected. Don't worry, though, it's only the first semester!"
		slow_type(result, 100)
else:
	rand = random.randint(1,2)
	if rand == 1:
		result = "\nYour choice paid off. You got a good grade in CS61A!"
		slow_type(result, 70)
	else:
		result = "\nThat didn't work so well and your grade in CS61A isn't what you expected. Don't worry, though, it's only the first semester!"
		slow_type(result, 100)

time.sleep(2)

############
# Conclusion
############

os.system('cls' if os.name == 'nt' else 'clear')
conclusion = text2art("Conclusion")
print(conclusion)
input("Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

# intro
slow_type("\nCongrats, " + name + "! Your first semester at Cal has officially ended, and what a semester you had!")

# dorm
if dorm != first_dorm:
	slow_type("You chose your top-three dorms, and didn't end up with your first choice of " + dorms[first_dorm-1] + ", but you still ended up with a great dorm: " + dorms[dorm-1] + "!")	
else:
	slow_type("You chose your top-three dorms, and got your first choice of " + dorms[dorm-1] + "!")

# roommate
if your_roommate == amy or your_roommate == michelle:
	slow_type("You chose to room with " + your_roommate[0] + ", whom you knew before coming into Cal!")
else:
	slow_type("You chose random roommate assignment and ended up with " + your_roommate[0] + " and for better or for worse you have another semester left with them!")

# friends
intro = "On your first night in the dorms, you "
if talk == 'y':
	slow_type(intro + "hung out with some people on your floor and then went to eat at " + dinner + ". They became some of your closest friends after that night.")
else:
	slow_type(intro + "chose to stay in and relax with some Netflix, but later on you made some awesome friends that understand when you don't feel like going out.")

#clubs
accepted = random.randint(0, 1)
if accepted:
	slow_type("You applied to " + club1 + " and got in! You also tried out " + club2 + " and liked being a part of it, as well!")
else:
	slow_type("You applied to " + club1 + ", but didn't get in :(. It's okay, though, because you also went to " + club2 + "'s first GM and loved it. Plus, if you still want to join " + club1 + ", there's always next semester!")

#getting sick
if sick_choice == "go to Tang Center":
	slow_type("You even got sick this semester, and decided to " + options[sick_choice - 1] + " and ended up fine #gobears.")
else:
	slow_type("You even got sick this semester, and although all you wanted to do was " + options[sick_choice - 1] + ", you decided to go to Tang Center and ended up fine #gobears.")

#boba
slow_type("Throughout the semester, you went to get boba (many, many times) and when your friends needed you to settle their boba debate, you chose " + boba_choice + "like a pro.")

#job
intro = "You ended up needing to get a part-time job during the semester." 
if job == first_choice:
	slow_type(intro + " After some applications, you got an offer from your first choice job as a " + jobs[job-1] + "!")
else:
	slow_type(intro + " You didn't get your first choice, but you still ended up loving it anyway as a " + jobs[job-1] + "!") 

#61a
slow_type("And finally, the defining part of first semester for so many...CS61A. Every year, thousands of bright-eyed freshmen are faced with a very difficult decision: to go or not to go to lecture.")
if cs61alecture == 1:
	slow_type("You chose to attend lecture. " + result)
else:
	slow_type("You chose to not attend lecture and watch the webcasts instead. " + result)

the_end = text2art("The   End")
print(the_end)

#variables to include:
# Intro: name
# Dorm: dorm
# Roommate: your_roommate
# Friends: talk (y/n), dinner (1/2 croads or asian ghetto)
# Clubs: club1 (app), club2 (no app) 
# Getting sick: sick_choice
# Boba: boba_choice
# Job: job
# 61A: cs61alecture, good_grade (True/False)