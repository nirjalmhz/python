import random
move = random.choice(["rock", "paper", "scissor"])
user = input("Rock, Paper, or Scissor? ").strip().lower()

print("Computer chose:", move)

if user == move:
    print("It's a Tie!")
elif (user == "rock" and move == "scissor") or \
     (user == "scissor" and move == "paper") or \
     (user == "paper" and move == "rock"):
    print("Congratulations! You Won!")
elif user in ["rock", "paper", "scissor"]:
    print("You Lose!")
else:
    print("Invalid input. Please enter Rock, Paper, or Scissor.")
