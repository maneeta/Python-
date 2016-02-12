import random
player = eval(input("scissor (0), rock (1), paper (2) : "))
computer = random.randint(0,2)
if player == 0:
	if computer == 0:
		print("The computer is scissor. You are scissor too. It is a draw.")
	elif computer == 1:
		print("The computer is rock. You are scissor. You won.")
	elif computer == 2:
		print("The computer is paper. You are scissor. You won.")
elif player == 1:
	if computer == 0:
		print("The computer is scissor. You are rock. You won.")
	elif computer == 1:
		print("The computer is rock. You are rock too. It is a draw.")
	elif computer == 2:
		print("The computer is paper. You are rock. Computer won.")
elif player == 2:
	if computer == 0:
		print("The computer is scissor. You are paper. Computer won.")
	elif computer == 1:
		print("The computer is rock. You are paper. You won.")
	elif computer == 2:
		print("The computer is paper. You are paper too. It is a draw.")
else:
	print("Enter valid number")
	
