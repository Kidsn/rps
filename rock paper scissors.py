import random
from datetime import datetime
random.seed(datetime.now().timestamp())

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

print("Ready?")

while True:
    computer = random.choice(options)

    player = input("Enter a choice (rock, paper, scissors): ")
    print(f"(player) {player}")
    print(f"(computer) {computer}")

    if player_score == 3:
        print("victory")
        replay = input("Play again? (y/n): ").lower()
        if replay == "y":
            player_score, computer_score = 0, 0
            continue
        else:
            break
    elif computer_score == 3:
        print("You Suck")
        replay = input("Play again? (y/n): ").lower()
        if replay == "y":
            player_score, computer_score = 0, 0
            continue
        else:
            break
    else:
        if player == computer:
            print("Draw! No points awarded")
            print(player_score, computer_score)
        elif player == "rock" and computer == "scissors":
            print("Point goes to player")
            player_score += 1
            print(player_score, computer_score)
        elif player == "scissors" and computer == "paper":
            print("Point goes to player")
            player_score += 1
            print(player_score, computer_score)
        elif player == "paper" and computer == "rock":
            print("Point goes to player")
            player_score += 1
            print(player_score, computer_score)
        else:
            print("Point goes to Computer")
            computer_score += 1
            print(player_score, computer_score)