import random
choices = ("rock","paper","scissor")
player_choice = None

while True :
    player_choice = input("Enter Your Choice ")
    computer_choice = random.choice(choices)
    ########
    ##
    print(f"your choice is {player_choice}\ncomputer choice is {computer_choice}")
    ##
    ######
    if player_choice == computer_choice:
        print("Draw😒")
    elif player_choice == "rock" and computer_choice == "scissor":
        print("You Win😉")
    elif player_choice =="scissor" and computer_choice == "paper":
        print("You Win😉")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win😉")
    else:
        print("sorry, You lose🥲")
    
    quit_flag = input("\ndo you wanna compelete ? (y/n) : ".lower())
    if not quit_flag == "y":
        break