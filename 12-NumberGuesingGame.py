from random import randint

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


def check_answer(guess,answer,turns):
	if guess>answer:
		print("too high")
		
		return turns -1
	elif answer>guess:
		print("too low")
		return turns -1
	else:
		print(f"You got it! The answer was {answer}")

def set_difficulty():
	level =input("Choose a difficulty. Tyoe 'easy' or 'hard'")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def game():
	print("welvome to the number gueaing game")
	print("I m thinking of a number between 1 and 100")
	answer=randint(1,100)
	print(f"shhht, the correct answer is {answer}")

	turns =set_difficulty()

	guess = 0
	while guess != answer:
		print(f"You have {turns} attempts remaining to guess the number")
		guess = int(input("Make a guess"))
		turns=check_answer(guess,answer,turns)
		if turns==0:
			print("you have run out of gueses, you lost")
			return
		elif guess!= answer:
			print("guess again")
game()