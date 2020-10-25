import random
x = ""
y = ""
computer1_score = 0
computer2_score = 0
game_num = 0
start = "Y"
ROUNDS = 100000
RPSScoreFile = open('RPSScoreFile.txt','a')

def results(computer1, computer2):
	global computer1_score, computer2_score
	result = ""
	if computer1 == computer2:
		result = "0"
		computer1_score += 0.5
		computer2_score += 0.5
	elif computer1 == 1 and computer2 == 2:
		result = "2"
		computer2_score +=1
	elif computer1 == 1 and computer2 == 3:
		result = "1"
		computer1_score +=1
	elif computer1 == 2 and computer2 == 1:
		result = "1"
		computer1_score += 1
	elif computer1 == 2 and computer2 == 3:
		result = "2"
		computer2_score +=1
	elif computer1 == 3 and computer2 == 1:
		result = "2"
		computer2_score += 1
	elif computer1 == 3 and computer2 == 2:
		result = "1"
		computer1_score +=1
	storeResult(computer1, computer2, result)

def play ():
	global x, y

	for i in range(ROUNDS):
		
		computer1 = random.randrange(1, 4)
		computer2 = random.randrange(1, 4)
		results(computer1, computer2)

def storeResult(x,y,result):
	RPSScoreFile.write(str(x) + ',' + str(y) + ',' + result + '\n')

start = input("This program would play the game for %s times. Start? (Y/N) " % ROUNDS)
if start.upper() == "Y":
	play()
else:
	quit()

print("\nFinal Score:")
print("Computer1 :", computer1_score, " Computer2 :",  computer2_score)
if computer1_score > computer2_score:
	print("Computer1 is the WINNER!!")
elif computer2_score > computer1_score:
	print("Computer2 is the WINNER!!")
else:
	print("It's a draw!")
RPSScoreFile.close()