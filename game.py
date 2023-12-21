# this is the rock, paper, scissors game create by Adhunik Ganit ~Prajwal Yadav
import random

options = ("rock","paper","scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors) : ")
        break

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print(" It's a tie! ")
    elif player == "Rock" and computer =="Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You Win!")
    elif player == "Scissors" and computer == "Paper":
        print("you win!")
    else:
        print("You lose!")

    if not input("Play again?(y/n) :").lower() == "y":
        running = False

print("Thanks for playing!")