user_score = 0
computer_score = 0
round = 0
while True:
    user_choice = input("First to 3! Best of 5! Rock, Paper or Scissors? ")
    import random
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    print(f"You chose {user_choice} and the computer chose {computer_choice}")
    if computer_choice == user_choice:
        print("You and the computer have tied, choose again.")
        round +=1
    elif computer_choice == "Rock" and user_choice == "Paper":
        print("Paper wraps rock, you win! Choose again.")
        user_score +=1
        round +=1
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print("Scissors cut paper, you win! Choose again.")
        user_score +=1
        round +=1
    elif computer_choice == "Scissors" and user_choice == "Rock":
        print("Rock smashes scissors, you win! Choose again.")
        user_score +=1
        round +=1
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("Paper wraps rock, you lose :-( Choose again.")
        computer_score +=1
        round +=1
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("Rock smashes scissors, you lose :-( Choose again.")
        computer_score +=1
        round +=1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("Scissors cut paper, you lose :-( Choose again.")
        computer_score +=1
        round +=1
    if user_score > 2:
        print ("Game Over! Computer wins... :-(")
        break
    elif user_score > 2:
        print ("Game Over! You win!")
        break
    elif round > 5:
        if user_score > computer_score:
            print("Game Over! You win!")
            break
        elif computer_score > user_score:
            print("Game Over! Computer wins... :-(")
            break
        else:
            print("You and the computer have tied, choose again.")
            break











