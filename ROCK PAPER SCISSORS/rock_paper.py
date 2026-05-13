#==============ROCK PAPER SCISSORS GAME==============
import random

choices = ("rock","paper","scissors")
player_score = 0
computer_score = 0
running = True



while running:
    computer = random.choice(choices)
    player = input("Enter rock, paper or scissors(q to quit): ")
    if player.lower() == "q":
        print("Game ended")
        break
    if player not in choices:
        print("Invalid!")
        continue

    print(f"Computer: {computer}")
    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You Win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You Win!")
        player_score += 1
    
    else:
        print("You lose")
        computer_score += 1        
    if player_score == 3:
        print("🎉 You won the match!")
        print(f"Score: {player_score}")
        break
    if computer_score == 3:
        print("💻 Computer won the match!")
        break