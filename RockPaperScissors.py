import random
x = ""
y = ""
com_score = 0
player_score = 0
game_num = 0

def results(x, y):
	global com_score, player_score
	result = ""
	if x == y:
		result = "It's a Draw."
		com_score += 0.5
		player_score += 0.5
	elif x == "rock" and y == "paper":
		result = "You win!"
		player_score +=1
	elif x == "rock" and y == "scissors":
		result = "Computer wins!"
		com_score +=1
	elif x == "paper" and y == "rock":
		result = "Computer wins!"
		com_score += 1
	elif x == "paper" and y == "scissors":
		result = "You win!"
		player_score +=1
	elif x == "scissors" and y == "rock":
		result = "You win!"
		player_score += 1
	elif x == "scissors" and y == "paper":
		result = "Computer wins!"
		com_score +=1
	print("Computer picked", x,"and You picked",  y, ".", result, "\n")
	print("---------------------------------------------------------")

def play ():
	global x, y, com_score, player_score

	for i in range(5):
		player = input("\nGame number: ( "+ str(i+1) + " ). Score: You(" +str(player_score)+ "), Com(" +str(com_score)+ ") \nEnter your choice: \n (1) for rock \n (2) for paper \n (3) for scissors\n\n    ")
	
		if player == "1":
			y = ("rock")
			# print("you pick :", y)
		elif player == "2":
			y = ("paper")
			# print("you pick :", y)
		elif player == "3":
			y = ("scissors")
			# print("you pick :", y)
		else:
			print("Pagle, Enter a valid choice i.e. a number from 1 to 3. \n You LOST one point. ready for next......")
			y = ""
			com_score += 1	

		computer = random.randrange(1, 4)
		if computer == 1:
			x = ("rock")
		elif computer == 2:
			x = ("paper")
		elif computer == 3:
			x = ("scissors")

		results(x, y)

name = input("\nEnter your name: ").title()
print("\nHello,", name, "welcome to the 'Rock-Paper-Scissors' Game")
print("---------------------------------------------------------")

start = input("Do you want to play?(Y/N): ").upper()

if start == "Y":
	print("You have total five chances")
	print()
	
	play()
elif start == "N":
	print("OK, come some other time to play this game, You COWARD!")
else:
	print("I did not understand that. Try again later.")

print("\nFinal Score:")
print(name,":", player_score, " Computer:",  com_score)
if com_score > player_score:
	print("Computer is the WINNER!!")
elif player_score > com_score:
	print(name, "is the WINNER!!")
else:
	print("It's a draw!")