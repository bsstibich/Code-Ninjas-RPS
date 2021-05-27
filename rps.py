import random
play_trigger = True

while play_trigger:
    print("Rock, Paper, Scissors!")
    print("======================")

    player_choice = input("What do you choose?\n  r  p  s\n")
    computer_choice = random.choice(('r', 'p', 's'))
    
    print("Computer chooses " + computer_choice)

    if player_choice == "r":
        if computer_choice == 'p':
            print("You Lose!")
        if computer_choice == 'r':
            print("Draw!")
        if computer_choice == 's':
            print("You Win!")

    if player_choice == "p":
        if computer_choice == 'p':
            print("Draw!")
        if computer_choice == 'r':
            print("You Win!")
        if computer_choice == 's':
            print("You Lose!")

    if player_choice == "s":
        if computer_choice == 'p':
            print("You Win!")
        if computer_choice == 'r':
            print("You Lose!")
        if computer_choice == 's':
            print("Draw!")

    
    try_again = input("Try Again?\n  y  n\n")
    if try_again == 'n':
        play_trigger = False
        print("Goodbye!")