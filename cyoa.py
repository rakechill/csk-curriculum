import random
from art import *

header = text2art("Go Bears!")
print(header)


# ~ Intro ~
print("Hello there! Before we embark on this Cal adventure, what is your name?")
name = input()

print("Congratulations, " + name + ". You are going to be a student at the world's number one public university! Woohoo! \
This definitely calls for a Go Bears! Your first decision as a fresh new Cal Bear is to pick your top 3 \
dorms to live in. What shall it be? The ever lush Clark Kerr Campus? Or Unit 1 the #1? Or perhaps Berkeley's \
newest dorm, Blackwell? Choose wisely!\n")

dorms = ["Unit 1", "Unit 2", "Unit 3", "Stern", "Foothill", "Bowles", "Clark Kerr", "Blackwell"]

print("For the following choices, use the corresponding number for each dorm.")
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


print("Your assignment has been chosen! " + str(dorms[dorm-1]) + " will be your dorm for the year!")

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

# Example of a choice that impacts the storyline

print("There are only a few weeks left in the semester and you're quite behind in CS 61A. Crap! Should you still attend lecture or watch them at home on 2x speed? Answer 1 for attending lecture, 2 for watching at home.")
cs61alecture = input()
if cs61alecture == 1:
	rand = random.randint(1,4)
	if rand <= 3:
		print("Yay! Your choice paid off. You got a good grade in CS61A.")
	else:
		print("Crap. Maybe that didn't work so well. Your grade in CS61A isn't what you expected. Don't worry, it's only the first class though!")
else:
	rand = random.randint(1,2)
	if rand == 1:
		print("Yay! Your choice paid off. You got a good grade in CS61A.")
	else:
		print("Crap. Maybe that didn't work so well. Your grade in CS61A isn't what you expected. Don't worry, it's only the first class though!")

# Later in the storyline, can reference the grade in CS61A